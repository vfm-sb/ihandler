from ihandler.string_inputs import (
    StrictStringInput, UnrestrictedStringInput,
    LowercaseStringInput, UppercaseStringInput
)


INPUT_TYPES = {
    "strict-string": StrictStringInput,
    "unrestricted-string": UnrestrictedStringInput,
    "lower-string": LowercaseStringInput,
    "upper-string": UppercaseStringInput,
}
