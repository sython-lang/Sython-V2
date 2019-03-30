from rply.token import BaseBox
from Core.AST.Expressions import ExpressionBase
import sys


class Comparators(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = False

    def eval(self):
        return ExpressionBase(self.value, "boolean")


class Egal(Comparators):
    def apply(self):
        if self.left.eval() == self.right.eval():
            self.value = True
        else:
            self.value = False


class Less(Comparators):
    def apply(self):
        if self.left.eval() < self.right.eval():
            self.value = True
        else:
            self.value = False


class More(Comparators):
    def apply(self):
        if self.left.eval() > self.right.eval():
            self.value = True
        else:
            self.value = False


class LessOrEgal(Comparators):
    def apply(self):
        if self.left.eval() <= self.right.eval():
            self.value = True
        else:
            self.value = False


class MoreOrEgal(Comparators):
    def apply(self):
        if self.left.eval() >= self.right.eval():
            self.value = True
        else:
            self.value = False
