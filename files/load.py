from files.utils import (
    is_text_plain_file,
    get_path,
    file_exists
)
from exceptions import (
    NotTextPlainFile,
    IncompleteParticipantData
)
from models import Participant


def load_file(filename: str, *args: any, **kwargs: any) -> dict:
    """
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """

    context = args[0] if len(args) > 0 else kwargs.get("context", {})

    filename = filename
    if filename is None:
        raise NotImplementedError("No se ha definido el nombre del archivo.")
    path = get_path(filename)
    if not file_exists(path):
        raise FileNotFoundError(
            f"El archivo {path} no existe."
        )
    if not is_text_plain_file(path):
        raise NotTextPlainFile(path)

    context["filename"] = filename

    with open(path, "r") as file:
        context["file"] = file.readlines()
        context["file_path"] = path

    return context


def load_data(filename: str, *args, **kwargs) -> dict:
    """
    Params:
        context (dict): The context of the application.

    Returns:
        dict: The context of the application.
    """

    context = load_file(filename, *args, **kwargs)
    file = context.get("file")
    if len(file) == 0:
        raise ValueError("El archivo está vacío.")
    users = []
    user_dict_keys = [
        "ci",
        "first_last_name",
        "second_last_name",
        "first_name",
        "first_char_second_name",
        "gender",
        "age",
        "hours",
        "minutes",
        "seconds"
    ]
    for index, line in enumerate(file):
        user_dict_values = line.strip().strip('\n').split(',')
        if len(user_dict_values) != len(user_dict_keys):
            raise IncompleteParticipantData(
                index,
                len(user_dict_values),
                len(user_dict_keys)
            )
        user_dict = dict(zip(user_dict_keys, user_dict_values))
        user = Participant(**user_dict)
        users.append(user)
    context["participants"] = users
    return context
