
from ihandler.base_input import BaseInput


class StrictStringInput(BaseInput):
    def input_processor(self) -> str:
        user_input = super().input_processor()
        return user_input.strip()


class LowercaseStringInput(StrictStringInput):
    def input_processor(self) -> str:
        user_input = super().input_processor()
        return user_input.lower()


class UppercaseStringInput(StrictStringInput):
    def input_processor(self) -> str:
        user_input = super().input_processor()
        return user_input.upper()


if __name__ == "__main__":
    pass
