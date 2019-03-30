from rply.token import BaseBox


class Variables(BaseBox):
    def __init__(self):
        self.vars = []

    def add(self, var):
        if self.get(var.name) is not None:
            self.set(var.name, var.exp)
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
            var.exp = exp


class Variable(BaseBox):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def eval(self):
        self.exp.eval()
