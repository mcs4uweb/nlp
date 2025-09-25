import json
import os
import mimetypes
import traceback
from typing import Dict, Any, TYPE_CHECKING
from uuid import uuid4
from datetime import datetime
import smtplib
from pathlib import Path
from email.message import EmailMessage
try:
    from anthropic import Anthropic, APIStatusError
except ImportError:
    Anthropic = None
    APIStatusError = Exception

try:
    import google.generativeai as genai
except ImportError:
    genai = None
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter

"""
THIS FUNCTION IS NOT YET IMPLEMENTED
"""
from constants.xml_constants import XmlConstants
from constants.prompts import Prompts
from services.aws.lambda_event_helper import LambdaEventHelper
from services.application.messages.mepcom_nlp_processing_messages import MEPCOMNLPProcessingMessages
from utils.xml_parser import XmlParserUtil
from utils.xml_parser import CDAParserUtil
# inline DI container initialization needed for Lambda execution
from logging_container import LoggingContainer
logging_container = LoggingContainer()
from container import Container
if TYPE_CHECKING:
    from services.aws.s3_service import S3Service



system_prompt = (
    """
Your Goal: Analyze a patient's clinical note against specific U.S. Department of Defense medical standards (DODI 6130.03, Volume 1, Section 5) to determine if the patient has medical conditions that would disqualify or potentially disqualify them from military service.
Source Documents:
1.	The Clinical Note provided below.
2.	DoD Instruction 6130.03, Volume 1: You must use the standards found only in Section 5: DISQUALIFYING CONDITIONS. (Assume you have access to this document).
Instructions (Follow these steps precisely):
Step 1: Read the Clinical Note Carefully.
•	Understand the patient's current health issues, past medical history, and any diagnoses mentioned.
Step 2: Identify Relevant Medical Information.
•	Look for any specific medical diagnoses (like "diabetes mellitus" or "ulcerative colitis").
•	Look for any history of significant medical events (like "psychotic episode" or "surgery").
•	Look for any symptoms or findings mentioned that might relate to a disqualifying condition.
Step 3: Compare with DODI Section 5 Standards.
•	For each piece of relevant medical information identified in Step 2, check if it matches any of the disqualifying conditions listed in Section 5 of DODI 6130.03, Volume 1.
Step 4: Determine the Correct Flag Type (DISQUALIFYING or POTENTIALLY DISQUALIFYING).
•	DISQUALIFYING: Assign the flag [FLAG - DISQUALIFYING] if the clinical note confirms that the patient currently has or has a history of a condition that is listed as disqualifying in DODI Section 5.
o	Example: If the note says "Patient has history of asthma after age 13" and DODI Section 5.10.e says "History of airway hyper responsiveness including asthma...after the 13th birthday," this is DISQUALIFYING. It's a confirmed history matching the standard.
•	POTENTIALLY DISQUALIFYING: Assign the flag [FLAG - POTENTIALLY DISQUALIFYING] ONLY IF the clinical note explicitly states there is uncertainty about a diagnosis (using words like "possible," "suspected," "rule out," "differential diagnosis includes") AND that specific condition, if it were confirmed, is listed as disqualifying in DODI Section 5.
o	Example: If the note says "Impression: Possible sleep apnea, requires sleep study for confirmation" and DODI Section 5.27.b lists "sleep-related breathing disorders, including but not limited to sleep apnea" as disqualifying, this is POTENTIALLY DISQUALIFYING. The diagnosis is uncertain in the note, but would be disqualifying if confirmed.
o	IMPORTANT: Do not use this flag for conditions that are confirmed in the note, even if they happened in the past or are currently managed. If a confirmed condition matches a DODI standard, it is DISQUALIFYING, not potentially disqualifying.
•	NO FLAG: If a condition mentioned in the note is not listed in DODI Section 5, or if it clearly meets an exception described within a standard in Section 5, do not create a flag for it.
Step 5: Determine the Overall Eligibility Status.
•	Look at all the flags you created in Step 4.
•	If there is at least one [FLAG - DISQUALIFYING] flag, the overall status for the patient is DISQUALIFIED.
•	If there are only [FLAG - POTENTIALLY DISQUALIFYING] flags (and zero DISQUALIFYING flags), the overall status is POTENTIALLY DISQUALIFIED.
•	If there are no flags created at all, the overall status is QUALIFIED.
•	Write this overall status at the very beginning of your response, after a placeholder name like "Doe, Jane".
Step 6: Format Your Response Using Markdown EXACTLY Like the Example Below.
•	Start with the placeholder name and the overall eligibility status (bolded).
•	Use the heading "Military Eligibility Medical Flags:".
•	For each flag you created in Step 4, use the following Markdown structure:
o	Start with the flag type (e.g., [FLAG - DISQUALIFYING]) on its own line.
o	Condition: [Name of the Condition]
o	Clinical Encounter Text: "[Exact quote from the clinical note related to that condition]"
o	DODI 6130.03, Vol 1 - Section [Section Number, e.g., 5.XX.y.(z)] Text: "[Exact quote of the disqualifying standard from the DODI document]"
o	Add a blank line between each complete flag entry.
Example Output Format (Formatted with Markdown):
Doe, Jane DISQUALIFIED
Military Eligibility Medical Flags:
[FLAG - DISQUALIFYING]
Condition: Asthma
Clinical Encounter Text: "Patient has history of asthma after age 13, uses rescue inhaler occasionally."
DODI 6130.03, Vol 1 - Section 5.10.e Text: "History of airway hyper responsiveness including asthma, reactive airway disease, exercise-induced bronchospasm or asthmatic bronchitis, after the 13th birthday."
[FLAG - POTENTIALLY DISQUALIFYING]
Condition: Sleep Apnea
Clinical Encounter Text: "Impression: Possible sleep apnea, requires sleep study for confirmation"
DODI 6130.03, Vol 1 - Section 5.27.b Text: "Current diagnosis or treatment of sleep-related breathing disorders, including but not limited to sleep apnea."
(Add more flags as needed, following the same structure and adding a blank line between each flag)
"""
)
container = Container()
report_service = container.clinical_report_service()
EMAIL_TO   = os.environ.get("EMAIL_TO", "mike.hubbs@natgodatagroup.com")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASS = os.getenv("EMAIL_PASS")

