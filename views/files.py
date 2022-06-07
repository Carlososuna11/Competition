from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options
)
from files.load import (
    load_participant_data
)


# first call the decorator and then will call the function
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
    # generate the menu options
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


# first call the decorator and then will call the function
@loop_menu
def load_file_menu(context: dict) -> dict:
    """
    This function generates the load file menu of the application.
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    option = None
    # generate the menu options
    options = {
        # loads the default file
        "Cargar Archivo por defecto (./data/competencia.txt)":
        lambda
        context: {
            "return": True,
            **load_participant_data(
                **{"context": context, "filename": "./data/competencia.txt"}
            )
        },
        # loads a custom file
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
    filename = input(
        "**Nota**: si el archivo está en una"
        " subcarpeta (Ej: data/competencia.txt)\n usar './' o no declarar el"
        " '/' al inicio\n\nPara volver solo presiona enter\n\nIngresa la ruta del archivo : ")
    arguments = {"context": context, "filename": filename}
    context = load_participant_data(**arguments)
    return {"return": True, **context}
