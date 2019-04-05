from rply.token import BaseBox


class If(BaseBox):
    def __init__(self, condition, statementlist):
        self.condition = condition
        self.statementlist = statementlist

    def eval(self):
        if bool(self.condition.eval()):
            self.statementlist.eval()

    @staticmethod
    def gettokentype():
        return 'statement'


class Else(BaseBox):
    def __init__(self, statementlist):
        self.statementlist = statementlist


class IfElse(BaseBox):
    def __init__(self, ifexp, elseexp):
        self.condition = ifexp.condition
        self.statementlistif = ifexp.statementlist
        self.statementlistelse = elseexp.statementlist

    def eval(self):
        if bool(self.condition.eval()):
            self.statementlistif.eval()
        else:
            self.statementlistelse.eval()

    @staticmethod
    def gettokentype():
        return 'statement'
