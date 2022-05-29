import sys
from utils import clear_screen


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


def loop_menu(function: callable) -> None:
    """
    This decorator loop function.
    Params:
        function (callable): The function to be looped.
    Returns:
        None
    """
    def wrapper(*args, **kwargs):
        # get context from args or kwargs
        context = args[0] if len(args) > 0 else kwargs["context"]
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
