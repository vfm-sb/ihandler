"""
Choice Inputs
"""

# Built-in Modules
import string
from typing import Optional

# Local Modules
import pyvutils
from .numeric_inputs import loose_integer


def choice(prompt: str, choices: list, types: list, case_sensitive: bool = True, start: int = 1) -> str:
    user_choice = loose_integer(prompt)
    valid_choices = _get_valid_choices(choices, types, start)
    _assert_user_choice(user_choice, valid_choices, case_sensitive)
    choice_index = _get_choice_index(user_choice, valid_choices, case_sensitive)
    return choices[choice_index]


def choice2d(prompt: str, choices: list[list], types: list, case_sensitive: bool = True, start: int = 1) -> str:
    user_choice = loose_integer(prompt)
    valid_choices = _get_valid_choices(choices, types, start)
    _assert_user_choice(user_choice, valid_choices, case_sensitive)
    choice_index = _get_2d_choice_index(user_choice, valid_choices, case_sensitive)
    return choices[choice_index][0]


def alphanumeric_choice(prompt: str, choices: list, start: int = 1) -> str:
    types = ["numeric", "lowercase", "uppercase"]
    return choice(prompt, choices, types, start)


def numeric_choice(prompt: str, choices: list, start: int = 1) -> str:
    return choice(prompt, choices, ["numeric"], start)


def lowercase_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["lowercase"])


def uppercase_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["uppercase"])


def letter_choice(prompt: str, choices: list) -> str:
    return choice(prompt, choices, ["lowercase", "uppercase"])


def _assert_user_choice(user_choice: int | str, valid_choices: list, case_sensitive: bool = True) -> None:
    if not case_sensitive and isinstance(user_choice, str):
        user_choice = user_choice.lower()
    if user_choice not in pyvutils.flatten(valid_choices):
        raise ValueError("Invalid Choice")


def _get_valid_choices(choices: list, types: list, start: int = 1) -> list:
    number_of_choices = len(choices)
    options = [choices]
    for option_type in types:
        if option_type == "numeric":
            options.append(list(range(start, number_of_choices + start)))
        elif option_type == "lowercase":
            options.append(list(string.ascii_lowercase[:number_of_choices]))
        elif option_type == 'uppercase':
            options.append(list(string.ascii_uppercase[:number_of_choices]))
    return options


def _get_choice_index(user_choice: int | str, valid_choices: list, case_sensitive: bool = True) -> Optional[int]:
    if not case_sensitive and isinstance(user_choice, str):
        user_choice = user_choice.lower()
    for choice_group in valid_choices:
        if user_choice in choice_group:
            return choice_group.index(user_choice)
    return None


def _get_2d_choice_index(user_choice: int | str, valid_choices: list, case_sensitive: bool = True) -> Optional[int]:
    def is_nested_list(lst: list) -> bool:
        return any(isinstance(item, list) for item in lst)

    if not case_sensitive and isinstance(user_choice, str):
        user_choice = user_choice.lower()
    for choice_group in valid_choices:
        if is_nested_list(choice_group):
            for subgroup in choice_group:
                if user_choice in subgroup:
                    return subgroup.index(user_choice)
        elif user_choice in choice_group:
            return choice_group.index(user_choice)
    return None


if __name__ == "__main__":
    pass
