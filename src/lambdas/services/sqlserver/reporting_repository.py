from typing import List, Dict, Any

from .database_connection_service import DatabaseConnectionService

class ReportingRepository:
    """
    A repository for handling complex, read-only queries, often involving joins.
    This separates complex query logic from simple single-table CRUD operations.
    """

    def __init__(self, db_service: DatabaseConnectionService):
        """
        Initializes the repository.

        Args:
            db_service (DatabaseConnectionService): The service used to get database connections.
        """
        self._db_service = db_service

    def get_Notes_on_Patients(self) -> List[Dict[str, Any]]:
        """
         

        Returns:
            A list of dictionaries, where each dictionary represents patient notes.
        """
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor(as_dict=True)
            
            # Sample complex query joining ClinicalNotes and ProcessedMedicalEntities tables.
            # Subject to change based on actual requirements.
            query = """
                SELECT 
                    cn.[NoteID],
                    cn.[EncounterID],
                    cn.[PatientID],
                    cn.[NoteType],
                    cn.[NoteText],
                    cn.[CreateDate],
                    cn.[LastUpdateDate],
                    pme.[InferenceEngine],
                    pme.[PerClinicalNoteID],
                    pme.[Item_Category],
                    pme.[Id],
                    pme.[ICD10_Code],
                    pme.[ICD10_Description],
                    pme.[ICD10_Score],
                    pme.[Entity_Text],
                    pme.[Entity_Category],
                    pme.[Entity_Type],
                    pme.[Entity_Score],
                    pme.[Entity_BeginOffset],
                    pme.[Entity_EndOffset],
                    pme.[Attribute_Text],
                    pme.[Attribute_Type],
                    pme.[Attribute_Score],
                    pme.[Attribute_RelationshipScore],
                    pme.[Attribute_BeginOffset],
                    pme.[Attribute_EndOffset],
                    pme.[RxNorm_Code],
                    pme.[RxNorm_Description],
                    pme.[RxNorm_Score],
                    pme.[SNOMED_Code],
                    pme.[SNOMED_Description],
                    pme.[SNOMED_Score],
                    pme.[Trait_Name],
                    pme.[Trait_Score],
                    pme.[ModelVersion],
                    pme.[Timestamp],
                    pme.[Attribute_Traits],
                    pme.[Entity_Attributes],
                    pme.[Entity_Traits],
                    pme.[Entity_ICD10CMConcepts],
                    pme.[SNOMED_Edition],
                    pme.[SNOMED_VersionDate],
                    pme.[SNOMED_Language],
                    pme.[InferenceProvider],
                    pme.[Temporal_Expression],
                    pme.[Temporal_Type],
                    pme.[Temporal_Score],
                    pme.[Temporal_BeginOffset],
                    pme.[Temporal_EndOffset],
                    pme.[Temporal_RelationshipScore],
                    pme.[Entity_Id],
                    pme.[Attribute_Id],
                    pme.[Entity_Context],
                    pme.[Entity_ContextBeginOffset],
                    pme.[Entity_ContextEndOffset],
                    pme.[Body_Section]
                FROM [JCABAN].[adb].[ClinicalNotes] cn
                INNER JOIN [JCABAN].[adb].[ProcessedMedicalEntities] pme
                    ON cn.[NoteID] = pme.[PerClinicalNoteID];
            """
            
            cursor.execute(query)
            return cursor.fetchall()
        
    def get_Patients_FileName(self) -> List[Dict[str, Any]]:
        with self._db_service.get_connection() as conn:
            cursor = conn.cursor(as_dict=True)
            
            # Sample complex query joining ClinicalNotes and ProcessedMedicalEntities tables.
            # Subject to change based on actual requirements.
            query = """
                SELECT 
                    pmd.PersonMedicalDocumentID,
                    p.FirstName, 
                    p.LastName, 
                    pmd.FilePath,  
                    REVERSE(SUBSTRING(REVERSE(pmd.FilePath), 1, CHARINDEX('/', REVERSE(pmd.FilePath)) - 1)) AS FileName
                FROM 
                    mirs.Person AS p  
                JOIN 
                    mirs.PersonMedicalDocument AS pmd  
                    ON p.PersonID = pmd.PersonID
                WHERE 
                    pmd.DocumentResultStatusID = 1 and pmd.FilePath IS NOT NULL 
            """
            
            cursor.execute(query)
            return cursor.fetchall()
            