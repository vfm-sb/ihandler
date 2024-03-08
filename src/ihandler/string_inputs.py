"""
String Inputs
"""

# Local Modules
import pyvutils


def unrestricted_string(prompt: str = "") -> str:
    return input(prompt)


def strict_string(prompt: str = "") -> str:
    user_input = input(prompt)
    pyvutils.assert_input(user_input)
    return user_input.strip()


def loose_string(prompt: str = "") -> str:
    user_input = input(prompt)
    return user_input.strip()


def lowercase_string(prompt: str = "") -> str:
    user_input = strict_string(prompt)
    return user_input.lower()


def uppercase_string(prompt: str = "") -> str:
    user_input = strict_string(prompt)
    return user_input.upper()


def loose_lowercase_string(prompt: str = "") -> str:
    user_input = loose_string(prompt)
    return user_input.lower()


def multiple_strings(
    prompt: str = "",
    exit_keywords: list | None = None,
    duplicates: bool = True
) -> list[str]:
    if not exit_keywords:
        exit_keywords = ["done", "end", "finish", "stop"]
    strings = []
    while True:
        user_input = lowercase_string(prompt)
        if user_input in exit_keywords:
            break
        if "," in user_input:
            values = pyvutils.split_by_comma(user_input)
            strings.extend(values)
        else:
            strings.append(user_input)
    if not duplicates:
        strings = pyvutils.remove_duplicates(strings)
    return strings


if __name__ == "__main__":
    pass
