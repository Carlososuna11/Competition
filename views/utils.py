import os
import sys
from time import sleep
from exceptions.file import (
    NotTextPlainFile
)
from exceptions.participant import (
    IncompleteParticipantData
)


def generate_title(context: dict) -> None:
    """
    This function generates the title of the application

    Params:
        context (dict): The context of the application.

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
    print("| |   / _ \| '_ ` _ \| '_ \ / _ \ __| | __| |/ _ \| '_ \ ")  # noqa  W605
    sleep(0.1)
    print("| |__| (_) | | | | | | |_) |  __/ |_| | |_| | (_) | | | |")  # noqa  W605
    sleep(0.1)
    print(" \____\___/|_| |_| |_| .__/ \___|\__|_|\__|_|\___/|_| |_|")  # noqa  W605
    sleep(0.1)
    print("                     |_|                                 ")  # noqa  W605
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
    # if "file_path" in context: prints the file path
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
    This decorator have all exceptions handled. for reusing the same function
    Params:
        function (callable): The function to be looped.
    Returns:
        None
    """
    # the wrapper function
    def wrapper(*args, **kwargs):
        # get context from args or kwargs
        context = args[0] if len(args) > 0 else kwargs.get("context", {})
        if not isinstance(context, dict):
            raise TypeError("El contexto debe ser un diccionario")
        while True:
            try:
                # generate the title
                generate_title(context)
                # call the function and returns the context
                context = function(context)
                """
                loop in contexts means that the function is called again
                (there is no break)
                """
                if "loop" in context:
                    del context["loop"]
                    continue
                """
                return in contexts means that the before function is
                called again. (there is break)
                """
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

                # remove because the file is not valid or has some
                # errors
                for_remove = [
                    "file_path",
                    "participants",
                    "file",
                    "filename",
                ]
                for key in for_remove:
                    if key in context:
                        del context[key]
                # set loop again to repeat the function
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
        # return context
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
    # iterate que quantity of options
    for i in range(len(options)):
        # add the option to the dict and the value is the index
        print(f"  {i+1}. {options[i]}")
        options_dict[i+1] = options[i]
    print("\n")
    for i in range(60):
        print("-", end="")
    print("\n")
    # return the dict options
    return options_dict


def print_table(
    table: list,
    merge_first_column: bool = False
) -> None:
    """
    This function prints dinamics table.
    Params:
        table (list): A matrix to be printed.
        merge_first_column (bool): If the first column should be merged.
    Returns:
        None
    """
    # get the max length of each column
    longest_cols = [
        (
            max(
                [
                    len(
                        str(row[i])
                    ) for row in table
                ]
            ) + 3   # +3 for the padding
        )
        for i in range(
            len(table[0])
        )   # quantity of columns
    ]
    row_formats = []
    # set a format for each column (padding, alignment) and
    # set borders
    for index, longest_col in enumerate(longest_cols):
        if index < len(longest_cols)-1:
            # if is not the last column add the border at left
            row_formats.append("| {:^" + str(longest_col) + "s}")
        else:
            # if is the last column add the border at right and left
            row_formats.append("| {:^" + str(longest_col) + "s} |")

    # join the formats to a string(every column)
    row_formats_list = row_formats
    row_format = "".join(row_formats)

    first_column_value = None
    print_lines_change = False
    # iterate the table
    for row in table:
        # convert to string the cell for each column
        row = [str(cell) for cell in row]
        # if the first column need to be merged
        if merge_first_column:
            # if the first column should be merged
            if first_column_value != row[0]:
                # if is the first row
                first_column_value = row[0]
                print_lines_change = True
            else:
                # if is not the first row
                row[0] = len(row[0]) * " "
        # print the row desectructe the list to args
        row_print = row_format.format(*row)
        # print the separator if is the first row not merged
        if not(merge_first_column):
            print("-" * len(row_print))
        else:
            # if is the first row print the separator
            if print_lines_change:
                print("-" * len(row_print))
                print_lines_change = False
            else:
                # if new joined row is the same as the previous
                print(
                    row_formats_list[0].format(" ") + "-" *
                    (
                        len(row_print) - len(row_formats_list[0].format(" "))
                    )
                )
        print(row_print)
    print("-" * len(row_print))


def historigram(table: list) -> None:
    """
    This function generates a histogram.
    Params:
        table (list): The table to be printed.
    Returns:
        None
    """
    table = table[1:]   # get the table
    histogram_list = []
    for category, count in table:
        histogram_list.append(
            (f"{category} ({count}):", f"| {'*'* int(count)}"))

    # set new table (based only in the count and *)
    table = histogram_list

    longest_cols = [
        (
            max(
                [
                    len(
                        str(row[i])
                    ) for row in table
                ]
            ) + 3   # +3 for the padding
        )
        for i in range(
            len(table[0])
        )   # quantity of columns
    ]

    # set a format for each column (padding, alignment) and
    row_format = "".join(["{:<" + str(longest_col) + "}"
                          for longest_col in longest_cols])

    for row in table:
        # print the row desecte the list to args
        print(row_format.format(*row))


def one_line_view(table: list) -> None:
    """
    This function generates a one line view.
    Params:
        table (list): The table to be printed.
    Returns:
        None
    """
    # get the keys
    keys = table[0]
    # get the values
    table = table[1:]
    to_print = ""
    # iterate the table
    for index, value in enumerate(table):
        for key, element in zip(keys, value):
            # print in one line
            if key not in ["", " "]:
                to_print += f"{key}: {element}, "
        # if the table has more than one row set a sepparator
        if index < len(table)-1:
            to_print += " | "
    # remove the last comma and space
    to_print = to_print.rstrip(" ").rstrip(",")
    print(to_print)
