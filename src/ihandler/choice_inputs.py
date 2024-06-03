"""
Choice Inputs
"""

# Built-in Modules
import string
from typing import Optional

# Local Modules
import pyvutils
from .numeric_inputs import loose_integer


def choice(prompt: str, choices: list, types: list) -> str:
    user_choice = loose_integer(prompt)
    valid_choices = _get_valid_choices(choices, types)
    _assert_user_choice(user_choice, valid_choices)
    choice_index = _get_choice_index(user_choice, valid_choices)
    return choices[choice_index]


def alphanumeric_choice(prompt: str, choices: list) -> str:
    types = ["numeric", "lowercase", "uppercase"]
    return choice(prompt, choices, types)


def numeric_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["numeric"])


def lowercase_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["lowercase"])


def uppercase_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["uppercase"])


def letter_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["lowercase", "uppercase"])


def _assert_user_choice(user_choice: int | str, valid_choices: list) -> None:
    if user_choice not in pyvutils.flatten(valid_choices):
        raise ValueError("Invalid Choice")


def _get_valid_choices(choices: list, types: list) -> list:
    number_of_choices = len(choices)
    options = [choices]
    for option_type in types:
        if option_type == "numeric":
            options.append(list(range(1, number_of_choices + 1)))
        elif option_type == "lowercase":
            options.append(list(string.ascii_lowercase[:number_of_choices]))
        elif option_type == 'uppercase':
            options.append(list(string.ascii_uppercase[:number_of_choices]))
    return options


def _get_choice_index(user_choice: int | str, valid_choices: list) -> Optional[int]:
    for choice_group in valid_choices:
        if user_choice in choice_group:
            return choice_group.index(user_choice)
    return None
