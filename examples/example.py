import LLMToolParser
import json

@LLMToolParser.tool(x = "An integer representing some value.", y = "A floating-point number representing another value.", z = "A string representing a label (default value: 'default').")
def example_function(x: int, y: float, z: str = "default") -> tuple:
    """
    This function takes three parameters and returns them as a tuple.
    
    Parameters:
        x (int): An integer representing some value.
        y (float): A floating-point number representing another value.
        z (str, optional): A string representing a label (default value: 'default').
    
    Returns:
        tuple: A tuple containing the input parameters.
    """
    return x, y, z

info = LLMToolParser.get_tool(example_function)
print(json.dumps(info, indent = 4))

#{
#    "type": "function",
#    "function": {
#        "name": "example_function",
#        "description": "This function takes three parameters and returns them as a tuple.\n\nParameters:\n    x (int): An integer representing some value.\n    y (float): A floating-point number representing another value.\n    z (str, optional): A string representing a label (default value: 'default').\n\nReturns:\n    tuple: A tuple containing the input parameters.",
#        "parameters": {
#            "type": "object",
#            "properties": {
#                "x": {
#                    "type": "int",
#                    "description": "An integer representing some value."
#                },
#                "y": {
#                    "type": "float",
#                    "description": "A floating-point number representing another value."
#                },
#                "z": {
#                    "type": "str",
#                    "description": "A string representing a label (default value: 'default')."
#                }
#            },
#            "required": [
#                "x",
#                "y"
#            ]
#        }
#    }
#}