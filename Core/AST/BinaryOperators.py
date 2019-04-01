from rply.token import BaseBox
import sys


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        if self.right.kind == "string" or self.left.kind == "string":
            self.kind = "string"
        else:
            self.kind = self.left.kind


class Sum(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() + self.right.eval()
        except:
            try:
                return self.left.sum(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Addition")
                sys.exit(1)


class Sub(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() - self.right.eval()
        except:
            try:
                return self.left.sub(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Subtraction")
                sys.exit(1)


class Mul(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() * self.right.eval()
        except:
            try:
                return self.left.mul(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Multiplication")
                sys.exit(1)


class Div(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() / self.right.eval()
        except:
            try:
                return self.left.div(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Division")
                sys.exit(1)


class DivEu(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() // self.right.eval()
        except:
            try:
                return self.left.diveu(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Euclidean Division")
                sys.exit(1)


class Pow(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() ** self.right.eval()
        except:
            try:
                return self.left.pow(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Power")
                sys.exit(1)


class Mod(BinaryOp):
    def eval(self):
        try:
            return self.left.eval() % self.right.eval()
        except:
            try:
                return self.left.mod(self.right)
            except:
                print("Operation impossible : \n - Values :", self.left.eval(), "|", self.right.eval(),
                      "\n - Types :", self.left.kind, "|", self.right.kind,
                      "\n - Operation : Modulo")
                sys.exit(1)