SUPPORTED_S3_FILE_TYPES = {"txt", "docx", "pdf", "xml"}
CONTENT_TYPE_TO_TYPE = {
    "text/plain": "txt",
    "application/pdf": "pdf",
    "application/xml": "xml",
    "text/xml": "xml",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx",
}
EXTENSION_ALIASES = {"pdt": "pdf"}

def send_email(subject: str, body: str):
    """
    Send an email via Gmail SMTP to the fixed recipient (EMAIL_TO).
    """
    if not EMAIL_FROM or not EMAIL_PASS:
        
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_PASS)
            smtp.send_message(msg)
    except Exception as e:
        print(str(e))

def determine_s3_file_type(s3_service: "S3Service", bucket_name: str, key: str) -> str:
    """Resolve the logical type for an S3 object we need to process."""
    content_type = ""
    try:
        head = s3_service.s3_client.head_object(Bucket=bucket_name, Key=key)
        content_type = (head.get('ContentType') or "").split(';', 1)[0].strip().lower()
    except Exception:
        content_type = ""

    if content_type:
        mapped = CONTENT_TYPE_TO_TYPE.get(content_type)
        if mapped:
            return mapped

    guessed_type, _ = mimetypes.guess_type(key)
    if guessed_type:
        mapped = CONTENT_TYPE_TO_TYPE.get(guessed_type.lower())
        if mapped:
            return mapped

    extension = Path(key).suffix.lower().lstrip('.')
    if extension in SUPPORTED_S3_FILE_TYPES:
        return extension
    if extension in EXTENSION_ALIASES:
        return EXTENSION_ALIASES[extension]

    raise ValueError(f"Unsupported S3 file type for key: {key}")



def call_claude_sonnet(prompt: str, notes: str, api_key: str):
    if Anthropic is None:
        raise ImportError("anthropic package is not installed")
    if not api_key:
        raise ValueError("Anthropic API key is required")
    client = Anthropic(api_key=api_key)
    user_block = {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "text", "text": f"\n\nClinical Notes:\n{notes}"}
        ]
    }
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8192,
        temperature=0,
        messages=[user_block]
    )
    output_string = "".join(part.text for part in msg.content if hasattr(part, "text"))
    return {"text": output_string, "model": "claude-3-5-sonnet-20240620"}

