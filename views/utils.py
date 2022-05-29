import os
import sys
from time import sleep


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


def clear_screen() -> None:
    """
    Clear the screen.

    Returns:
        None

    """
    os.system("cls" if os.name == "nt" else "clear")


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


def generate_menu_options(options: list[str]) -> dict:
    """
    This function generates the menu options.
    Params:
        options (list[str]): The options to be printed.
    Returns:
        dict: The menu options.
    """
    options_dict = {}
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    for i in range(len(options)):
        print(f"  {i+1}. {options[i]}")
        options_dict[i+1] = options[i]
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    return options_dict
