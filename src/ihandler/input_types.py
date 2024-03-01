from ihandler.string_inputs import (
    strict_string, unrestricted_string, lowercase_string, uppercase_string,
    multiple_strings,
)


INPUT_TYPES = {
    "strict-string": strict_string,
    "unrestricted-string": unrestricted_string,
    "lower-string": lowercase_string,
    "upper-string": uppercase_string,
    "multiple-strings": multiple_strings,
}