def call_gemini_flash(prompt: str, notes: str, api_key: str):
    """Call the Gemini 2.0 Flash model and return a simplified response dict.

    Raises:
        ImportError: If the google-generativeai dependency is unavailable.
        ValueError: If an API key is not provided.
    """
    if genai is None:
        raise ImportError("google-generativeai package is not installed")
    if not api_key:
        raise ValueError("Gemini API key is required")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"{prompt}\n\nClinical Notes:\n{notes}",
        generation_config={"temperature": 0, "max_output_tokens": 8192},
    )
    text_output = getattr(response, "text", None)
    if not text_output:
        collected_parts = []
        try:
            for candidate in getattr(response, "candidates", []) or []:
                content = getattr(candidate, "content", None)
                if content and hasattr(content, "parts"):
                    for part in content.parts:
                        part_text = getattr(part, "text", None)
                        if part_text:
                            collected_parts.append(part_text)
        except Exception:
            pass
        text_output = "".join(collected_parts).strip()
    return {"text": text_output or "", "model": "gemini-2.0-flash"}

def extract_patient_demographics(summary_note: Dict[str, Any]) -> Dict[str, Any]:
    """Safely extract patient demographics from a parsed summary note.

    Args:
        summary_note: The dict returned by `CDAParserUtil.parse_to_summary_note()`
            which contains a `patient_demographics` key.

    Returns:
        A dict with keys: `first_name`, `last_name`, `gender`, `date_of_birth`,
        `ssn`, and `dod_id`. Missing values are returned as None.
    """
   
    demographics = summary_note.get("patient_demographics") or {}
    first = demographics.get("first_name")
    last = demographics.get("last_name")
    data_dict = {
        "first_name": first,
        "last_name": last,
        "gender": demographics.get("gender"),
        "date_of_birth": demographics.get("date_of_birth"),
        "ssn": demographics.get("ssn"),
        "dod_id": demographics.get("dod_id"),
        "full_name": (f"{first} {last}".strip() if (first or last) else None),
        }
    return json.dumps(data_dict)

