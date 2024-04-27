import inspect
from typing import Callable

def tool(function_description: str = None, required_params: list[str] = [], **parameters_descriptions):
    """
    A decorator to add descriptions to a function and its parameters with the tool format.

    This decorator allows you to specify descriptions for both the tool itself and its parameters.

    Args:
        function_description (str, optional): Overrides the description of the function. If provided, this description will replace the original function description. Defaults to None, in which case the original function description will be retained.
        required_params (list[str], optional): Sets the required parameters for the tool that the model will set. If empty, it will set all non-optional parameters of the function as required and optional parameters as not required.
        **parameters_descriptions: Keyword arguments where the key is the parameter name and the value is the description for that parameter. Each parameter can have an associated description, providing insights into its usage and meaning.

    Returns:
        decorator: A decorator function that can be applied to target functions to add descriptions to them and their parameters with the tool format.
    """
    def decorator(func: Callable) -> Callable:
        signature = inspect.signature(func)
        for param in required_params:
            if param not in signature.parameters:
                raise ValueError(f"The parameter '{param}' provided in 'required_params' was not found in the function signature. Please ensure that the parameter names in 'required_params' match exactly with the parameter names defined in the function signature.")
        for param_name, _ in parameters_descriptions.items():
            if param_name not in signature.parameters:
                raise ValueError(f"The parameter '{param_name}' provided in the decorator was not found in the function signature. Please ensure that the parameter names in the decorator match exactly with the parameter names defined in the function signature.")
        if function_description:
            func.__doc__ = function_description
        func.__required__ = required_params
        func.__parameters_descriptions__ = parameters_descriptions
        return func
    return decorator

def get_tool(func: Callable) -> dict:
    """
    Gets a dictionary representing information about a function in a specific format suitable for a tool.
    This extracts metadata about a given function, such as its name, description, and parameter information, and organizes it into a dictionary in a format optimized for use as a tool.
    It's recommended to use this together with the 'tool' decorator, but it's not obligatory.

    Args:
        func (Callable): The function for which metadata is to be retrieved. This should be a callable object, typically a function or method.

    Returns:
        dict: A dictionary containing information about the function in the tool-specific format. The dictionary includes the function's name, description, and details about its parameters.
    """
    signature = inspect.signature(func)

    function_name = func.__name__
    description = inspect.getdoc(func)
    
    properties = {}
    required = []

    for param_name, param in signature.parameters.items():
        param_info = {
            "type": str(param.annotation).split("'")[1],
            "description": func.__parameters_descriptions__.get(param_name, "None")
        }
        properties[param_name] = param_info
        if param.default == inspect.Parameter.empty:
            required.append(param_name)

    if func.__required__:
        required = func.__required__

    function_info = {
        "type": "function",
        "function": {
            "name": function_name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required
            },
        }
    }
    
    return function_info