from rply.token import BaseBox
import sys


class AffectionOperator(BaseBox):
    def __init__(self, exp, right):
        self.exp = exp
        self.right = right
        if self.right.kind == "string" or self.exp.kind == "string":
            self.kind = "string"
        else:
            self.kind = self.exp.kind


class SumAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value += self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.sumaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Addition affection")
                sys.exit(1)


class SubAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value -= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.subaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Subtraction affection")
                sys.exit(1)


class MulAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value *= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.mulaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Multiplication affection")
                sys.exit(1)


class DivAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value /= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.divaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Division affection")
                sys.exit(1)


class DivEuAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value //= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.diveuaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Euclidean Division affection")
                sys.exit(1)


class ModAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value %= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.modaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Modulo affection")
                sys.exit(1)


class PowAffector(AffectionOperator):
    def eval(self):
        try:
            self.exp.value **= self.right.eval()
            return self.exp.value
        except:
            try:
                self.exp.powaff(self.right)
                return self.exp.value
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Power affection")
                sys.exit(1)
