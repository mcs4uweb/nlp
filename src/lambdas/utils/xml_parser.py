import xml.etree.ElementTree as ET
import re
from datetime import datetime
from typing import Dict, Any, Optional

class XmlParserUtil:
    """
    A utility class to parse a specific Cerner-format XML report into a structured
    PatientVisitNote dictionary. It handles the XML namespace and extracts key
    metadata and content.
    """

    def __init__(self, xml_string: str):
        """
        Initializes the parser with the XML string.

        Args:
            xml_string (str): The raw XML content to be parsed.
        """
        # Ensure XML starts at the first character (strip BOM/whitespace)
        xml_string = xml_string.lstrip('\ufeff\r\n\t ')
        self.root = ET.fromstring(xml_string)
        # The namespace is defined in the root element. We must use it to find any tags.
        self.ns = {'cerner': 'urn:com-cerner-patient-ehr:v3'}

    def parse_to_visit_notes(self) -> Dict[str, Any]:
        """
        Orchestrates the parsing of the XML into a structured PatientVisitNote dictionary.

        Returns:
            A dictionary containing the extracted and formatted patient visit information.
        """
        doc_element = self.root.find('.//cerner:document', self.ns)
        personnel_list_element = self.root.find('.//cerner:personnel-list', self.ns)
        
        if doc_element is None:
            raise ValueError("Could not find the main <document> element in the XML.")

        provider_info = self._extract_provider_info(doc_element, personnel_list_element)
        blob_content = self._extract_blob_content(doc_element)

        visit_note = {
            "document_title": doc_element.get("title"),
            "document_type": self._find_text(doc_element, './/cerner:event-type', 'event-display'),
            "encounter_id": doc_element.get("encounter-id"),
            "documentation_datetime": self._format_datetime(doc_element.get("documentation-dt-tm")),
            "provider_info": provider_info,
            "embedded_document": blob_content
        }
        return visit_note

    def _extract_provider_info(self, doc_element: ET.Element, personnel_list: Optional[ET.Element]) -> Dict[str, Any]:
        """Extracts information about the participating provider."""
        if personnel_list is None:
            return {"error": "Personnel list not found."}

        # Find the main personnel ID from the document's participation section
        participation = doc_element.find('.//cerner:participation', self.ns)
        if participation is None:
            return {"error": "Participation element not found."}
        
        personnel_id = participation.get("participating-personnel")

        # Now, find the matching personnel in the personnel-list
        provider_xpath = f".//cerner:personnel[@prsnl-id='{personnel_id}']"
        personnel_element = personnel_list.find(provider_xpath, self.ns)

        if personnel_element is None:
            return {"error": f"Personnel with ID {personnel_id} not found in list."}

        # Extract NPI and EDIPI using their alias type codes
        npi_alias = personnel_element.find(".//cerner:personnel-alias[@personnelAliasTypeCode='4038127']", self.ns)
        edipi_alias = personnel_element.find(".//cerner:personnel-alias[@personnelAliasTypeCode='1086']", self.ns)

        return {
            "full_name": self._find_text(personnel_element, './/cerner:provider-name', 'name-full'),
            "personnel_id": personnel_id,
            "npi": npi_alias.text if npi_alias is not None else None,
            "edipi": edipi_alias.text if edipi_alias is not None else None
        }

    def _extract_blob_content(self, doc_element: ET.Element) -> Dict[str, Any]:
        """Extracts the Base64 encoded document and its metadata."""
        blob_element = doc_element.find('.//cerner:blob-content', self.ns)
        if blob_element is None:
            return {"error": "Blob content not found."}

        # NOTE: The provided XML sample has an empty <blob-content> tag.
        # In a real-world scenario, the Base64 string would be the .text of this element.
        base64_data = blob_element.text.strip() if blob_element.text else None

        return {
            "media_type": blob_element.get("media-type"),
            "format": blob_element.get("format"),
            "pages": blob_element.get("number-of-pages"),
            "base64_content": base64_data # This will be None for the sample XML
        }

    def _find_text(self, parent_element: ET.Element, xpath: str, attribute: str) -> Optional[str]:
        """Helper to safely find an element and get an attribute's text."""
        element = parent_element.find(xpath, self.ns)
        return element.get(attribute) if element is not None else None

    def _format_datetime(self, iso_string: Optional[str]) -> Optional[str]:
        """Helper to parse an ISO 8601 datetime string into a more readable format."""
        if not iso_string:
            return None
        try:
            # datetime.fromisoformat can handle the timezone offset
            dt_object = datetime.fromisoformat(iso_string)
            return dt_object.strftime('%Y-%m-%d %H:%M:%S %Z')
        except (ValueError, TypeError):
            return iso_string # Return original if parsing fails

# --- Example Usage for Testing ---
if __name__ == '__main__':
    import json
    from constants.xml_constants import XmlConstants

    print("--- Testing XML Parser Utility ---")
    
    # Get the sample XML from your constants file
    sample_xml = XmlConstants.THORACIC_TEST_REPORT_XML
    
    try:
        # 1. Instantiate the parser
        parser = XmlParserUtil(sample_xml)
        
        # 2. Call the main parsing method
        visit_notes = parser.parse_to_visit_notes()
        
        # 3. Print the structured output
        print("\nSuccessfully Parsed Patient Visit Note:")
        print(json.dumps(visit_notes, indent=2))

    except Exception as e:
        print(f"\nAn error occurred during parsing: {e}")

