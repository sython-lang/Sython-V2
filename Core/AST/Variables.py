from rply.token import BaseBox
from Core.AST.Expressions import ExpressionBase


class Variables(BaseBox):
    def __init__(self):
        self.vars = []

    def add(self, var):
        if self.get(var.name) is not None:
            self.set(var.name, var.value)
        else:
            self.vars.append(var)

    def get(self, nom):
        for i in self.vars:
            if i.name == nom:
                return i
        return None

    def set(self, nom, exp):
        var = self.get(nom)
        if var is not None:
            var.value = exp


class Variable(BaseBox):
    def __init__(self, name, value, kind):
        self.name = name
        self.value = value
        self.kind = kind

    def eval(self):
        return ExpressionBase(self.value, self.kind)
