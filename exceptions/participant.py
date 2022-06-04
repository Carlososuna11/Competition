class IncompleteParticipantData(Exception):
    """
    Raised when a participant has not complete data
    """

    def __init__(
        self,
        position: int,
        actual_length: int,
        needed_length: int
    ) -> None:
        """
        Constructor.

        Params:
            position (int): The position of the malformed data on the file
            actual_length (int): The actual length of de suministred data
            needed_length (int): The needed length of the data
        """
        self.actual_length = actual_length
        self.needed_length = needed_length
        self.position = position
        super().__init__(
            f"La data suministrada en la línea {self.position}"
            + " está mal formada, solo se suministraron"
            + f" {self.actual_length} datos, son requeridos"
            + f" {self.needed_length}"
        )
