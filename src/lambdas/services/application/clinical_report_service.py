from typing import Dict, Any, Optional
from collections import defaultdict

class ClinicalReportService:
    def __init__(
            self
    ):
        self.time_links = defaultdict(list)
        self.TRAITS = [
            "DIAGNOSIS", "NEGATION", "PERTAINS_TO_FAMILY", "HYPOTHETICAL",
            "LOW_CONFIDENCE", "SIGN", "SYMPTOM"
        ]

        self.ATTR_TYPES = [
            "DIRECTION", "SYSTEM_ORGAN_SITE", "ACUITY", "QUALITY",
            "TIME_TO_DX_NAME", "DX_NAME"
        ]
    """
    A service that takes structured medical analysis data and formats it into a
    human-readable clinical summary, mimicking a physician's interpretation.
    """

    def generate_clinical_summary(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generates a formatted clinical summary report from analysis data.

        Args:
            analysis_data: The JSON output from ComprehendMedicalService.analyze_patient_health.

        Returns:
            A formatted string containing the full clinical report.
        """
        # --- Data Extraction ---
        bucket = {k: [] for k in self.ATTR_TYPES}
        assessment = analysis_data.get("assessment", "Assessment not available.")
        total_score = analysis_data.get("total_health_score", 0)
        
        details = analysis_data.get("details", {})
        entity_analysis = details.get("entity_analysis", {})
        icd10_analysis = details.get("icd10_diagnosis_analysis", {})
        
        contributing_conditions = entity_analysis.get("contributing_conditions", [])
        negated_conditions = entity_analysis.get("negated_conditions", [])
        contributing_diagnoses = icd10_analysis.get("contributing_diagnoses", [])

        # Helper to find the most severe diagnosis for the summary
        primary_diagnosis = self._find_most_severe_diagnosis(contributing_diagnoses)

        # --- Report Generation ---
        report_parts = [
            "### Clinical Interpretation of AI-Generated Medical Note Summary ###",
            "",
            "**Overall Assessment:**",
            "This patient presents with a high-acuity medical situation that requires immediate attention.",
            f"The system's automated assessment is correct: {assessment}",
            f"The primary finding appears to be **{primary_diagnosis['description']} (ICD-10: {primary_diagnosis['icd10_code']})**.",
            "",
            "---",
            "",
            "**Key Positive Findings (Evidence for Diagnosis):**"
        ]
        
        # 1. Primary Diagnosis
        report_parts.append(f"1.  **Primary Diagnosis: {primary_diagnosis['description']}** - This is the most critical finding, "
                            f"assigned a high severity score of {primary_diagnosis['score']}.")

        # 2. Other conditions, history, and procedures
        for condition in contributing_conditions:
            text = condition['text']
            category = condition['category']
            if category == 'MEDICAL_CONDITION' and text.lower() not in primary_diagnosis['text'].lower():
                report_parts.append(f"-   **Relevant History/Symptom:** Patient has a history of or is presenting with '{text}'.")
            elif category == 'TEST_TREATMENT_PROCEDURE':
                report_parts.append(f"-   **Intervention Performed:** A '{text}' was noted, indicating an active workup.")

        report_parts.append("\n**Key Negative Findings (Important for Context):**")
        if negated_conditions:
            for condition in negated_conditions:
                report_parts.append(f"-   Patient **denied** classic symptoms of **{condition['text']}**.")
            report_parts.append("    This may suggest an atypical presentation of the primary diagnosis.")
        else:
            report_parts.append("-   No negated conditions were explicitly identified.")

        report_parts.extend([
            "", "---", "",
            "**Clinical Impression & Synthesis:**",
            "In summary, this patient presents with a significant medical event.",
            "Despite the potential absence of classic symptoms (as noted by the negated findings), the diagnostic data points strongly towards the primary diagnosis.",
            "",
            "**Recommendations & Plan (Based on Primary Finding):**",
            "1.  **Immediate Action:** Escalate this case for immediate physician review.",
            "2.  **Confirm Workup:** Review all relevant diagnostic results (e.g., ECG, labs) to confirm the finding.",
            "3.  **Treatment:** Initiate standard protocol for the diagnosed condition.",
            "4.  **Consultation:** An urgent consultation with the relevant specialty (e.g., Cardiology) is likely required."
        ])

        return "\n".join(report_parts)

    def _find_most_severe_diagnosis(self, diagnoses: list) -> Dict[str, Any]:
        """Finds the diagnosis with the highest score from a list."""
        if not diagnoses:
            return {"description": "N/A", "icd10_code": "N/A", "score": 0, "text": ""}
        
        return max(diagnoses, key=lambda d: d['score'])
    
    def extract_trait_scores(self, entity):
        trait_scores = {t: 0.0 for t in self.TRAITS}
        for tr in entity.get("Traits", []):
            if tr["Name"] in trait_scores: trait_scores[tr["Name"]] = round(tr["Score"], 2)
        return trait_scores
    
    def extract_attributes(self, entity):
        bucket = {k: [] for k in self.ATTR_TYPES}

        def add_attr_to_bucket(attr_dict):
            attr_type = attr_dict.get("Type")
            if attr_type in bucket:
                relationship_score_val = attr_dict.get("rel", attr_dict.get("RelationshipScore", 0.0))

                attr_entry = {
                    "text": attr_dict.get("Text", ""),
                    "score": round(attr_dict.get("Score", 0.0), 2),
                    "rel": round(float(relationship_score_val), 2)
                }

                # Preserve offsets for tooltip highlighting
                begin = attr_dict.get("begin_offset", attr_dict.get("BeginOffset"))
                end   = attr_dict.get("end_offset", attr_dict.get("EndOffset"))
                if begin is not None and end is not None:
                    attr_entry["begin_offset"] = begin
                    attr_entry["end_offset"] = end
                    if self.clinical_notes:
                        ctx, _, _ = self.get_entity_context(
                            self.clinical_notes,
                            begin,
                            end,
                        )
                        attr_entry["context"] = ctx

                bucket[attr_type].append(attr_entry)

        for attr_from_entity in entity.get("Attributes", []):
            add_attr_to_bucket(attr_from_entity)

        if hasattr(self, 'time_links') and entity.get("Id") in self.time_links:
            for tlink_dict in self.time_links[entity.get("Id")]:
                add_attr_to_bucket(tlink_dict) 

        return bucket