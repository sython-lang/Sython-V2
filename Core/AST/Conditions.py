from rply.token import BaseBox


class Conditions(BaseBox):
    def __init__(self, condition, expression):
        self.condition = condition
        self.expression = expression


class If(Conditions):
    def eval(self):
        if bool(self.condition.eval()):
            return self.expression.eval()
        else:
            return None

