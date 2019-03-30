from rply import ParserGenerator
import sys

from Core.AST.BinaryOperators import Sum, Sub, Mul, Div, Mod, Pow
from Core.AST.AffectionOperators import SumAffector, SubAffector, MulAffector, DivAffector, ModAffector, PowAffector
from Core.AST.Expressions import ExpressionBase, Nothing
from Core.AST.Functions import Print, Input, Int, Str, Float, Type, Boolean
from Core.AST.Variables import Variable, Variables
from Core.AST.UniqueOperators import Increment, Decrement


class Parser:
    def __init__(self, tokens):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            tokens,
            precedence=[
                ('left', ['EGAL']),
                ('left', ['SUMAFF', 'SUBAFF']),
                ('left', ['MULAFF', 'DIVAFF', 'MODAFF']),
                ('left', ['POWAFF']),
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
            return p[2]

        @self.pg.production('expression : INT OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : FLOATF OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : BOOL OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : STR OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : TYPE OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('expression : ENTER OPEN_PAREN STRING CLOSE_PAREN')
        def programfunc1(p):
            func = p[0]
            exp = p[2]
            if func.gettokentype() == "INT":
                i = Int(exp)
                i.apply()
                return i
            elif func.gettokentype() == "FLOAT":
                i = Float(exp)
                i.apply()
                return i
            elif func.gettokentype() == "BOOLEAN":
                i = Boolean(exp)
                i.apply()
                return i
            elif func.gettokentype() == "STR":
                i = Str(exp)
                i.apply()
                return i
            elif func.gettokentype() == "TYPE":
                return Type(exp)
            elif func.gettokentype() == "PRINT":
                i = Print(exp)
                i.apply()
                return i
            else:
                i = Input(exp.value)
                i.apply()
                return i

        @self.pg.production('expression : EXIT OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : ENTER OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : PRINT OPEN_PAREN CLOSE_PAREN')
        def programfunc0(p):
            func = p[0]
            if func.gettokentype() == "EXIT":
                sys.exit(0)
            elif func.gettokentype() == "ENTER":
                i = Input()
                i.apply()
                return i
            else:
                i = Print()
                i.apply()
                return i

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
                else:
                    value = Decrement(var.exp)
                if value.eval() is not None:
                    var = Variable(p[0].value, value.apply())
                    self.var.add(var)
                return value
            else:
                print("Variable not declared : \n - Name :", p[0].value)
                sys.exit(1)

        @self.pg.production('expression : IDENTIFIER SUMAFF expression')
        @self.pg.production('expression : IDENTIFIER SUBAFF expression')
        @self.pg.production('expression : IDENTIFIER MULAFF expression')
        @self.pg.production('expression : IDENTIFIER DIVAFF expression')
        @self.pg.production('expression : IDENTIFIER MODAFF expression')
        @self.pg.production('expression : IDENTIFIER POWAFF expression')
        def affectionop(p):
            var = self.var.get(p[0].value)
            op = p[1]
            if var is not None:
                value = Nothing()
                if op.gettokentype() == 'SUMAFF':
                    value = SumAffector(var.exp, p[2])
                elif op.gettokentype() == 'SUBAFF':
                    value = SubAffector(var.exp, p[2])
                elif op.gettokentype() == 'MULAFF':
                    value = MulAffector(var.exp, p[2])
                elif op.gettokentype() == 'MODAFF':
                    value = ModAffector(var.exp, p[2])
                elif op.gettokentype() == 'POWAFF':
                    value = PowAffector(var.exp, p[2])
                else:
                    value = DivAffector(var.exp, p[2])
                if value.eval() is not None:
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
        @self.pg.production('expression : BOOLEAN')
        def expression(p):
            if p[0].gettokentype() == 'FLOAT':
                return ExpressionBase(float(p[0].value), "float")
            elif p[0].gettokentype() == 'STRING':
                return ExpressionBase(str(p[0].value)[1:-1], "string")
            elif p[0].gettokentype() == 'BOOLEAN':
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
