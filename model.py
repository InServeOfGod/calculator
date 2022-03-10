class Model:
    def __init__(self):
        self.value = '0'

    def calculate(self, title: str):
        if title == 'C':
            self._default()

        elif self.value == '0':
            self.value = str(title)

        elif self.value == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif self.value == '%':
            pass

        elif self.value == '.':
            pass

        elif isinstance(title, int):
            self.value += str(title)

        return self.value

    def _default(self):
        self.value = '0'
