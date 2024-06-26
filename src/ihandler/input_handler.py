# Built-in Modules
from typing import Any

# Local Packages, Modules and Constants
from ihandler.input_types import INPUT_TYPES


class InputHandler:

    def __init__(self, input_type: str, prompt: str = "> ", **kwargs) -> None:
        if input_type not in INPUT_TYPES:
            raise ValueError("Invalid Input Type")
        self._user_input = INPUT_TYPES.get(input_type)(prompt, **kwargs)

    @property
    def output(self) -> Any:
        return self._user_input


def ihandler(input_type: str, prompt: str = "> ", **kwargs) -> Any:
    return InputHandler(input_type, prompt, **kwargs).output


if __name__ == "__main__":
    pass
