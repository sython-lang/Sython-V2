from rply.token import BaseBox


class ExpressionBase(BaseBox):
    def __init__(self, value, kind, var = None):
        self.value = value
        self.kind = kind
        self.var = var

    def eval(self):
        if self.var is not None:
            self.value, self.kind = self.var.value, self.var.kind
        return self.value

    def sum(self, exp):
        if self.kind == "string" or exp.kind == "string":
            return str(self.eval()) + str(exp.eval())

    def sub(self, exp):
        if self.kind == "string" and exp.kind == "integer":
            return self.eval()[:len(self.eval())-exp.value]

    def increment(self):
        if self.kind == "string":
            self.value = self.eval() * 2


class Nothing(BaseBox):
    @staticmethod
    def eval():
        return None
