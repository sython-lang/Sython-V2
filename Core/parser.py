from rply import ParserGenerator
import sys

from Core.AST.BinaryOperators import Sum, Sub, Mul, Div, Mod, Pow
from Core.AST.Expressions import ExpressionBase, Nothing
from Core.AST.Functions import Print, Input
from Core.AST.Variables import Variable, Variables
from Core.AST.UniqueOperators import Increment, Decrement


class Parser:
    def __init__(self, tokens):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            tokens,
            precedence=[
                ('left', ['EGAL']),
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV', 'MOD']),
                ('left', ['POW'])
            ]
        )
        self.var = Variables()

    def parse(self):
        @self.pg.production('program : expression')
        def programexp(p):
            return p[0]

        @self.pg.production('program : expression COMMENT')
        def programexpcomment(p):
            return p[0]

        @self.pg.production('program : COMMENT')
        def programcomment(p):
            return Nothing()

        @self.pg.production('expression : IDENTIFIER EGAL expression')
        def programvar(p):
            var = Variable(p[0].value, p[2])
            self.var.add(var)
            return var

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def programprint(p):
            return Print(p[2])

        @self.pg.production('expression : EXIT OPEN_PAREN CLOSE_PAREN')
        def programexit(p):
            sys.exit(0)

        @self.pg.production('expression : ENTER OPEN_PAREN CLOSE_PAREN')
        def programenter(p):
            return Input()

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expressionparen(p):
            return p[1]

        @self.pg.production('expression : IDENTIFIER INCREMENT')
        @self.pg.production('expression : IDENTIFIER DECREMENT')
        def uniqueop(p):
            var = self.var.get(p[0].value)
            if var is not None:
                value = Nothing()
                if p[1].gettokentype() == "INCREMENT":
                    value = Increment(var.exp)
                    var = Variable(p[0].value, value.apply())
                    self.var.add(var)
                else:
                    value = Decrement(var.exp)
                    var = Variable(p[0].value, value.apply())
                    self.var.add(var)
                return value
            else:
                print("Variable not declared : \n - Name :", p[0].value)
                sys.exit(1)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression POW expression')
        def binaryop(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'MOD':
                return Mod(left, right)
            elif operator.gettokentype() == 'POW':
                return Pow(left, right)
            else:
                return Div(left, right)

        @self.pg.production('expression : SUB expression')
        @self.pg.production('expression : SUM expression')
        def uniqueop(p):
            ope = p[0]
            exp = p[1]
            if ope.gettokentype() == 'SUM':
                return Sum(ExpressionBase(0, "integer"), exp)
            else:
                return Sub(ExpressionBase(0, "integer"), exp)

        @self.pg.production('expression : INTEGER')
        @self.pg.production('expression : FLOAT')
        @self.pg.production('expression : STRING')
        @self.pg.production('expression : BOOL')
        def expression(p):
            if p[0].gettokentype() == 'FLOAT':
                return ExpressionBase(float(p[0].value), "float")
            elif p[0].gettokentype() == 'STRING':
                return ExpressionBase(str(p[0].value)[1:-1], "string")
            elif p[0].gettokentype() == 'BOOL':
                if p[0].value == "false":
                    return ExpressionBase(False, "boolean")
                return ExpressionBase(True, "boolean")
            else:
                return ExpressionBase(int(p[0].value), "integer")

        @self.pg.production('expression : IDENTIFIER')
        def variable(p):
            var = self.var.get(p[0].value)
            if var is not None:
                return var.exp
            else:
                print("Variable not declared : \n - Name :", p[0].value)
                sys.exit(1)

        @self.pg.error
        def error_handle(token):
            print("Syntax unexcepted : \n - Type :", token.gettokentype(),
                  "\n - Position : Line", token.getsourcepos().lineno, "| Column :", token.getsourcepos().colno,
                  "\n - Token :", token.value)
            sys.exit(1)

    def get_parser(self):
        return self.pg.build()
