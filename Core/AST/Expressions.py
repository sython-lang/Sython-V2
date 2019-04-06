from rply.token import BaseBox
import sys


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
        else:
            raise Exception

    def sub(self, exp):
        if self.kind == "string" and exp.kind == "integer":
            return self.eval()[:len(self.eval())-exp.value]
        else:
            raise Exception

    def increment(self):
        if self.kind == "string":
            self.value = self.eval() * 2
        else:
            raise Exception


class ExpressionFromList(ExpressionBase):
    def __init__(self, var, indice):
        self.value = ""
        self.kind = "string"
        self.var = var
        self.indice = indice

    def eval(self):
        var = self.var.exp.var
        if len(var) <= self.indice:
            values = self.var.exp.getexpression()
            value = []
            for i in values:
                value.append(i.eval())
            print("List index out of range : \n - Index :", self.indice,
                  "\n - List :", value)
            sys.exit(1)
        self.value, self.kind = var[self.indice].value, var[self.indice].kind
        return self.value


class Nothing(BaseBox):
    @staticmethod
    def eval():
        return None
