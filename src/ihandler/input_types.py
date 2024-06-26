from .string_inputs import (
    unrestricted_string,
    strict_string,
    loose_string,
    lowercase_string,
    uppercase_string,
    loose_lowercase_string,
    multiple_strings
)

from .numeric_inputs import (
    strict_numeric,
    loose_numeric,
    strict_integer,
    loose_integer,
    multiple_numerics
)

from .choice_inputs import (
    choice,
    choice2d,
    alphanumeric_choice,
    numeric_choice,
    lowercase_choice,
    uppercase_choice,
    letter_choice,
    binary_choice
)

from .currency_inputs import (
    currency_code,
    alphabetic_currency_code,
    numeric_currency_code
)


INPUT_TYPES = {
    "strict-string": strict_string,
    "loose-string": loose_string,
    "unrestricted-string": unrestricted_string,
    "strict-lowercase": lowercase_string,
    "loose-lowercase": loose_lowercase_string,
    "strict-uppercase": uppercase_string,
    "multiple-strings": multiple_strings,
    "strict-numeric": strict_numeric,
    "strict-integer": strict_integer,
    "loose-numeric": loose_numeric,
    "loose-integer": loose_integer,
    "multiple-numerics": multiple_numerics,
    "choice": choice,
    "choice2d": choice2d,
    "alphanumeric-choice": alphanumeric_choice,
    "numeric-choice": numeric_choice,
    "lowercase-choice": lowercase_choice,
    "uppercase-choice": uppercase_choice,
    "letter-choice": letter_choice,
    "binary-choice": binary_choice,
    "currency-code": currency_code,
    "alphabetic-currency-code": alphabetic_currency_code,
    "numeric-currency-code": numeric_currency_code,
}
