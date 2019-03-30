from Core.lexer import Lexer
from Core.parser import Parser
import sys

tokens = ['PRINT', 'EXIT', 'ENTER', 'INT', 'FLOAT', 'STR',
          'TYPE', 'BOOLEAN', 'BOOL', 'FLOAT',
          'INCREMENT', 'DECREMENT', 'INTEGER', 'SUMAFF',
          'SUBAFF', 'MULAFF', 'DIVAFF', 'MODAFF', 'POWAFF',
          'OPEN_PAREN', 'CLOSE_PAREN', 'SUM',
          'SUB', 'MUL', 'DIV', 'MOD', 'POW', 'EGAL',
          'STRING', 'IDENTIFIER',
          'COMMENT']
values = [r'show', r'exit', r'enter', r'int', r'float', r'str',
          r'type', r'bool', r'(true)|(false)', r'-?\d+.\d+',
          r'\+\+', r'\-\-', r'-?\d+', r'\+\=',
          r'\-\=', r'\*\=', r'\/\=', r'\%\=', r'\^=',
          r'\(', r'\)', r'\+',
          r'\-', r'\*', r'\/', r'\%', r'\^', r'\=',
          r'(\"([^\\\n]|(\\.))*?\")|(\'([^\\\n]|(\\.))*?\')', r"[a-zA-Z][a-zA-Z0-9]*",
          r'\#.*']

lexer = Lexer(tokens, values).get_lexer()
pg = Parser(tokens)
pg.parse()
parser = pg.get_parser()

if len(sys.argv) >= 2:
    try:
        with open(sys.argv[1]) as f:
            text_input = f.readlines()
            for i in text_input:
                if i != "":
                    tokens = lexer.lex(i)
                    parser.parse(tokens).eval()
    except IOError:
        pass
else:
    launched = True
    while launched:
        text_input = input(">>> ")
        tokens = lexer.lex(text_input)
        # print(list(tokens)) # ONLY TO DEBUG : This function shows tokens (make crash the program)
        result = parser.parse(tokens).eval()
        if result is not None:
            print(result)
