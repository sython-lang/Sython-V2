import sys


class Type:
    def __init__(self, exp):
        self.name = ""
        self.exp = exp

    def tostr(self):
        return self.name


class IntType(Type):
    def __init__(self, exp):
        super(IntType, self).__init__(exp)
        self.name = "integer"


class StrType(Type):
    def __init__(self, exp):
        super(StrType, self).__init__(exp)
        self.name = "string"

    def sum(self, value1, value2):
        return str(value1) + str(value2)

    def sub(self, value1, value2):
        return str(value1)[:len(value1)-value2]

    def increment(self, value1):
        return value1 + value1

    def length(self):
        return len(self.exp.eval())


class FloatType(Type):
    def __init__(self, exp):
        super(FloatType, self).__init__(exp)
        self.name = "float"


class BoolType(Type):
    def __init__(self, exp):
        super(BoolType, self).__init__(exp)
        self.name = "bool"


class List(Type):
    def __init__(self, exp=None, exp2=None):
        super(List, self).__init__(exp)
        self.name = "list"
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

