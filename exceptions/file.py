class NotTextPlainFile(Exception):
    """
    Raised when a file is not a text plain file.
    """

    def __init__(self, filename: str) -> None:
        """
        Constructor.

        Params:
            filename (str): The name of the file.
        """
        self.filename = filename
        super().__init__(
            f"El archivo '{filename}' no es un archivo texto plano."
        )
