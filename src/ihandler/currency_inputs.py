"""
Currency Inputs
"""

# Local Modules
import pyvutils
from .string_inputs import strict_string, uppercase_string


def currency_code(prompt: str) -> str:
    user_input = uppercase_string(prompt)
    pyvutils.assert_currency_code(user_input)
    return user_input


def alphabetic_currency_code(prompt: str) -> str:
    user_input = uppercase_string(prompt)
    pyvutils.assert_iso_alphabetic_code(user_input)
    return user_input


def numeric_currency_code(prompt: str) -> str:
    user_input = strict_string(prompt)
    pyvutils.assert_iso_alphabetic_code(user_input)
    return user_input
