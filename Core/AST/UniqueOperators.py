from rply.token import BaseBox
import sys


class UniqueOp(BaseBox):
    def __init__(self, var):
        self.var = var


class Increment(UniqueOp):
    def eval(self):
        try:
            self.var.value = self.var.value + 1
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().increment()
                return self.var.value
            except:
                print("Operation impossible : \n - Value :", self.var.value,
                      "\n - Type :", self.var.kind,
                      "\n - Operation : Increase")
                sys.exit(1)


class Decrement(UniqueOp):
    def eval(self):
        try:
            self.var.value = self.var.value - 1
            return self.var.value
        except:
            try:
                self.var.value = self.var.expression().decrement()
                return self.var.value
            except:
                print("Operation impossible : \n - Value :", self.var.value,
                      "\n - Type :", self.var.kind,
                      "\n - Operation : Decrease")
                sys.exit(1)
