from .string_inputs import (
    strict_string, unrestricted_string, lowercase_string, uppercase_string,
    multiple_strings,
)

from .numeric_inputs import (
    strict_numeric, loose_numeric, strict_integer, loose_integer,
)

from .choice_inputs import (
    choice, alphanumeric_choice, numeric_choice,
    lowercase_choice, uppercase_choice, letter_choice,
)


INPUT_TYPES = {
    "strict-string": strict_string,
    "unrestricted-string": unrestricted_string,
    "lower-string": lowercase_string,
    "upper-string": uppercase_string,
    "multiple-strings": multiple_strings,
    "numeric": strict_numeric,
    "integer": strict_integer,
    "loose-numeric": loose_numeric,
    "loose-integer": loose_integer,
    "choice": choice,
    "alphanumeric-choice": alphanumeric_choice,
    "numeric-choice": numeric_choice,
    "lowercase-choice": lowercase_choice,
    "uppercase-choice": uppercase_choice,
    "letter-choice": letter_choice,
}
