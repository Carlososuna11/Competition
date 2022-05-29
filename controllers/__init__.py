from importlib import import_module

controllers = {
    'participant': import_module('controllers.participant'),
}


def call_controller(
        controller: str,
        function: str,
        *args: any,
        **kwargs: any
) -> dict:
    """
    This function calls a controller function.

    Params:
        context (dict): The context of the application.
        function (str): The name of the function to be called.

    Returns:
        dict: The context of the application.
    """
    if controller not in controllers:
        raise Exception('Controller not found: %s' % controller)
    module = controllers[controller]
    callable_function = getattr(module, function)
    if not callable(callable_function):
        raise Exception('Function not found: %s' % function)
    return callable_function(*args, **kwargs)
