from views.files import (
    file_menu
)
from views.actions import(
    actions_menu
)
from views.utils import (
    clear_screen,
    call_exit,
    loop_menu,
    generate_menu_options
)

# first call the decorator and then will call the function
@loop_menu
def main(context: dict) -> dict:
    """
    This function generates the main menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    option = None
    # generate the menu options
    options = {
        "Archivo": file_menu,
        "Acciones": actions_menu,
        "Salir": call_exit
    }
    option_keys = list(options.keys())
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)