class CDAParserUtil:
    """
    A utility class to parse a standard HL7 CDA XML document into readable,
    structured clinical notes. It handles the complex HL7 namespace and extracts
    key sections and demographic information.
    """

    def __init__(self, xml_string: str):
        """
        Initializes the parser with the CDA XML string.

        Args:
            xml_string (str): The raw XML content of the CDA document.
        """
        # Remove default namespace definition for easier parsing with findall
        xml_string = re.sub(r'\sxmlns="[^"]+"', '', xml_string, count=1)
        self.root = ET.fromstring(xml_string)
        # Define the namespace map for HL7 v3, which is still needed for some attributes
        self.ns = {'hl7': 'urn:hl7-org:v3'}

    def parse_to_summary_note(self) -> Dict[str, Any]:
        """
        Orchestrates the parsing of the CDA XML into a structured summary note.

        Returns:
            A dictionary containing demographics and the text content of key clinical sections.
        """
        patient_info = self._parse_patient_demographics()
        
        # Extract the human-readable text from the most important sections
        note_text = {
            "problem_list": self._extract_section_text_by_title("Problem List"),
            "allergies": self._extract_section_text_by_title("Allergies, Adverse Reactions, Alerts"),
            "medications": self._extract_section_text_by_title("Medications"),
            "encounters": self._extract_section_text_by_title("Encounter(s)"),
            "assessment_and_plan": self._extract_section_text_by_title("Assessment and Plan"),
            "results": self._extract_section_text_by_title("Results")
        }

        return {
            "patient_demographics": patient_info,
            "clinical_notes": note_text
        }
        
    def _parse_patient_demographics(self) -> Dict[str, Any]:
        """Extracts key patient demographic information."""
        patient_role = self.root.find('.//patientRole')
        if patient_role is None:
            return {"error": "Patient role section not found."}

        # Safe extraction helpers
        def _find_text(element, path):
            node = element.find(path)
            return node.text.strip() if node is not None and node.text else None

        def _find_attribute(element, path, attribute):
            node = element.find(path)
            return node.get(attribute) if node is not None else None

        return {
            "first_name": _find_text(patient_role, './/given'),
            "last_name": _find_text(patient_role, './/family'),
            "gender": _find_attribute(patient_role, './/administrativeGenderCode', 'displayName'),
            "date_of_birth": self._format_cda_datetime(_find_attribute(patient_role, './/birthTime', 'value')),
            "ssn": _find_attribute(patient_role, ".//id[@assigningAuthorityName='SSN']", 'extension'),
            "dod_id": _find_attribute(patient_role, ".//id[@assigningAuthorityName='Person DoD ID']", 'extension')
        }

    def _find_section_by_title(self, title_text: str) -> Optional[ET.Element]:
        """Finds a <section> element based on the text of its <title> child."""
        # This XPath finds a section that has a title element with the exact text
        sections = self.root.findall(".//section")
        for section in sections:
            title_element = section.find('title')
            if title_element is not None and title_element.text == title_text:
                return section
        return None

    def _extract_section_text_by_title(self, title: str) -> Optional[str]:
        """
        Finds a section by its title and extracts all human-readable text from it,
        stripping out all XML/HTML tags.
        """
        section = self._find_section_by_title(title)
        if section is None:
            return f"Section '{title}' not found."

        text_element = section.find('text')
        if text_element is None:
            return f"No <text> block found in section '{title}'."

        # This powerful method gets all text from an element and its children
        full_text = ''.join(text_element.itertext())
        
        # Clean up whitespace and extra newlines for readability
        cleaned_text = re.sub(r'\s+', ' ', full_text).strip()
        return cleaned_text

    def _format_cda_datetime(self, cda_date: Optional[str]) -> Optional[str]:
        """Formats various CDA date/datetime strings into a standard format."""
        if not cda_date:
            return None
        try:
            # Handle YYYYMMDD format
            if len(cda_date) == 8:
                return datetime.strptime(cda_date, '%Y%m%d').strftime('%Y-%m-%d')
            # Handle YYYYMMDDHHMMSS... format
            if len(cda_date) > 8:
                # Truncate to the first 14 digits (YYYYMMDDHHMMSS) for simplicity
                return datetime.strptime(cda_date[:14], '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            return cda_date # Return original if parsing fails
        return cda_date

# --- Example Usage for Testing ---
if __name__ == '__main__':
    import json
    from constants.xml2 import XmlConstants

    print("\n--- Testing CDA Parser Utility ---")
    
    cda_xml = XmlConstants.TEST_REPORT_XML
    
    try:
        # 1. Instantiate the new parser
        cda_parser = CDAParserUtil(cda_xml)
        
        # 2. Call the main parsing method
        summary_notes = cda_parser.parse_to_summary_note()
        
        # 3. Print the readable output
        print("\nSuccessfully Parsed CDA to Readable Notes:")
        print(json.dumps(summary_notes, indent=2))
        
    except Exception as e:
        print(f"\nAn error occurred during CDA parsing: {e}")
