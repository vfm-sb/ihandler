

class BaseInput:

    def __init__(self, prompt: str = "> ") -> None:
        self._user_input = input(prompt)
        self._user_data = self.input_processor()

    def input_processor(self):
        return self._user_input

    def output(self):
        return self._user_data


if __name__ == "__main__":
    pass
