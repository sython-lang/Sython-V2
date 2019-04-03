from rply import ParserGenerator
import sys

from Core.AST.BinaryOperators import Sum, Sub, Mul, Div, Mod, Pow, DivEu
from Core.AST.AffectionOperators import SumAffector, SubAffector, DivEuAffector, MulAffector, DivAffector,\
    ModAffector, PowAffector
from Core.AST.Expressions import ExpressionBase, Nothing
from Core.AST.Functions import Print, Input, Int, Str, Float, Type, Boolean
from Core.AST.Variables import Variable, Variables
from Core.AST.UniqueOperators import Increment, Decrement
from Core.AST.Comparators import Egal, Less, LessOrEgal, More, MoreOrEgal
from Core.AST.Conditions import If, IfElse, Else
from Core.AST.Statements import Statement, StatementList


class Parser:
    def __init__(self, tokens):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            tokens,
            precedence=[
                ('left', ['NEWLINE']),
                ('left', ['EGAL']),
                ('left', ['IS', 'LESS', 'MORE', 'LESSE', 'MOREE']),
                ('left', ['SUMAFF', 'SUBAFF']),
                ('left', ['MULAFF', 'DIVAFF', 'DIVEUAFF', 'MODAFF']),
                ('left', ['POWAFF']),
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV', 'DIVEU', 'MOD']),
                ('left', ['POW'])
            ]
        )
        self.var = Variables()

    def parse(self):
        @self.pg.production('program : statementlist')
        def program(p):
            return p[0].eval()

        @self.pg.production('statementlist : statementlist NEWLINE statement')
        @self.pg.production('statementlist : statementlist NEWLINE if_statement')
        @self.pg.production('statementlist : statementlist NEWLINE ifelse_statement')
        def statementlistexp(p):
            return StatementList(p[2], p[0])

        @self.pg.production('statementlist : statement')
        @self.pg.production('statementlist : if_statement')
        @self.pg.production('statementlist : ifelse_statement')
        @self.pg.production('statementlist : statementlist NEWLINE')
        def statementlist(p):
            if p[0].gettokentype() == 'statement':
                return StatementList(p[0])
            else:
                return StatementList(None, p[0])

        @self.pg.production('if_statement : IF expression OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def ifexp(p):
            return If(p[1], p[4])

        @self.pg.production('if_statement : IF expression NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def ifexp2(p):
            return If(p[1], p[5])

        @self.pg.production('else_statement : ELSE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def elseexp(p):
            return Else(p[3])

        @self.pg.production('else_statement : ELSE NEWLINE OPEN_CRO NEWLINE statementlist NEWLINE CLOSE_CRO')
        def elseexp3(p):
            return Else(p[4])

        @self.pg.production('ifelse_statement : if_statement else_statement')
        def ifelse(p):
            return IfElse(p[0], p[1])

        # @self.pg.production('ifelse_statement : if_statement NEWLINE else_statement')
        # def ifelse2(p):
        #     return IfElse(p[0], p[2])

        @self.pg.production('statement : expression COMMENT')
        @self.pg.production('statement : expression')
        def statement(p):
            return Statement(p[0])

        @self.pg.production('statement : COMMENT')
        def statement(p):
            return None

        @self.pg.production('expression : IDENTIFIER EGAL expression')
        def programvar(p):
            var = Variable(p[0].value, p[2].eval(), p[2].kind)
            self.var.add(var)
            return ExpressionBase(var.eval(), p[2].kind)

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
                return Int(exp)
            elif func.gettokentype() == "FLOATF":
                return Float(exp)
            elif func.gettokentype() == "BOOL":
                return Boolean(exp)
            elif func.gettokentype() == "STR":
                return Str(exp)
            elif func.gettokentype() == "TYPE":
                return Type(exp)
            elif func.gettokentype() == "PRINT":
                return Print(exp)
            else:
                return Input(exp.value)

        @self.pg.production('expression : EXIT OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : ENTER OPEN_PAREN CLOSE_PAREN')
        @self.pg.production('expression : PRINT OPEN_PAREN CLOSE_PAREN')
        def programfunc0(p):
            func = p[0]
            if func.gettokentype() == "EXIT":
                sys.exit(0)
            elif func.gettokentype() == "ENTER":
                return Input()
            else:
                return Print()

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def expressionparen(p):
            return p[1]

        @self.pg.production('expression : IDENTIFIER INCREMENT')
        @self.pg.production('expression : IDENTIFIER DECREMENT')
        def uniqueop(p):
            var = self.var.get(p[0].value)
            if var is not None:
                if p[1].gettokentype() == "INCREMENT":
                    value = Increment(ExpressionBase(var.value, var.kind))
                else:
                    value = Decrement(ExpressionBase(var.value, var.kind))
                value = value.eval()
                if value is not None:
                    var = Variable(p[0].value, value, var.kind)
                    self.var.add(var)
                    return var
                return Nothing()
            else:
                print("Variable not declared : \n - Name :", p[0].value)
                sys.exit(1)

        @self.pg.production('expression : IDENTIFIER SUMAFF expression')
        @self.pg.production('expression : IDENTIFIER SUBAFF expression')
        @self.pg.production('expression : IDENTIFIER MULAFF expression')
        @self.pg.production('expression : IDENTIFIER DIVAFF expression')
        @self.pg.production('expression : IDENTIFIER MODAFF expression')
        @self.pg.production('expression : IDENTIFIER POWAFF expression')
        @self.pg.production('expression : IDENTIFIER DIVEUAFF expression')
        def affectionop(p):
            var = self.var.get(p[0].value)
            op = p[1]
            if var is not None:
                if op.gettokentype() == 'SUMAFF':
                    value = SumAffector(ExpressionBase(var.value, var.kind), p[2])
                elif op.gettokentype() == 'SUBAFF':
                    value = SubAffector(ExpressionBase(var.value, var.kind), p[2])
                elif op.gettokentype() == 'MULAFF':
                    value = MulAffector(ExpressionBase(var.value, var.kind), p[2])
                elif op.gettokentype() == 'MODAFF':
                    value = ModAffector(ExpressionBase(var.value, var.kind), p[2])
                elif op.gettokentype() == 'POWAFF':
                    value = PowAffector(ExpressionBase(var.value, var.kind), p[2])
                elif op.gettokentype() == 'DIVEUAFF':
                    value = DivEuAffector(ExpressionBase(var.value, var.kind), p[2])
                else:
                    value = DivAffector(ExpressionBase(var.value, var.kind), p[2])
                value = value.eval()
                if value is not None:
                    var = Variable(p[0].value, value, var.kind)
                    self.var.add(var)
                    return var
                return Nothing()
            else:
                print("Variable not declared : \n - Name :", p[0].value)
                sys.exit(1)

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression POW expression')
        @self.pg.production('expression : expression DIVEU expression')
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
            elif operator.gettokentype() == 'DIVEU':
                return DivEu(left, right)
            else:
                return Div(left, right)

        @self.pg.production('expression : expression IS expression')
        @self.pg.production('expression : expression LESS expression')
        @self.pg.production('expression : expression LESSE expression')
        @self.pg.production('expression : expression MORE expression')
        @self.pg.production('expression : expression MOREE expression')
        def comparators(p):
            c = p[1]
            e1 = p[0]
            e2 = p[2]
            if c.gettokentype() == "IS":
                i = Egal(e1, e2)
            elif c.gettokentype() == "LESS":
                i = Less(e1, e2)
            elif c.gettokentype() == "MORE":
                i = More(e1, e2)
            elif c.gettokentype() == "LESSE":
                i = LessOrEgal(e1, e2)
            else:
                i = MoreOrEgal(e1, e2)
            return ExpressionBase(i.eval(), "boolean")

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
        @self.pg.production('expression : IDENTIFIER')
        def expression(p):
            if p[0].gettokentype() == 'FLOAT':
                return ExpressionBase(float(p[0].value), "float")
            elif p[0].gettokentype() == 'STRING':
                return ExpressionBase(str(p[0].value)[1:-1], "string")
            elif p[0].gettokentype() == 'BOOLEAN':
                if p[0].value == "false":
                    return ExpressionBase(False, "boolean")
                return ExpressionBase(True, "boolean")
            elif p[0].gettokentype() == 'IDENTIFIER':
                var = self.var.get(p[0].value)
                if var is not None:
                    return var.eval()
                else:
                    print("Variable not declared : \n - Name :", p[0].value)
                    sys.exit(1)
            else:
                return ExpressionBase(int(p[0].value), "integer")

        @self.pg.error
        def error_handle(token):
            print("Syntax unexcepted : \n - Type :", token.gettokentype(),
                  "\n - Position : Line", token.getsourcepos().lineno, "| Column :", token.getsourcepos().colno,
                  "\n - Token :", token.value)
            sys.exit(1)

    def get_parser(self):
        return self.pg.build()
