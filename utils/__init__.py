import os
from typing import Union


def get_path(path: str) -> str:
    """
    Get the absolute path of the file.

    Params:
        path (str): The path of the file.

    Returns:
        str: The absolute path of the file.

    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))


def clear_screen() -> None:
    """
    Clear the screen.

    Returns:
        None

    """
    os.system("cls" if os.name == "nt" else "clear")


def path_exists(path: str) -> bool:
    """
    Check if the path exists.

    Params:
        path (str): The path to be checked.

    Returns:
        bool: True if the path exists, False otherwise.

    """
    return os.path.exists(path)


def bool_from_str(value: str) -> Union[bool, None]:
    """
    Convert string to boolean.

    Params:
        value (str): The string to be converted.

    Returns:
        Union[bool,None]: The boolean value of the string or None
        if the string is not a valid boolean.
    """
    if value is None:
        return None
    if value.lower() in ['true', '1', 'yes', 'y', 't', 'si', ]:
        return True
    elif value.lower() in ['false', '0', 'no', 'n', 'f']:
        return False
    return None
