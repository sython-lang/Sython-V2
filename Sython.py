from Core.lexer import Lexer
from Core.parser import Parser
import sys

dico = {
    # Comments
    'COMMENT': r'#.*',

    # Types
    'STRING': r'(\"([^\\\n]|(\\.))*?\")|(\'([^\\\n]|(\\.))*?\')',
    'BOOLEAN': r'(true)|(false)',
    'FLOAT': r'-?\d+.\d+',
    'INTEGER': r'-?\d+',

    # Functions
    'PRINT': r'print',
    'EXIT': r'exit',
    'ENTER': r'enter',
    'INT': r'int',
    'FLOATF': r'float',
    'STR': r'str',
    'TYPE': r'type',
    'BOOL': r'boolean',

    # Operators on variables
    'INCREMENT': r'\+\+',
    'DECREMENT': r'\-\-',
    'SUMAFF': r'\+\=',
    'SUBAFF': r'\-\=',
    'MULAFF': r'\*\=',
    'DIVAFF': r'\/\=',
    'DIVEUAFF': r'\/\/\=',
    'MODAFF': r'\%\=',
    'POWAFF': r'\^\=',

    # Binary Operators on expressions
    'SUM': r'\+',
    'SUB': r'\-',
    'MUL': r'\*',
    'DIV': r'\/',
    'DIVEU': r'\/\/',
    'MOD': r'\%',
    'POW': r'\^',

    # For variables
    'EGAL': r'\=',
    'IDENTIFIER': r"[a-zA-Z][a-zA-Z0-9]*",

    # Others
    'OPEN_PAREN': r'\(',
    'CLOSE_PAREN': r'\)'
}

tokens = []
values = []
for k, v in dico.items():
    tokens.append(k)
    values.append(v)

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