def lambda_handler(event, context):

    # initialize variables for possible error handling
    
    sample_medical_note = (
            "Patient name: Alexis Carter is a 45-year-old male with a history of hypertension "
            "and type 2 diabetes. He presents with a chief complaint of "
            "a persistent cough for the last 2 weeks. He was prescribed "
            "Lisinopril 20mg daily. Physical examination reveals "
            "clear lungs. No signs of acute distress. The patient denies "
            "any fever or chest pain. We will start him on Amoxicillin 500mg."
        )
    xml_data = XmlConstants.THORACIC_TEST_REPORT_XML
    
    raw_cda_xml = XmlConstants.TEST_REPORT_XML
    readable_notes = CDAParserUtil(raw_cda_xml)
    test = readable_notes.parse_to_summary_note()
    firstName = test.get("patient_demographics", {}).get("first_name")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    t = extract_patient_demographics(test)
    data = json.loads(t)
    print(data['first_name'])
    assessment_plan_text = test.get("clinical_notes", {}).get("assessment_and_plan")
    encounters = test.get("clinical_notes", {}).get("encounters")
    cda_parser = CDAParserUtil(raw_cda_xml)
    
    persons_table="[MEPCOM_DEV].[mirs].[Person]"  
    
    try:

        try:
            api_key_a = os.getenv('ANTHROPIC_API_KEY')
            gemini_api = os.getenv('GEMINI_API_KEY')
            client = None
            response = None

            if api_key_a and Anthropic is not None:
                try:
                    client = Anthropic(api_key=api_key_a)
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=10,
                        messages=[{"role": "user", "content": "Hi"}]
                    )
                except Exception as e:
                    # Don't crash startup on a failed sample call; log and continue.
                    print(f"Anthropic client creation or sample call failed: {e}")
            """
            prompt = "Tell me something about ICD 10 codes"
            notes = "This patient has severe asthma"
            #call_gemini_flash(prompt=prompt, notes=notes, api_key=gemini_api)
            calls = []
            if api_key_a and Anthropic is not None:
                calls.append(("claude-3-5-sonnet-20240620", lambda: call_claude_sonnet(prompt, notes, api_key_a)))

            results = []

            def execute_with_latency(fn):
                start_time = perf_counter()
                result = fn()
                latency = perf_counter() - start_time
                if isinstance(result, tuple) and result and isinstance(result[0], dict):
                    payload = result[0]
                    extra = result[1]
                    if isinstance(extra, dict):
                        payload = {**payload, **extra}
                elif isinstance(result, dict):
                    payload = result
                else:
                    payload = {"raw_response": result}
                return payload, latency

            if calls:
                try:
                    with ThreadPoolExecutor() as ex:
                        futures = {ex.submit(execute_with_latency, fn): name for name, fn in calls}
                        for fut in as_completed(futures):
                            name = futures[fut]
                            try:
                                payload, latency = fut.result()
                            except Exception as call_exc:
                                print(f"failed service for {name}: {call_exc}")
                                continue
                            payload.setdefault("model", name)
                            payload.setdefault("provider", name)
                            payload["latency_ms"] = int(latency * 1000)
                            results.append(payload)
                except Exception as pool_exc:
                    print(f"failed service: {pool_exc}")
            else:
                print("No LLM calls were configured.")

            tmp = json.dumps({'results': results}) """
        

            xml_parser = XmlParserUtil(xml_data)
            patient_visit_note = xml_parser.parse_to_visit_notes()
            embedded_doc = patient_visit_note.get("embedded_document", {})
            if embedded_doc.get("base64_content"):
                sample_medical_note = embedded_doc.get("base64_content")
            textract_service = container.textract_service()
            
            repo = container.persons_table_repository()
            reporter = container.reporting_repository()
            s3_iterator = container.s3_file_iterator_service()
            s3_service = container.s3_service()
            testChat = s3_service.bedrock_chat(Prompts.DODI, sample_medical_note)
            bucket_name = container.config.pdf_s3_bucket()
            s3Xml = s3_service.get_object_text(bucket_name, "usmepcom/hie-documents/1666701215/0165c859-0a5e-43c2-96f0-ee956d385314.xml")
            temp2 = determine_s3_file_type(s3_service, bucket_name, "usmepcom/hie-documents/1666701219/00e71de1-bbbd-4dbe-bc10-991adedbd6cc.pdf")
            tmp = determine_s3_file_type(s3_service, bucket_name, "usmepcom/hie-documents/1666701215/AlexisCarter_111222333.docx")
            wordDoc = s3_service.get_word_document_text(bucket_name, "usmepcom/hie-documents/1666701215/AlexisCarter_111222333.docx")
            t = s3_iterator.iterate_objects(bucket_name, prefix="usmepcom/hie-documents/1666701215/0165c859-0a5e-43c2-96f0-ee956d385314.xml", suffix=".xml")
            #clinicalPatient = s3_service.extract_text_from_pdf(bucket_name, "usmepcom/hie-documents/1666701219/clinical_note_wagner_matteo.pdf")
            """ for obj in t:
                print(f"Found S3 object: {obj['Key']} (Size: {obj['Size']} bytes)")
                s3_object = s3_service.get_file(bucket_name, obj['Key'])
                if s3_object:
                    xml_content = s3_object['Body'].read().decode('utf-8')
                    cda_parser = CDAParserUtil(xml_content)
                    parsed_note = cda_parser.parse_to_summary_note()
                    note_text = parsed_note.get("clinical_notes", {}).get("note_text", "")
                    print(f"Extracted Note Text: {note_text[:100]}...")  # Print first 100 characters
                else:
                    print(f"Failed to retrieve object: {obj['Key']}") """
            # initialize logging service
            logger = logging_container.logger().get_logger()
            # initialize other services
            #cont = container.database_connection_service()
            s3 = container.s3_service()
            #bucketName = s3.store_file('digin-di-testing', 'mike.txt', b'Hello from Mike!', content_type='text/plain')
            comprehend_service = container.comprehend_medical_service()
            secrets = container.secrets_manager_service()
            db_service = container.database_connection_service()

            # 1. READ ALL records
            logger.info("Fetching all records...")
            all_records = repo.get_all(table_name=persons_table)
            notesOnPatients = reporter.get_Patients_FileName()
            detected_entities = comprehend_service.detect_entities(sample_medical_note)
            icd10_response = comprehend_service.detect_ICD10(sample_medical_note)
            for note in notesOnPatients:
                note_text = note.get("FilePath")
            
                #entities = comprehend_service.detect_entities(note_text)
                #note["DetectedEntities"] = entities
            
            print(f"Fetched {len(notesOnPatients)} patient notes from complex query.")
            logger.info(f"Found {len(all_records)} total records.")
            logger.info(f"Fetched {len(notesOnPatients)} patient notes from complex query.")

            health_analysis_json = comprehend_service.analyze_patient_health(sample_medical_note)
    
            # --- 3. Pass the data to the report service to get the formatted summary ---
            physician_summary_text = report_service.generate_clinical_summary(health_analysis_json)
    
            # You can now log this text, save it to a database, or return it.
            print("--- GENERATED CLINICAL SUMMARY ---")
            print(physician_summary_text)
            print("---------------------------------")

        #Create a clinical notes record in the database
            CLINICAL_NOTES_TABLE = "[JCABAN].[mirs].[PerClinicalNote]"

            note_data = {
            "NoteBody": "Patient presents with headache. Denies chest pain...",
            "NoteSource": "Cerner-Encounter-97953477", # A unique source identifier
            "Processed": True,
            "PersonID": 93,
            "NoteSummary": "Initial assessment suggests possible AMI.",
            "ObservationDate": datetime(2023, 1, 8, 22, 25, 37),
            "NoteType": "Admission Note Physician",
            "NoteLocation": "Main Hospital",
            "NoteProvider": "Portal, Portal"
            }
            ##UPDATE database
            """ new_record_id = repo.create(
            table_name=CLINICAL_NOTES_TABLE,
            data=note_data) """

            # ...
        except Exception as e:
            raise Exception(f"Error initializing services: {str(e)}") from e

        # safely extract the input data from the event body before validating
        # log the start of the process
        logger.info(MEPCOMNLPProcessingMessages.PROCESS_STARTED_MESSAGE, extra={
            "event_type": "process_start",
        })


        # TODO: add implementation here


        logger.info(MEPCOMNLPProcessingMessages.PROCESS_COMPLETED_MESSAGE, extra={
            "event_type": "process_complete",
            "other_details": "additional details here"
        })

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"ok",
            }),
        }
    
    except ValueError as e:
        correlation_id = str(uuid4())
        error_message = str(e)
        message = MEPCOMNLPProcessingMessages.INVALID_DATA_MESSAGE
        
        logger.error(message, extra={
            "event_type": "validation_error",
            "error_message": error_message,
            "correlation_id": correlation_id
        })

        return {
            "statusCode": 400,
            "stopProcessing": True,
            "body": json.dumps({
                "message": error_message,
                "correlation_id": correlation_id
            })
        }
    
    except Exception as e:
        correlation_id = str(uuid4())
        error_message = str(e)
        stack_trace = traceback.format_exc()
        message = MEPCOMNLPProcessingMessages.GENERAL_ERROR_MESSAGE

        logger.error(message, extra={
            "event_type": "general_error",
            "error_message": error_message,
            "correlation_id": correlation_id,
            "stack": stack_trace
        })

        return {
            "statusCode": 500,
            "stopProcessing": True,
            "body": json.dumps({
                "message": error_message, 
                "correlation_id": correlation_id
            })
        }
    
    finally:
        # Ensure all handlers are flushed before exiting
        logging_container.logger().flush_all_handlers()

# Test the Lambda handler function locally
def create_event() -> Dict[str, Any]:
    # Create the event object

    event = {
    }
    
    return event

def test_lambda_locally():  
    try:
        test_event = create_event()
        
        # Create a mock context
        class MockContext:
            def __init__(self):
                self.function_name = 'test-function'
                self.function_version = '$LATEST'
                self.memory_limit_in_mb = 128
                self.aws_request_id = '123456'
        
        # Run the handler
        result = lambda_handler(test_event, MockContext())
        print("Lambda execution result:", json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
    

if __name__ == '__main__':
    test_lambda_locally()


