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


def multiple_numerics(
    prompt: str = "",
    exit_keywords: list | None = None,
    duplicates: bool = True
) -> list[int | float]:
    if not exit_keywords:
        exit_keywords = ["done", "end", "finish", "stop"]
    numeric_values = []
    while True:
        user_input = loose_numeric(prompt)
        if user_input in exit_keywords:
            break
        if "," in user_input:
            input_values = pyvutils.split_by_comma(user_input)
            for value in input_values:
                numeric_values.append(pyvutils.parse_numeric_value(value))
        else:
            numeric_values.append(pyvutils.parse_numeric_value(user_input))
    if not duplicates:
        numeric_values = pyvutils.remove_duplicates(numeric_values)
    return numeric_values
