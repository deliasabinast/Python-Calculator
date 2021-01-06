# lex/yacc calculator
# supports +, -, *, /, ^^, sin, cos, tg, ctg, rad, log
import ply.lex as lex
import ply.yacc as yacc
import math
import sys

tokens = [
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'POW',
    'FUNCTION',
    'INT',
    'FLOAT',
    'LPAREN',
    'RPAREN'
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_POW = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_FUNCTION(t):
    r'sin|cos|tan|log|rad'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = r' /t'


def t_error(t):
    print("Syntax error")
    t.lexer.skip(1)



lexer = lex.lex()
# data = 'sin'
# lexer.input(data)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('left', 'POW')
)

def p_calc(p):   #start
    '''
    calc : expression
        | empty
    '''
    print(evaluate(p[1]))

def p_expression(p):   # creates a "tree" -> basic operations
    '''
    expression : expression POW expression
                | expression MUL expression
                | expression DIV expression
                | expression PLUS expression
                | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_number(p):   #single number
    '''
    expression : INT
                | FLOAT
    '''
    p[0]=p[1]

def p_error(p):
    print("Syntax error")

def p_empty(p):
    '''
    empty :
    '''
    p[0]=None

parser = yacc.yacc()

def evaluate(p):
    if type(p) == tuple:
        if p[0] == '+':
            return evaluate(p[1]) + evaluate(p[2])
        elif p[0] == '-':
            return evaluate(p[1]) - evaluate(p[2])
        elif p[0] == '*':
            return evaluate(p[1]) * evaluate(p[2])
        elif p[0] == '/':
            return evaluate(p[1]) / evaluate(p[2])
        elif p[0] == '^':
            return pow(evaluate(p[1]), evaluate(p[2]))

    else:
        return p



while True:
    try:
        expr = input('>> ')
    except EOFError:
        break
    parser.parse(expr)

        # Tokenize
        # while True:
        #     tok = lexer.token()
        #     if not tok:
        #         break  # No more input
        #     print(tok)






