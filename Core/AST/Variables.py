from rply.token import BaseBox
from Core.AST.Expressions import ExpressionBase, ExpressionFromList


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
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        self.kind = exp.kind
        self.value = None

    def expression(self):
        return ExpressionBase(self.value, self.kind)

    def eval(self):
        self.value = self.exp.eval()
        self.kind = self.exp.kind
        return ExpressionBase(self.value, self.kind)


class ListVar(BaseBox):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
        self.kind = "list"
        self.value = []
        self.values = []

    def expression(self):
        return ExpressionBase(self.values, self.kind, self)

    def get(self, indice):
        return ExpressionFromList(self, indice)

    def eval(self):
        self.exp.eval()
        self.values = self.exp.getexpression()
        self.value = []
        for i in self.values:
            self.value.append(i.eval())
        return self.value


class List(BaseBox):
    def __init__(self, exp=None, exp2=None):
        if exp is None and exp2 is None:
            self.var = []
        elif exp is None:
            if type(exp2) == List:
                self.var = exp2.var
            else:
                self.var = [exp2]
        elif exp2 is None:
            if type(exp) == List:
                self.var = exp.var
            else:
                self.var = [exp]
        else:
            if type(exp) == List and type(exp2) == List:
                self.var = exp.var
                for i in exp2.var:
                    self.var.append(i)
            elif type(exp) == List:
                self.var = exp.var
                self.var.append(exp2)
            elif type(exp2) == List:
                self.var = [exp]
                for i in exp2.var:
                    self.var.append(i)
            else:
                self.var = [exp, exp2]

    def add(self, exp):
        self.var.append(exp)

    def getexpression(self):
        return self.var

    def eval(self):
        for i in range(len(self.var)):
            self.var[i].value = self.var[i].eval()


class AffectionVar(BaseBox):
    def __init__(self, var, exp):
        self.var = var
        self.exp = exp

    def eval(self):
        self.var.exp = self.exp
        self.var.eval()
        return self.var
