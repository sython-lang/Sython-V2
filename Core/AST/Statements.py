from rply.token import BaseBox


class Statement(BaseBox):
    def __init__(self, exp):
        self.exp = exp

    def eval(self):
        return self.exp.eval()

    @staticmethod
    def gettokentype():
        return "statement"


class StatementList(BaseBox):
    def __init__(self, statement, sl=None):
        if sl is not None:
            self.statements = sl.statements
        else:
            self.statements = []
        if statement is not None:
            self.statements.append(statement)

    def eval(self):
        value = None
        print(self.statements)
        for i in self.statements:
            i.eval()
        return value

    @staticmethod
    def gettokentype():
        return "statementlist"
