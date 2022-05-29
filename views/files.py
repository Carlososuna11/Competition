from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options
)
from files.load import (
    load_data
)


@loop_menu
def file_menu(context: dict) -> dict:
    """
    This function generates the file menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    option = None
    options = {
        "Cargar Archivo": load_file_menu,
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
def load_file_menu(context: dict) -> dict:
    """
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    option = None
    options = {
        "Cargar Archivo por defecto (./data/competencia.txt)":
        lambda
        context: {
            "return": True,
            **load_data(
                **{"context": context, "filename": "./data/competencia.txt"}
            )
        },
        "Cargar Archivo personalizado": load_file_custom_menu,
        "Volver": lambda context: {"return": True, **context},
        "Salir": call_exit, }
    option_keys = list(options.keys())
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)


def load_file_custom_menu(context: dict) -> dict:
    """
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    filename = input("Ingresa el nombre del archivo: ")
    arguments = {"context": context, "filename": filename}
    context = load_data(**arguments)
    return {"return": True, **context}
