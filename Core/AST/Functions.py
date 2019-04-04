from rply.token import BaseBox
from Core.AST.Expressions import ExpressionBase
import sys


class CanBe(BaseBox):
    def __init__(self, exp, value):
        self.value = value
        self.exp = exp
        self.kind = "boolean"

    def eval(self):
        if self.value == "int":
            try:
                int(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "float":
            try:
                float(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "str":
            try:
                str(self.exp.eval())
                return True
            except:
                return False
        elif self.value == "bool":
            try:
                bool(self.exp.eval())
                return True
            except:
                return False
        else:
            print("Invalid Type : \n - Operation : CanBe Function",
                  "\n - Type : ", self.value)
            sys.exit(1)


class Print(BaseBox):
    def __init__(self, value=ExpressionBase("", "string")):
        self.value = value
        self.kind = "string"

    def eval(self):
        print(self.value.eval())
        return self.value.eval()


class Input(BaseBox):
    def __init__(self, text=""):
        self.text = text
        self.kind = "string"

    def eval(self):
        return input(self.text[1:-1])


class Int(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "integer"

    def eval(self):
        try:
            return int(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Integer")
            sys.exit(1)


class Float(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "float"

    def eval(self):
        try:
            return float(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Float")
            sys.exit(1)


class Str(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "string"

    def eval(self):
        try:
            return str(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become String")
            sys.exit(1)


class Boolean(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "boolean"

    def eval(self):
        try:
            return bool(self.exp.eval())
        except:
            print("Operation impossible : \n - Value :", self.exp.eval(),
                  "\n - Type :", self.exp.kind,
                  "\n - Operation : Become Float")
            sys.exit(1)


class Type(BaseBox):
    def __init__(self, exp):
        self.exp = exp
        self.kind = "string"

    def eval(self):
        return self.exp.kind
