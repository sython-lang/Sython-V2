from rply.token import BaseBox


class Print(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())


class Input(BaseBox):
    @staticmethod
    def eval(self):
        return input()
