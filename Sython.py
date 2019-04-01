from Core.lexer import Lexer
from Core.parser import Parser
import sys

dico = {
    # Comments
    'COMMENT': r'#.*',
    'NEWLINE': r'\n+',

    # Types
    'STRING': r'(\"([^\\\n]|(\\.))*?\")|(\'([^\\\n]|(\\.))*?\')',
    'BOOLEAN': r'(true)|(false)',
    'FLOAT': r'-?\d+.\d+',
    'INTEGER': r'-?\d+',

    # Conditions
    'ELSEIF': r'else if',
    'IF': r'if',
    'OPEN_CRO': r'\{',
    'CLOSE_CRO': r'\}',
    'ELSE': r'else',

    # Functions
    'PRINT': r'show',
    'EXIT': r'exit',
    'ENTER': r'enter',
    'INT': r'int',
    'FLOATF': r'float',
    'STR': r'str',
    'TYPE': r'type',
    'BOOL': r'boolean',

    # Comparators
    'IS': r'\=\=',
    'LESSE': r'\<\=',
    'MOREE': r'\>\=',
    'LESS': r'\<',
    'MORE': r'\>',

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
            text_input = f.read()
            tokens = lexer.lex(text_input)
            # b = lexer.lex(text_input) # ONLY TO DEBUG
            # print(list(b))  # ONLY TO DEBUG
            parser.parse(tokens)
    except IOError:
        pass
else:
    launched = True
    while launched:
        text_input = input(">>> ")
        tokens = lexer.lex(text_input)
        # b = lexer.lex(text_input) # ONLY TO DEBUG
        # print(list(b))  # ONLY TO DEBUG
        result = parser.parse(tokens)
        if result is not None:
            print(result)
