from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options,
    print_table,
    one_line_view,
    historigram,
)
from controllers.participant import (
    list_participants,
    total_participants,
    etarian_participants,
    gender_participants,
    winners_by_etarian_group,
    winners_by_gender_and_etarian_group,
    winners_by_gender,
    general_winner,
    average_by_gender_and_etarian_group,
)


# first call the decorator and then will call the function
@loop_menu
def actions_menu(context: dict) -> dict:
    """
    This function generates the actions menu of the application.

    **Note**: It's necessary to pass inside the context parameter
    the `participants` list.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    # Verify if the context has the participants list
    flag = False
    if "file_path" not in context:
        flag = True
    if "participants" not in context:
        flag = True
    if flag:
        print("\n")
        print("Primero debes cargar el archivo para acceder")
        print("A estas funcionalidades")
        print("\n")
        input("Pulsa una tecla para continuar...")
        return {"return": True, **context}
    # Generate the menu options
    options = {
        "Cantidad total de participantes": count_participants_view,
        "Lista con la totalidad de los participantes": list_participants_view,
        "Cantidad de participantes por grupo etario": list_participants_by_etarian_group_view,  # noqa E501
        "Cantidad de participantes por sexo": list_participants_by_gender_view,  # noqa E501
        "Ganadores por grupo etario": list_winners_by_etarian_group_view,
        "Ganadores por sexo": list_winners_by_gender_view,
        "Ganadores por Grupo Etario y sexo": list_winners_by_gender_and_etarian_group_views,    # noqa E501
        "Ganador General": general_winner_view,
        "Historigrama de Participantes por grupo Etario": historigram_etarian_group_view,   # noqa E501
        "Promedio de Tiempo por grupo Etario y Sexo": list_average_by_gender_and_etarian_group_view,    # noqa E501
        "Volver": lambda context: {"return": True, **context},
        "Salir": call_exit,
    }
    # get the keys options
    option_keys = list(options.keys())
    # generate the menu options
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    # get the selected option
    method = options[options_dict[option]]
    # clear the screen
    clear_screen()
    # call the selected method
    return method(context)

# first call the decorator and then will call the function


@loop_menu
def list_participants_view(context):
    """
    This function prints the list of participants.

    Params:
        context (dict): The context of the application.
        participants (list[dict]): The list of participants.
    """

    participants = list_participants(context.get("participants", []))
    print("\n")
    print("Lista de participantes")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    # call the print_table function
    print_table(participants)
    print("\n")
    input("Pulsa una tecla para continuar...")
    # return the context
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def count_participants_view(context):
    """
    This function prints the total amount of participants.

    Params:
        context (dict): The context of the application.
        participants (list[dict]): The list of participants.
    """
    # get the total amount of participants
    count = total_participants(
        context.get("participants", []),
        lambda x: True
    )
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    # print the total amount of participants (one line view)
    one_line_view(
        [
            ["Cantidad total de participantes"],
            [str(count)],
        ]
    )
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def list_participants_by_etarian_group_view(context):
    """
    This function prints the list of participants by etarian group.

    Params:
        context (dict): The context of the application.
    """

    # get the list of participants by etarian group
    participants = etarian_participants(
        context.get("participants", [])
    )
    print("\n")
    print("Lista de participantes por Grupo Etario")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(participants)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def list_participants_by_gender_view(context):
    """
    This function prints the list of participants by gender.

    Params:
        context (dict): The context of the application.
    """
    # get the list of participants by gender
    participants = gender_participants(
        context.get("participants", [])
    )
    print("\n")
    print("Lista de participantes por Género")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    one_line_view(participants)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def list_winners_by_etarian_group_view(context):
    """
    This function prints the list of winners by etarian group.

    Params:
        context (dict): The context of the application.
    """
    # get the list of winners by etarian group
    winners = winners_by_etarian_group(
        context.get("participants", [])
    )
    print("\n")
    print("Lista de ganadores por Grupo Etario")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def list_winners_by_gender_view(context):
    """
    This function prints the list of winners by gender.

    Params:
        context (dict): The context of the application.
    """
    # get the list of winners by gender
    winners = winners_by_gender(
        context.get("participants", [])
    )
    print("\n")
    print("Lista de ganadores por Sexo")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


# first call the decorator and then will call the function
@loop_menu
def list_winners_by_gender_and_etarian_group_views(context):
    """
    This function prints the list of winners by etarian group and gender.

    Params:
        context (dict): The context of the application.
    """
    # get the list of winners by gender
    winners = winners_by_gender_and_etarian_group(
        context.get("participants", [])
    )
    print("\n")
    print("Lista de ganadores por Sexo y por Grupo Etario")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners, True)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}

# first call the decorator and then will call the function


@loop_menu
def general_winner_view(context):
    """
    This function prints the general winner.

    Params:
        context (dict): The context of the application.
    """
    # get the general winner
    winner = general_winner(
        context.get("participants", [])
    )
    print("\n")
    print("Ganador General")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    one_line_view(winner)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


@loop_menu
def historigram_etarian_group_view(context):
    """
    This function prints the historigram of etarian participants.

    Params:
        context (dict): The context of the application.
    """
    # get the count of participants by etarian group
    winner = etarian_participants(
        context.get("participants", [])
    )
    print("\n")
    print("Histograma por Grupo Etario")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    historigram(winner)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


@loop_menu
def list_average_by_gender_and_etarian_group_view(context):
    """
    This function prints the average of eratian groups and gender.

    Params:
        context (dict): The context of the application.
    """
    # get the average by gender and etarian group
    winners = average_by_gender_and_etarian_group(
        context.get("participants", []),
    )
    print("\n")
    print("Promedio de Tiempo por grupo etario y sexo")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners, True)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}
