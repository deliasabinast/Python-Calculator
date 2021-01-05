# lex/yacc calculator
# supports +, -, *, /, ^^, sin, cos, tg, ctg, rad, log
import ply.lex as lex

tokens = [
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'POW',
    'FUNCTION',
    'INT',
    'FLOAT',
    'VAR',
    'LPAREN',
    'RPAREN'
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_POW = r'\^^'
t_LPAREN = r'\('
t_RPAREN = r'\)'

"""
#t_LOG = r'\log'
t_SIN = r'\sin'
t_COS = r'\cos'
t_TG = r'\tan'
#t_CTG = r'\ctan'
t_SQRT = r'\rad'
"""

"""

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t
      """

def t_FUNCTION(t):
    r'sin|cos|tan|log|rad'
    return t

def t_FLOAT(t):
    r'[+-]?([1-9][0-9]*\.[0-9]+)|(0\.[0-9]+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[+-]?[1-9][0-9]*|0'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = r' /t'


def t_error(t):
    print("Syntax error")
    t.lexer.skip(1)


# lexer = lex.lex()

# def p_function_exp(p):
#     'function : expression PLUS function'
#     p[0] = p[1] + p[3]



lexer = lex.lex()
data = 'sin'
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
