from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options,
    print_table,
    one_line_view,
    historigram,
)
from controllers import call_controller


@loop_menu
def actions_menu(context: dict) -> dict:
    """
    This function generates the actions menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
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
    option = None
    options = {
        "Cantidad total de participantes": count_participants_view,
        "Lista con la totalidad de los participantes": list_participants_view,
        "Cantidad de participantes por grupo etario": list_participants_by_etarian_group_view,
        "Cantidad de participantes por sexo": list_participants_by_gender_view,
        "Ganadores por grupo etario": list_winners_by_etarian_group_view,
        "Ganadores por sexo": list_winners_by_gender_view,
        "Ganadores por Grupo Etario y sexo": list_winners_by_gender_and_etarian_group_views,
        "Ganador General": general_winner_view,
        "Historigrama de Participantes por grupo Etario": historigram_etarian_group_view,
        "Promedio de Tiempo por grupo Etario y Sexo": list_average_by_gender_and_etarian_group_view,
        "Volver": lambda context: {"return": True, **context},
        "Salir": call_exit,
    }
    option_keys = list(options.keys())
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)


@loop_menu
def list_participants_view(context):
    """
    This function prints the list of participants.

    Params:
        context (dict): The context of the application.
        participants (list[dict]): The list of participants.
    """

    participants = call_controller(
        "participant",
        "list_participants",
        context.get("participants", []),
    )
    print("\n")
    print("Lista de participantes")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(participants)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


@loop_menu
def count_participants_view(context):
    """
    This function prints the total amount of participants.

    Params:
        context (dict): The context of the application.
        participants (list[dict]): The list of participants.
    """
    count = call_controller(
        "participant",
        "total_participants",
        context.get("participants", []),
        lambda x: True,
    )
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    one_line_view(
        [
            ["Cantidad total de participantes"],
            [str(count)],
        ]
    )
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


@loop_menu
def list_participants_by_etarian_group_view(context):
    """
    This function prints the list of participants by etarian group.

    Params:
        context (dict): The context of the application.
    """

    participants = call_controller(
        "participant",
        "etarian_participants",
        context.get("participants", []),
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


@loop_menu
def list_participants_by_gender_view(context):
    """
    This function prints the list of participants by etarian group.

    Params:
        context (dict): The context of the application.
    """

    participants = call_controller(
        "participant",
        "gender_participants",
        context.get("participants", []),
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


@loop_menu
def list_winners_by_etarian_group_view(context):
    """
    This function prints the list of winners by etarian group.

    Params:
        context (dict): The context of the application.
    """

    winners = call_controller(
        "participant",
        "winners_by_etarian_group",
        context.get("participants", []),
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


@loop_menu
def list_winners_by_gender_view(context):
    """
    This function prints the list of winners by etarian group.

    Params:
        context (dict): The context of the application.
    """

    winners = call_controller(
        "participant",
        "winners_by_gender",
        context.get("participants", []),
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


@loop_menu
def list_winners_by_gender_and_etarian_group_views(context):
    """
    This function prints the list of winners by etarian group.

    Params:
        context (dict): The context of the application.
    """

    winners = call_controller(
        "participant",
        "winners_by_gender_and_etarian_group",
        context.get("participants", []),
    )
    print("\n")
    print("Lista de ganadores por Sexo y por Grupo Etario")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}


@loop_menu
def general_winner_view(context):
    """
    This function prints the general winner.

    Params:
        context (dict): The context of the application.
    """

    winner = call_controller(
        "participant",
        "general_winner",
        context.get("participants", []),
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
    This function prints the general winner.

    Params:
        context (dict): The context of the application.
    """

    winner = call_controller(
        "participant",
        "etarian_participants",
        context.get("participants", []),
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
    This function prints the general winner.

    Params:
        context (dict): The context of the application.
    """

    winners = call_controller(
        "participant",
        "average_by_gender_and_etarian_group",
        context.get("participants", []),
    )
    print("\n")
    print("Promedio de Tiempo por grupo etario y sexo")
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print_table(winners)
    print("\n")
    input("Pulsa una tecla para continuar...")
    return {"return": True, **context}