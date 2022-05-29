import sys
from time import sleep
from views.menu_options import (
    generate_menu_options,
    loop_menu
)
from utils import clear_screen


def generate_title() -> None:
    """
    This function generates the title of the application

    Returns:
        None
    """
    print("\n\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    print("  ____                           _   _ _   _             ")
    sleep(0.1)
    print(" / ___|___  _ __ ___  _ __   ___| |_(_) |_(_) ___  _ __  ")
    sleep(0.1)
    print("| |   / _ \| '_ ` _ \| '_ \ / _ \ __| | __| |/ _ \| '_ \ ")
    sleep(0.1)
    print("| |__| (_) | | | | | | |_) |  __/ |_| | |_| | (_) | | | |")
    sleep(0.1)
    print(" \____\___/|_| |_| |_| .__/ \___|\__|_|\__|_|\___/|_| |_|")
    sleep(0.1)
    print("                     |_|                                 ")
    sleep(0.1)
    author = "by Carlos Osuna"
    author = f"{author:^80}"
    for i in range(60):
        print("-", end="")
    print("\n")
    for character in author:
        print(character, end="")
        sleep(0.00005)
    print("\n")


@loop_menu
def main_menu(context: dict) -> None:
    """
    This function generates the main menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        None
    """
    option = None
    options = {
        "Archivo": file_menu,
        "Acciones": actions_menu,
        "Salir": call_exit
    }
    option_keys = list(options.keys())
    generate_title()
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)


@loop_menu
def actions_menu(context: dict) -> None:
    """
    This function generates the actions menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        None
    """
    pass


@loop_menu
def file_menu(context) -> None:
    """
    This function generates the file menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        None
    """
    option = None
    options = {
        "Salir": call_exit,
        "Volver": lambda context: {"return": True, **context}
    }
    option_keys = list(options.keys())
    generate_title()
    options_dict = generate_menu_options(option_keys)
    option = int(input("Selecciona una opción: "))
    method = options[options_dict[option]]
    clear_screen()
    return method(context)


def call_exit(context: dict) -> None:
    """
    This function calls the exit function.

    Params:
        context (dict): The context of the application.

    Returns:
        None
    """
    print("\n")
    print("¡Hasta la próxima!")
    print("\n")
    input("Pulsa una tecla para salir...")
    sys.exit()
