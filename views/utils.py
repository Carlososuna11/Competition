import os
import sys
from time import sleep

from numpy import histogram
from exceptions import (
    NotTextPlainFile,
    IncompleteParticipantData
)


def generate_title(context: dict) -> None:
    """
    This function generates the title of the application

    Returns:
        None
    """
    clear_screen()
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
    if "file_path" in context:
        file_path = context["file_path"]
        print(f"  Archivo cargado: {file_path}")


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
                generate_title(context)
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
            except (
                FileNotFoundError,
                NotTextPlainFile,
                IncompleteParticipantData
            ) as e:
                print("\n")
                print(f"¡Error! {e}")
                print("\n")
                input("Pulsa una tecla para continuar...")
                for_remove = [
                    "file_path",
                    "participants",
                    "file",
                    "filename",
                ]
                for key in for_remove:
                    if key in context:
                        del context[key]
                context["loop"] = True
                break
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


def print_table(table: list) -> None:
    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3)
        for i in range(len(table[0]))
    ]
    row_formats = []
    for index, longest_col in enumerate(longest_cols):
        if index < len(longest_cols)-1:
            row_formats.append("| {:^" + str(longest_col) + "s}")
        else:
            row_formats.append("| {:^" + str(longest_col) + "s} |")

    row_format = "".join(row_formats)

    for row in table:
        row = [str(cell) for cell in row]
        row_print = row_format.format(*row)
        print("-" * len(row_print))
        print(row_format.format(*row))
    print("-" * len(row_print))


def historigram(table: list) -> None:
    """
    This function generates a histogram.
    Params:
        table (list): The table to be printed.
    Returns:
        None
    """
    table = table[1:]
    histogram_list = []
    for category, count in table:
        histogram_list.append(
            (f"{category} ({count}):", f"| {'*'* int(count)}"))

    table = histogram_list

    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3)
        for i in range(len(table[0]))
    ]

    row_format = "".join(["{:<" + str(longest_col) + "}"
                          for longest_col in longest_cols])

    for row in table:
        print(row_format.format(*row))


def one_line_view(table: list) -> None:
    """
    This function generates a one line view.
    Params:
        table (list): The table to be printed.
    Returns:
        None
    """
    keys = table[0]
    table = table[1:]
    to_print = ""
    for index, value in enumerate(table):
        for key, element in zip(keys, value):
            if key not in ["", " "]:
                to_print += f"{key}: {element}, "
        if index < len(table)-1:
            to_print += " | "
    to_print = to_print.rstrip(",").rstrip(" ")
    print(to_print)
