from rply.token import BaseBox
from Core.AST.Expressions import ExpressionBase
import sys


class Print(BaseBox):
    def __init__(self, value=ExpressionBase("", "string")):
        self.value = value
        self.kind = "string"

    def apply(self):
        print(self.value.eval())

    def eval(self):
        return self.value.eval()


class Input(BaseBox):
    def __init__(self, text=""):
        self.text = text
        self.value = ""
        self.kind = "string"

    def apply(self):
        self.value = input(self.text[1:-1])

    def eval(self):
        return self.value


class Int(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.value = 0
        self.kind = "integer"

    def apply(self):
        try:
            self.value = int(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Integer")
            sys.exit(1)

    def eval(self):
        return self.value


class Float(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.value = 0.0
        self.kind = "float"

    def apply(self):
        try:
            self.value = float(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Float")
            sys.exit(1)

    def eval(self):
        return self.value


class Str(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.value = ""
        self.kind = "string"

    def apply(self):
        try:
            self.value = str(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become String")
            sys.exit(1)

    def eval(self):
        return self.value


class Boolean(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.value = True
        self.kind = "boolean"

    def apply(self):
        try:
            self.value = bool(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Float")
            sys.exit(1)

    def eval(self):
        return self.value


class Type(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "string"

    def eval(self):
        return self.exp.kind
