from files.utils import (
    is_text_plain_file,
    is_text_plain_v2,
    get_path,
    file_exists
)
from exceptions.file import (
    NotTextPlainFile
)
from exceptions.participant import (
    IncompleteParticipantData
)
from models import Participant


def load_file(
    filename: str,
    *args: any,
    **kwargs: any
) -> dict:
    """
    This function loads the file. The file must be a text plain file.

    Params:
        filename (str): The filename of the text plain file (Can be a path
        o just only the name of the file)
        *args (any): The arguments of the function.
        **kwargs (any): The keyword arguments of the function.

    Returns:
        dict: The context of the application.
    """

    # get the context from args or kwargs
    context = args[0] if len(args) > 0 else kwargs.get("context", {})

    filename = filename
    if filename is None:
        raise FileNotFoundError("No se ha definido el nombre del archivo.")

    # Complete the path (Make relative path to absolute path)
    path = get_path(filename)

    # Check if the file exists
    if not file_exists(path):
        raise FileNotFoundError(
            f"El archivo {path} no existe."
        )

    # This more easy way to check if the file is a text plain file.
    if not is_text_plain_v2(path):
        raise NotTextPlainFile(path)

    # this way is more complex because it verify if the file is binary
    # first and then negate the result.
    if not is_text_plain_file(path):
        raise NotTextPlainFile(path)

    context["filename"] = filename

    with open(path, "r") as file:
        # set in the context the file.
        context["file"] = file.readlines()
        # set in the context the file path.
        context["file_path"] = path

    return context


def load_participant_data(filename: str, *args, **kwargs) -> dict:
    """
    This fuction loads the participant data.
    It need to have structure:
    ci,first_last_name,second_last_name,first_name,first_char_second_name,
    gender,age,hours,minutes,seconds.

    Params:
        filename (str): The filename of the text plain file (Can be a path
        o just only the name of the file).
        *args (any): The arguments of the function.
        **kwargs (any): The keyword arguments of the function.

    Returns:
        dict: The context of the application.
    """

    # first load the file
    context = load_file(filename, *args, **kwargs)

    # get the file
    file = context.get("file")

    # validate the length of the file
    if len(file) == 0:
        raise ValueError("El archivo está vacío.")

    # declare the list of participants
    users = []

    # declare list of keys for each column
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
    # iterate the file line by line
    for index, line in enumerate(file):
        # remove the backscape and split the line by comma (to get the columns)
        user_dict_values = line.strip().strip('\n').split(',')
        # compare the quantity of given columns with the quantity of keys
        if len(user_dict_values) != len(user_dict_keys):
            # raise an error if the quantity of columns is different
            raise IncompleteParticipantData(
                index,
                len(user_dict_values),
                len(user_dict_keys)
            )
        # create a dictionary with the values of the columns
        user_dict = dict(zip(user_dict_keys, user_dict_values))
        # create a participant object and pass the dictionary
        user = Participant(**user_dict)
        # append the participant to the list
        users.append(user)
    # set the list of participants in the context
    context["participants"] = users
    return context
