import boto3
from botocore.exceptions import ClientError
from typing import List, Dict, Any
from services.application.condition_scoring_service import ConditionScoringService

class ComprehendMedicalService:
    """
    A service class for interacting with AWS Comprehend Medical to extract
    medical entities from unstructured text.
    """

    def __init__(self, region_name: str, logger: Any, scoring_service: ConditionScoringService):
       
        self.region_name = region_name
        self.client = boto3.client("comprehendmedical", region_name=self.region_name)
        self._scoring_service = scoring_service
        
    def analyze_patient_health(self, text: str) -> Dict[str, Any]:
        """
        Performs a comprehensive health analysis of a medical text
            A dictionary containing the combined health score and detailed findings.
        """
        # 1. Get raw data from AWS Comprehend Medical APIs
        general_entities = self.detect_entities(text)
        icd10_entities = self.detect_ICD10(text)
        
        # 2. Use the scoring service to interpret the raw data
        entity_analysis = self._scoring_service.score_from_entities(general_entities)
        icd10_analysis = self._scoring_service.score_from_icd10(icd10_entities)
        
        # 3. Combine the results into a final report
        total_score = entity_analysis['score'] + icd10_analysis['score']
        
        final_assessment = "Patient appears to have one or more adverse medical conditions." if total_score > 0 else "No significant adverse medical conditions detected."
        
        return {
            "total_health_score": total_score,
            "assessment": final_assessment,
            "details": {
                "entity_analysis": entity_analysis,
                "icd10_diagnosis_analysis": icd10_analysis
            }
        }

    def detect_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Analyzes text to detect medical entities such as PHI, anatomy, and medications.
        This method returns a list of detected entities.

        Args:
            text (str): The unstructured text to analyze (e.g., a doctor's note).

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, where each dictionary represents a
                                  detected medical entity and its attributes. Returns an
                                  empty list if no text is provided or no entities are found.
        
        Raises:
            botocore.exceptions.ClientError: If the AWS API call fails.
        """
        if not text or not text.strip():
            #self.logger.warning("detect_entities called with empty or whitespace-only text.")
            return []

        try:
            # Note: The API has a text size limit of 20,000 UTF-8 characters.
            # For production, you may need to chunk larger texts.
            if len(text.encode('utf-8')) > 20000:
                 #self.logger.warning("Text exceeds 20,000 byte limit for Comprehend Medical. Truncating.")
                 # A simple truncation strategy:
                 text = text.encode('utf-8')[:20000].decode('utf-8', 'ignore')

            """   self.logger.info(
                "Sending text to Comprehend Medical for entity detection.",
                extra={"text_length": len(text)}
            ) """

            # We use detect_entities_v2 as it is the latest and most capable version.
            response = self.client.detect_entities_v2(
                Text=text
            )
            
            entities = response.get("Entities", [])
            """  self.logger.info(
                "Successfully detected medical entities.",
                extra={"entity_count": len(entities)}
            ) """
            
            # The request asks for the JSON entities object, which is this list.
            return entities

        except ClientError as e:
            error_code = e.response.get("Error", {}).get("Code")
            """  self.logger.error(
                "AWS Comprehend Medical API call failed.",
                extra={
                    "error_message": str(e),
                    "aws_error_code": error_code
                }
            ) """
            # Re-raise the exception so the calling function can handle it.
            raise

    def detect_ICD10(self, text: str) -> List[Dict[str, Any]]:
       
        if not text or not text.strip():
            #self.logger.warning("detect_entities called with empty or whitespace-only text.")
            return []

        try:
            # Note: The API has a text size limit of 20,000 UTF-8 characters.
            # For production, you may need to chunk larger texts.
            if len(text.encode('utf-8')) > 20000:
                 #self.logger.warning("Text exceeds 20,000 byte limit for Comprehend Medical. Truncating.")
                 # A simple truncation strategy:
                 text = text.encode('utf-8')[:20000].decode('utf-8', 'ignore')

            """   self.logger.info(
                "Sending text to Comprehend Medical for entity detection.",
                extra={"text_length": len(text)}
            ) """

            # We use detect_entities_v2 as it is the latest and most capable version.
            response = self.client.infer_icd10_cm(
                Text=text
            )
            
            entities = response.get("Entities", [])
            """  self.logger.info(
                "Successfully detected medical entities.",
                extra={"entity_count": len(entities)}
            ) """
            
            # The request asks for the JSON entities object, which is this list.
            return entities

        except ClientError as e:
            error_code = e.response.get("Error", {}).get("Code")
            """  self.logger.error(
                "AWS Comprehend Medical API call failed.",
                extra={
                    "error_message": str(e),
                    "aws_error_code": error_code
                }
            ) """
            # Re-raise the exception so the calling function can handle it.
            raise