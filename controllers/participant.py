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
    # first we filter the participants using the filter_function
    # the filter_function returns a list of participants
    # and we get the length of the list
    return len(list(filter(filter_function, participants)))


def list_participants(participants: list[Participant]) -> list:
    """
    This function lists the participants.

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: The list of participants.
    """
    # create a list with the titles
    participants_list = [
        titles,
    ]
    participants_list.extend(
        [
            # cast the participant object to a list
            # **note**: in the `models/participant.py` file had been defined it     # noqa E501
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
    # set the titles
    participants_list = [
        [
            "Grupo",
            "Total"
        ]
    ]
    for etarian_group in etarian_groups:
        participants_list.append(
            [
                etarian_group,  # the etarian group (name)
                # call the total_participants function and pass the filter function  # noqa E501
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
    # set the titles
    participants_list = [
        [
            "Género",
            "Total"
        ]
    ]
    genders = {
        'M': 'Masculino',
        'F': 'Femenino'
    }
    # iterate in the genders (M,F)
    for key, value in genders.items():
        participants_list.append(
            [
                value,     # gender name
                # call the total_participants function and pass the filter function  # noqa E501
                total_participants(
                    participants,
                    lambda participant: participant.gender == key  # noqa E501
                ),
            ]
        )
    return participants_list


def winners_by_filter(
        participants: list[Participant],
        categories: list,
        titles_list: list = [""]
) -> list:
    """
    This function returns the winners by specific categories

    Params:
        participants (list[Participant]): The list of participants.
        categories (list): The list of categories.
        titles_list (list): The list of titles.

    Returns:
        list: Matrix with the winners by specific categories.
    """
    # set the titles
    titles_list = titles_list + titles
    participants_list = [titles_list]

    # iterate over the list of tuples (category, filter_function)
    for category, filter_function in categories:
        # filter the participants using the filter_function
        if isinstance(category, str):
            category = [category]
        filtered_list = list(
            filter(
                filter_function,
                participants
            )
        )
        # if length of the filtered list is zero, we skip the iteration
        if len(filtered_list) == 0:
            participants_list.append(
                [
                    *category,
                    *["" for _ in range(len(titles))]
                ]
            )
            continue
        # get the min time of the filtered list by the total seconds
        winner = min(
            filtered_list,
            key=lambda participant: participant.total_time
        )
        # add the winner to the list
        participants_list.append(
            [
                *category,
                *list(winner)   # cast the participant object to a list and also deserialize the object  # noqa E501
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
    # call winners function
    return winners_by_filter(
        participants,
        [   # set the categories and the filter functions
            ("Juniors", lambda participant: participant.etarian_group == "Juniors"),  # noqa E501
            ("Seniors", lambda participant: participant.etarian_group == "Seniors"),  # noqa E501
            ("Masters", lambda participant: participant.etarian_group == "Masters"),  # noqa E501
        ],
        ["Grupo Etario"]
    )


def winners_by_gender(participants: list[Participant]) -> list:
    """
    This function returns the winers by gender

    Params:
        participants (list[Participant]): The list of participants.

    Returns:
        list: Matrix with the winners by gender
    """
    # call winners function
    return winners_by_filter(
        participants,
        [   # set the genders and the filter functions
            ("Masculino", lambda participant: participant.gender == "M"),
            ("Femenino", lambda participant: participant.gender == "F")
        ],
        ["Genero"]
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
            (["Juniors", "Masculino"], lambda participant: participant.etarian_group == "Juniors" and participant.gender == "M"),  # noqa E501
            (["Juniors", "Femenino"], lambda participant: participant.etarian_group == "Juniors" and participant.gender == "F"),  # noqa E501
            (["Seniors", "Masculino"], lambda participant: participant.etarian_group == "Seniors" and participant.gender == "M"),  # noqa E501
            (["Seniors", "Femenino"], lambda participant: participant.etarian_group == "Seniors" and participant.gender == "F"),  # noqa E501
            (["Masters", "Masculino"], lambda participant: participant.etarian_group == "Masters" and participant.gender == "M"),  # noqa E501
            (["Masters", "Femenino"], lambda participant: participant.etarian_group == "Masters" and participant.gender == "F"),  # noqa E501
        ],
        [
            "Grupo Etario",
            "Género"
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
    # call winners function
    return winners_by_filter(
        participants,
        [
            # pass dummy category and filter function to get all
            ("", lambda participant: True)
        ]
    )


def average_by_filter(
    participants: list[Participant],
    categories: list,
    titles: list
) -> list:
    """
    This function returns the average by specific categories

    Params:
        participants (list[Participant]): The list of participants.
        categories (list): The list of categories.
        titles (list): The list of titles.

    Returns:
        list: Matrix with the average by specific categories.
    """
    # defines the titles of the matrix
    average_list_titles = ["Promedio (Horas)"]
    titles_list = titles + average_list_titles
    participants_list = [titles_list]
    # iterate over the list of tuples (category, filter_function)
    for category, filter_function in categories:
        # filter the participants by the filter function
        if isinstance(category, str):
            category = [category]
        filtered_list = list(
            filter(
                filter_function,
                participants
            )
        )
        # if there are no participants, add an empty row
        if len(filtered_list) == 0:
            participants_list.append(
                [
                    *category,
                    *["" for _ in range(len(average_list_titles))]
                ]
            )
            continue
        # calculate the average (in seconds) of the filtered list
        average = sum(
            [
                participant.total_time for participant in filtered_list
            ]
        ) / len(filtered_list)
        # convert the average to format hh:mm:ss
        minutes, seconds = divmod(int(average), 60)
        hours, minutes = divmod(minutes, 60)
        # add the average to the list
        participants_list.append(
            [
                *category,
                "{}:{}:{}".format(
                    hours,
                    minutes,
                    seconds
                )
            ]
        )
    # return the list
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
        ],
        ["Grupo Etario"]
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
        ["Sexo"]
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
            (["Juniors", "Masculino"], lambda participant: participant.etarian_group == "Juniors" and participant.gender == "M"),  # noqa E501
            (["Juniors", "Femenino"], lambda participant: participant.etarian_group == "Juniors" and participant.gender == "F"),  # noqa E501
            (["Seniors", "Masculino"], lambda participant: participant.etarian_group == "Seniors" and participant.gender == "M"),  # noqa E501
            (["Seniors", "Femenino"], lambda participant: participant.etarian_group == "Seniors" and participant.gender == "F"),  # noqa E501
            (["Masters", "Masculino"], lambda participant: participant.etarian_group == "Masters" and participant.gender == "M"),  # noqa E501
            (["Masters", "Femenino"], lambda participant: participant.etarian_group == "Masters" and participant.gender == "F"),  # noqa E501
        ],
        [
            "Grupo Etario",
            "Género"
        ]
    )
