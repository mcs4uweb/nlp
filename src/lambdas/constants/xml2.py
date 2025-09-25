class XmlConstants:
    """
    This class acts as a namespace for static XML templates and constants.
    It is not meant to be instantiated. Its attributes should be accessed directly
    via the class name (e.g., XmlConstants.THORACIC_TEST_REPORT_XML).
    """

    def __init__(self):
        """Prevents instantiation of this constants class."""
        raise NotImplementedError("This class is not meant to be instantiated.")

    # Using triple quotes allows for a clean, multi-line string definition.
    # The variable is named in UPPERCASE_SNAKE_CASE, the Python convention for constants.
   