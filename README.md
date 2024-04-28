# LLM Tool Parser

The `LLMToolParser.py` provides a tool for annotating Python functions and their parameters with descriptions for function calling.  
This tool is helpful for documenting functions and generating metadata suitable for tooling purposes.  
Compact, simple and should be pretty eazy to use!

## Install
Install using pip:
```bash
pip install git+https://github.com/pandora-s-git/LLMToolParser.git
```

## Usage

### `tool` Decorator

The `tool` decorator allows you to annotate your tools with descriptions and set the required parameters. It takes the following arguments:

- `function_description`: An optional description of the function.
- `required_params`: An optional list of required parameters for the tool.
- `**parameters_descriptions`: Keyword arguments providing descriptions for each parameter.

### `get_tool` Function

The `get_tool` function retrieves metadata about a given function and organizes it into a dictionary format suitable for tooling. It returns a dictionary containing information about the function, its description, and its parameters.

## Example

```python
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
print(json.dumps(info, indent=4))
```
Output:
```json
{
    "type": "function",
    "function": {
        "name": "example_function",
        "description": "This function takes three parameters and returns them as a tuple.\n\nParameters:\n    x (int): An integer representing some value.\n    y (float): A floating-point number representing another value.\n    z (str, optional): A string representing a label (default value: 'default').\n\nReturns:\n    tuple: A tuple containing the input parameters.",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "int",
                    "description": "An integer representing some value."
                },
                "y": {
                    "type": "float",
                    "description": "A floating-point number representing another value."
                },
                "z": {
                    "type": "str",
                    "description": "A string representing a label (default value: 'default')."
                }
            },
            "required": [
                "x",
                "y"
            ]
        }
    }
}
```