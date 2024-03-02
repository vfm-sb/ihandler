"""
Numeric Inputs
"""

# Local Modules
import pyvutils
from .string_inputs import strict_string


def strict_numeric(prompt: str = "") -> int | float:
    user_input = strict_string(prompt)
    return pyvutils.parse_numeric_value(user_input)


def loose_numeric(prompt: str = "") -> int | float | str:
    user_input = strict_string(prompt)
    try:
        return pyvutils.parse_numeric_value(user_input)
    except ValueError:
        return user_input


def strict_integer(prompt: str = "") -> int:
    user_input = strict_string(prompt)
    return pyvutils.parse_integer_value(user_input)


def loose_integer(prompt: str = "") -> int:
    user_input = strict_string(prompt)
    try:
        return pyvutils.parse_integer_value(user_input)
    except ValueError:
        return user_input
