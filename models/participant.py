import datetime
from typing import Union


class Participant():
    """
    Participant class for the mapping from the Text Plain
    File to the object
    """

    def __init__(
        self,
        ci: Union[str, int],
        first_last_name: str,
        second_last_name: str,
        first_name: str,
        first_char_second_name: str,
        gender: str,
        age: Union[str, int],
        hours: Union[str, int],
        minutes: Union[str, int],
        seconds: Union[str, int],
    ) -> None:
        """
        Constructor

        Set the initial values of the Participant model

        Params:
            ci (Union[str, int]): CI of the participant
            first_last_name (str): First Last Name of the participant
            second_last_name (str): Second Last Name of the participant
            first_name (str): First Name of the participant
            first_char_second_name (str): First Character of the Second Name
            gender (Union[str, int]): The gender of the participant
            age (Union[str, int]): The age of the partipant
            hours (Union[str, int]): The hours part of the participant running time
            minutes (Union[str, int]): The minutes part of the participant running time
            seconds (Union[str, int]): The seconds part of the participant running time

        Returns:
            None
        """  # noqa: E501

        self.ci = ci
        self.first_last_name = first_last_name
        self.second_last_name = second_last_name
        self.first_name = first_name
        self.first_char_second_name = first_char_second_name
        self.gender = gender.upper()
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
        self.time = datetime.time(
            hour=self.hours,
            minute=self.minutes,
            second=self.seconds
        )

    def __str__(self) -> str:
        """String representation of the Participant object"""
        return f"{self.first_name} {self.first_last_name}"

    def __iter__(self):
        """Iterator for the Participant object"""
        return iter(
            [
                self.ci,
                self.first_last_name,
                self.second_last_name,
                self.first_name,
                self.first_char_second_name,
                self.gender,
                str(self.age),
                str(self.hours),
                str(self.minutes),
                str(self.seconds)
            ]
        )
