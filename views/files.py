from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_title,
    generate_menu_options
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
        "Cargar Archivo": load_file,
        "Volver": lambda context: {"return": True, **context},
        "Salir": call_exit,
    }
    option_keys = list(options.keys())
    generate_title()
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)


@loop_menu
def load_file(context: dict) -> dict:
    """
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    option = None
    options = {
        "Cargar Archivo por defecto (./competencia.txt)": lambda context: context,
        "Cargar Archivo personalizado": lambda context: context,
        "Volver": lambda context: {"return": True, **context},
        "Salir": call_exit,
    }
    option_keys = list(options.keys())
    generate_title()
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)
