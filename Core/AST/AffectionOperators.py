from rply.token import BaseBox
import sys


class AffectionOperator(BaseBox):
    def __init__(self, var, right):
        self.right = right
        self.var = var
        self.kind = var.kind


class SumAffector(AffectionOperator):
    def eval(self):
        if self.right.kind == "string":
            self.kind = "string"

        try:
            self.var.value = self.var.value + self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().sum(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Addition affection")
                sys.exit(1)


class SubAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value - self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().sub(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Subtraction affection")
                sys.exit(1)


class MulAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value * self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().mul(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Multiplication affection")
                sys.exit(1)


class DivAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value / self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().div(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Division affection")
                sys.exit(1)


class DivEuAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value // self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().diveu(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Euclidean Division affection")
                sys.exit(1)


class ModAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value % self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().mod(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Modulo affection")
                sys.exit(1)


class PowAffector(AffectionOperator):
    def eval(self):
        try:
            self.var.value = self.var.value ** self.right.eval()
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().pow(self.right.eval())
                return self.var.value
            except:
                print("Operation impossible : \n - Values :", self.var.value, "|", self.right.eval(),
                      "\n - Types :", self.var.kind, "|", self.right.kind,
                      "\n - Operation : Power affection")
                sys.exit(1)
