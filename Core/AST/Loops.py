from rply.token import BaseBox


class Loop(BaseBox):
    def __init__(self, number, statementlist):
        self.number = number
        self.statementlist = statementlist

    def eval(self):
        for i in range(self.number-1):
            self.statementlist.eval()
        return self.statementlist.eval()

    @staticmethod
    def gettokentype():
        return 'statement'


class While(BaseBox):
    def __init__(self, condition, statementlist):
        self.condition = condition
        self.statementlist = statementlist

    def eval(self):
        while bool(self.condition.eval()):
            self.statementlist.eval()
        return None

    @staticmethod
    def gettokentype():
        return 'statement'