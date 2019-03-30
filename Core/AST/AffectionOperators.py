from rply.token import BaseBox
import sys


class AffectionOperator(BaseBox):
    def __init__(self, exp, right):
        self.exp = exp
        self.right = right

    def eval(self):
        return self.exp.eval()


class SumAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value += self.right.eval()
            return self.exp
        except:
            try:
                self.exp.sumaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Addition affection")
                sys.exit(1)


class SubAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value -= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.subaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Subtraction affection")
                sys.exit(1)


class MulAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value *= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.mulaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Multiplication affection")
                sys.exit(1)


class DivAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value /= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.divaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Division affection")
                sys.exit(1)


class DivEuAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value //= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.diveuaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Euclidean Division affection")
                sys.exit(1)


class ModAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value %= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.modaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Modulo affection")
                sys.exit(1)


class PowAffector(AffectionOperator):
    def apply(self):
        try:
            self.exp.value **= self.right.eval()
            return self.exp
        except:
            try:
                self.exp.powaff(self.right)
                return self.exp
            except:
                print("Operation impossible : \n - Values :", self.exp.eval(), "|", self.right.eval(),
                      "\n - Types :", self.exp.kind, "|", self.right.kind,
                      "\n - Operation : Power affection")
                sys.exit(1)
