
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
        self.age = int(age)
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        if self.age <= 25:
            self.etarian_group = "Juniors"
        if 25 < self.age <= 40:
            self.etarian_group = "Seniors"
        if self.age > 40:
            self.etarian_group = "Masters"
        self.total_time = self.seconds
        self.total_time += self.minutes * 60
        self.total_time += self.hours * 3600

    def __str__(self) -> str:
        return f"{self.first_name} {self.first_last_name}"

    def __iter__(self):
        return iter(
            [
                self.ci,
                self.first_last_name,
                self.second_last_name,
                self.first_name,
                self.first_char_second_name,
                self.gender,
                self.age,
                self.hours,
                self.minutes,
                self.seconds
            ]
        )
