# Built-in Modules
from typing import Any

# Local Packages, Modules and Constants
from ihandler.input_types import INPUT_TYPES


class InputHandler:

    def __init__(self, input_type: str, prompt: str = "> ") -> None:
        if input_type not in INPUT_TYPES:
            raise ValueError("Invalid Input Type") # TODO Use InvalidInputTypeError Instead
        self.handler = INPUT_TYPES.get(input_type)(prompt)

    @property
    def output(self) -> Any:
        return self.handler.output()


def ihandler(input_type: str, prompt: str = "") -> Any:
    return InputHandler(input_type, prompt).output


if __name__ == "__main__":
    pass
