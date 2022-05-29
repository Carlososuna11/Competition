
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
