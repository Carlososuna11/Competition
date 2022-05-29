from models.participant import Participant

titles = [
    "CI",
    "1er Apellido",
    "2do Apellido",
    "Nombre",
    "Inicial 2do Nombre",
    "Sexo",
    "Edad",
    "Horas",
    "Minutos",
    "Segundos",
]
etarian_groups = [
    "Juniors",
    "Seniors",
    "Masters",
]


def total_participants(
        participants: list[Participant],
        filter_function: callable
) -> int:
    """
    This function calculates the total of participants.

    Params:
        participants (list[Participant]): The list of participants.
        filter_function (callable): The filter function.

    Returns:
        int: The total of participants.
    """
    return len(list(filter(filter_function, participants)))


def list_participants(participants: list[Participant]) -> list:
    """
    This function lists the participants.

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: The list of participants.
    """
    participants_list = [
        titles,
    ]
    participants_list.extend(
        [
            list(participant) for participant in participants
        ]
    )
    return participants_list


def etarian_participants(participants: list[Participant]) -> list:
    """
    This function counts the participants by etarian group.

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the count of participants by etarian group.
    """
    participants_list = [
        [
            "Grupo",
            "Total"
        ]
    ]
    for etarian_group in etarian_groups:
        participants_list.append(
            [
                etarian_group,
                total_participants(
                    participants,
                    lambda participant: participant.etarian_group == etarian_group  # noqa E501
                ),
            ]
        )
    return participants_list


def gender_participants(participants: list[Participant]) -> list:
    """
    This function counts the participants by gender.

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the count of participants by gender.
    """
    participants_list = [
        [
            "Género",
            "Total"
        ]
    ]
    for gender in ["M", "F"]:
        participants_list.append(
            [
                gender,
                total_participants(
                    participants,
                    lambda participant: participant.gender == gender  # noqa E501
                ),
            ]
        )
    return participants_list


def winners_by_filter(
        participants: list[Participant],
        categories: list
) -> list:
    """
    This function returns the winners by specific categories

    Params:
        participants (list[Participant]): The list of participants.
        categories (list): The list of categories.

    Returns:
        list: Matrix with the winners by specific categories.
    """
    titles_list = [""] + titles
    participants_list = [titles_list]
    for category, filter_function in categories:
        filtered_list = list(
            filter(
                filter_function,
                participants
            )
        )
        if len(filtered_list) == 0:
            participants_list.append(
                [
                    category,
                    *["" for _ in range(len(titles))]
                ]
            )
            continue
        winner = min(
            filtered_list,
            key=lambda participant: participant.total_time
        )
        participants_list.append(
            [
                category,
                *list(winner)
            ]
        )
    return participants_list


def winners_by_etarian_group(participants: list[Participant]) -> list:
    """
    This function returns the winners by etarian group

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the winners by etarian group.
    """
    return winners_by_filter(
        participants,
        [
            ("Juniors", lambda participant: participant.etarian_group == "Juniors"),  # noqa E501
            ("Seniors", lambda participant: participant.etarian_group == "Seniors"),  # noqa E501
            ("Masters", lambda participant: participant.etarian_group == "Masters"),  # noqa E501
        ]
    )


def winners_by_gender(participants: list[Participant]) -> list:
    """
    This function returns the winers by gender

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the winners by gender
    """
    return winners_by_filter(
        participants,
        [
            ("M", lambda participant: participant.gender == "M"),
            ("F", lambda participant: participant.gender == "F")
        ]
    )


def winners_by_gender_and_etarian_group(
        participants: list[Participant]
) -> list:
    """
    This function returns the winners by gender and etarian group

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the winners by gender and etarian group
    """
    return winners_by_filter(
        participants,
        [
            ("Juniors", lambda participant: participant.etarian_group == "Juniors"),  # noqa E501
            ("Seniors", lambda participant: participant.etarian_group == "Seniors"),  # noqa E501
            ("Masters", lambda participant: participant.etarian_group == "Masters"),  # noqa E501
            ("M", lambda participant: participant.gender == "M"),
            ("F", lambda participant: participant.gender == "F")
        ]
    )


def general_winner(participants: list[Participant]) -> list:
    """
    This function return the winner without filtering

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the winner
    """
    return winners_by_filter(
        participants,
        [
            ("", lambda participant: True)
        ]
    )


def average_by_filter(
    participants: list[Participant],
    categories: list
) -> list:
    """
    This function returns the average by specific categories

    Params:
        participants (list[Participant]): The list of participants.
        categories (list): The list of categories.

    Returns:
        list: Matrix with the average by specific categories.
    """
    average_list_titles = ["Promedio (Horas)"]
    titles_list = [""] + average_list_titles
    participants_list = [titles_list]
    for category, filter_function in categories:
        filtered_list = list(
            filter(
                filter_function,
                participants
            )
        )
        if len(filtered_list) == 0:
            participants_list.append(
                [
                    category,
                    *["" for _ in range(len(average_list_titles))]
                ]
            )
            continue
        average = sum(
            [
                participant.total_time for participant in filtered_list
            ]
        ) / len(filtered_list)
        participants_list.append(
            [
                category,
                f"{average/3600:.2f}",
            ]
        )
    return participants_list


def average_by_etarian_group(participants: list[Participant]) -> list:
    """
    This function returns the average by etarian group

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the average by etarian group.
    """
    return average_by_filter(
        participants,
        [
            ("Juniors", lambda participant: participant.etarian_group == "Juniors"),  # noqa E501
            ("Seniors", lambda participant: participant.etarian_group == "Seniors"),  # noqa E501
            ("Masters", lambda participant: participant.etarian_group == "Masters"),  # noqa E501
        ]
    )


def average_by_gender(participants: list[Participant]) -> list:
    """
    This function returns the average by gender

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the average by gender
    """
    return average_by_filter(
        participants,
        [
            ("M", lambda participant: participant.gender == "M"),
            ("F", lambda participant: participant.gender == "F")
        ]
    )


def average_by_gender_and_etarian_group(
        participants: list[Participant]) -> list:
    """
    This function returns the averages by gender and etarian group

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the averages by gender and etarian group
    """
    return average_by_filter(
        participants,
        [
            ("Juniors", lambda participant: participant.etarian_group == "Juniors"),  # noqa E501
            ("Seniors", lambda participant: participant.etarian_group == "Seniors"),  # noqa E501
            ("Masters", lambda participant: participant.etarian_group == "Masters"),  # noqa E501
            ("M", lambda participant: participant.gender == "M"),
            ("F", lambda participant: participant.gender == "F")
        ]
    )
