class AppConfig:
    
    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated.")

    # Using triple quotes allows for a clean, multi-line string definition.
    # The variable is named in UPPERCASE_SNAKE_CASE, the Python convention for constants.
    schemaName: str = "mirs"
    mirsProcessedNotes: str = "ProcessedNotes"
    mirsPerson: str = "Person"
    mirsPersonMedicalDocument: str = "PersonMedicalDocument"