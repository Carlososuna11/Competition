import sys
from time import sleep
from views.options import (
    generate_menu_options,

)
from utils import clear_screen


def loop_menu(function: callable) -> callable:
    """
    This decorator loop function.
    Params:
        function (callable): The function to be looped.
    Returns:
        None
    """
    def wrapper(*args, **kwargs):
        # get context from args or kwargs
        context = args[0] if len(args) > 0 else kwargs.get("context", {})
        if not isinstance(context, dict):
            raise TypeError("El contexto debe ser un diccionario")
        while True:
            try:
                context = function(context)
                if "loop" in context:
                    del context["loop"]
                    continue
                if "return" in context:
                    context["loop"] = True
                    del context["return"]
                break
            except ValueError:
                print("\n")
                print("¡Error! Debes introducir un número.")
                print("\n")
                input("Pulsa una tecla para continuar...")
            except KeyboardInterrupt:
                print("\n")
                print("Has cancelado la ejecución del programa.")
                print("\n")
                input("Pulsa una tecla para salir...")
                sys.exit()
            except KeyError:
                print("\n")
                print("¡Error! Debes introducir una opción válida.")
                print("\n")
                input("Pulsa una tecla para continuar...")
            except Exception as e:
                print(e)
                print("\n")
                print("¡Error! No se ha podido ejecutar la opción.")
                print("\n")
                input("Pulsa una tecla para continuar...")
            clear_screen()
        clear_screen()
        return context
    return wrapper


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
def main_menu(context: dict) -> dict:
    """
    This function generates the main menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
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
def actions_menu(context: dict) -> dict:
    """
    This function generates the actions menu of the application.

    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """
    pass


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
