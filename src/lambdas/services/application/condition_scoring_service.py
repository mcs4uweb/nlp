from typing import List, Dict, Any

class ConditionScoringService:
    """
    Analyzes lists of medical entities and ICD-10 codes to generate a health score.
    A higher score indicates a greater number and severity of adverse conditions.
    """

    # --- Scoring Configuration ---
    # These can be expanded or loaded from a config file in a real application.
    CATEGORY_SCORES = {
        "MEDICAL_CONDITION": 5,
        "TEST_TREATMENT_PROCEDURE": 2,
        "MEDICATION": 1
    }
    
    # Scores for specific, high-severity ICD-10 codes.
    ICD10_HIGH_SEVERITY_SCORES = {
        "I21": 25,  # Acute Myocardial Infarction (Heart Attack)
        "C50": 20,  # Malignant neoplasm of breast (Cancer)
        "J44": 15   # Chronic obstructive pulmonary disease (COPD)
    }
    
    # Default score for any other detected ICD-10 diagnosis.
    ICD10_DEFAULT_SCORE = 10

    def score_from_entities(self, entities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculates a score based on a list of general medical entities.

        Args:
            entities: The list of entities from Comprehend Medical's detect_entities_v2.

        Returns:
            A dictionary containing the score, contributing conditions, and negated conditions.
        """
        score = 0
        contributing_conditions = []
        negated_conditions = []

        for entity in entities:
            # Check for the NEGATION trait. If present, this condition doesn't add to the score.
            is_negated = any(trait['Name'] == 'NEGATION' for trait in entity.get('Traits', []))
            
            if is_negated:
                negated_conditions.append({
                    "text": entity['Text'],
                    "category": entity['Category']
                })
                continue # Skip to the next entity

            # Add points based on the entity's category if it's a condition of interest.
            category = entity['Category']
            points = self.CATEGORY_SCORES.get(category, 0)
            
            if points > 0:
                score += points
                contributing_conditions.append({
                    "text": entity['Text'],
                    "category": category,
                    "score": points
                })
        
        return {
            "score": score,
            "contributing_conditions": contributing_conditions,
            "negated_conditions": negated_conditions
        }

    def score_from_icd10(self, icd10_entities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculates a score based on a list of detected ICD-10-CM concepts.

        Args:
            icd10_entities: The list of entities from Comprehend Medical's infer_icd10_cm.

        Returns:
            A dictionary containing the score and a list of contributing diagnoses.
        """
        score = 0
        contributing_diagnoses = []
        
        for entity in icd10_entities:
            # --- FIX STARTS HERE ---
            
            # 1. Safely get the list of concepts, defaulting to an empty list.
            concepts_list = entity.get('ICD10CMConcepts', [])
            
            # 2. Check if the list is empty. If so, skip to the next entity.
            if not concepts_list:
                continue

            # 3. Now it's safe to access the first element.
            concept = concepts_list[0]
            
            # --- FIX ENDS HERE ---
            
            code = concept.get('Code')
            
            if not code:
                continue

            # Assign points based on severity map, or use default.
            code_prefix = code.split('.')[0]
            points = self.ICD10_HIGH_SEVERITY_SCORES.get(code_prefix, self.ICD10_DEFAULT_SCORE)
            
            score += points
            contributing_diagnoses.append({
                "text": entity['Text'],
                "icd10_code": code,
                "description": concept.get('Description'),
                "score": points
            })
            
        return {
            "score": score,
            "contributing_diagnoses": contributing_diagnoses
        }