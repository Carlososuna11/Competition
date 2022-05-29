from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options,
    print_table,
    one_line_view
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
    participants = context["participants"]
    options = {
        "Cantidad total de participantes": count_participants_view,
        "Lista con la totalidad de los participantes": list_participants_view,
        "Cantidad de participantes por grupo etario": list_participants_by_etarian_group_view,
        "Cantidad de participantes por sexo": list_participants_by_gender_view,
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
