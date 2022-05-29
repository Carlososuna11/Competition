
class Participant():
    """
    Participant class for the mapping from the Text Plain
    File to the object
    """

    def __init__(
        self,
        ci: int,
        first_last_name: str,
        second_last_name: str,
        first_name: str,
        first_char_second_name: str,
        gender: str,
        age: int,
        hours: int,
        minutes: int,
        seconds: int,
    ) -> None:
        self.ci = ci
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.first_name = first_name
        self.first_char_second_name = first_char_second_name
        self.gender = gender
        self.age = age
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self) -> str:
        return f"{self.first_name} {self.first_last_name}"
