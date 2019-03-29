from rply.token import BaseBox
import sys


class UniqueOp(BaseBox):
    def __init__(self, exp):
        self.exp = exp
    def eval(self):
        return self.exp.eval()


class Increment(UniqueOp):
    def apply(self):
        try:
            self.exp.value += 1
            return self.exp
        except:
            try:
                self.exp.increment()
                return self.exp
            except:
                print("Operation impossible : \n - Value :", self.exp.eval(),
                      "\n - Type :", self.exp.kind,
                      "\n - Operation : Increase")
                sys.exit(1)


class Decrement(UniqueOp):
    def apply(self):
        try:
            self.exp.value -= 1
            return self.exp
        except:
            try:
                self.exp.decrement()
                return self.exp
            except:
                print("Operation impossible : \n - Value :", self.exp.eval(),
                      "\n - Type :", self.exp.kind,
                      "\n - Operation : Decrease")
                sys.exit(1)
