from rply.token import BaseBox


class ExpressionBase(BaseBox):
    def __init__(self, value, kind):
        self.value = value
        self.kind = kind

    def eval(self):
        return self.value

    def sum(self, exp):
        if self.kind == "string" or exp.kind == "string":
            return str(self.value) + str(exp.eval())

    def sub(self, exp):
        if self.kind == "string" and exp.kind == "integer":
            return self.value[:len(self.value)-exp.value]

    def sumaff(self, exp):
        if self.kind == "string" or exp.kind == "string":
            self.value = str(self.value) + str(exp.eval())

    def subaff(self, exp):
        if self.kind == "string" and exp.kind == "integer":
            self.value = self.value[:len(self.value)-exp.value]

    def increment(self):
        if self.kind == "string":
            self.value *= 2


class Nothing(BaseBox):
    @staticmethod
    def eval():
        return None
