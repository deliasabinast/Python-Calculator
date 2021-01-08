# lex/yacc calculator
# supports +, -, *, /, ^^, sin, cos, tg, ctg, rad, log + new one @
# bibliografie: https://www.dabeaz.com/ply/ply.html
#               https://www.youtube.com/watch?v=Hh49BXmHxX8 (pretty much the same stuff)

import math

import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'LP',
    'RP',
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'POW',
    'INT',
    'FLOAT',
    'FUNCTION'
]

t_LP = r'\('
t_RP = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_POW = r'\^\^'




def t_FUNCTION(t):
    r'sin|cos|tan|ctg|log|rad|@'
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

t_ignore  = ' \t'

def t_error(t): #syntax error
    print("This is t_error")
    t.lexer.skip(1)


precedence = (
    ('left','PLUS','MINUS'),
    ('left','MUL','DIV'),
    ('left','POW'),
    ('right','UMINUS')
)


def p_calc(p):  # start
    '''
    calc : expression
        | empty
    '''
    print(evaluate(p[1]))


def p_function(p):  # sin cos tg ctg rad log
    '''
    expression : FUNCTION LP expression RP
    '''
    p[0] = (p[1],p[3])  # ex: sin, 1    sin(1)


def p_expression_parentheses(p): #parentheses case, ex: (1+2)*3
    '''
    expression : LP expression RP
    '''
    p[0] = p[2]
    # print(p[0])
    # print(p[2])


def p_expression(p):  # creates a "tree" -> basic operations
    '''
    expression : expression POW expression
                | expression MUL expression
                | expression DIV expression
                | expression PLUS expression
                | expression MINUS expression
    '''
    p[0] = (p[2],p[1],p[3])
    print(p)


def p_expression_uminus(p): #minus in front of an expression
    '''
    expression : MINUS expression %prec UMINUS
    '''
    p[0] = -p[2]


def p_expression_number(p):  # single number
    '''
    expression : INT
                | FLOAT
    '''
    p[0] = p[1]

def p_error(p):  #parsing error
    print("This is p_error")


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


parser = yacc.yacc()
lexer = lex.lex()


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
        elif p[0] == '^^':
            return pow(evaluate(p[1]),evaluate(p[2]))
        elif p[0] == '@':
            return pow(evaluate(p[1]),3/2)   #the new function, sqrt(something ^ 3) = something ^ (3/2)
        elif p[0] == 'sin':
            print(p[1])
            print("i do stuff")
            return math.sin(evaluate(p[1]))
        elif p[0] == 'cos':
            return math.cos(evaluate(p[1]))
        elif p[0] == 'tg':
            return math.tan(evaluate(p[1]))
        elif p[0] == 'ctg':
            return 1 / (math.tan(evaluate(p[1])))
        elif p[0] == 'rad':
            return math.sqrt(evaluate(p[1]))
        elif p[0] == 'log':
            return math.log(evaluate(p[1]),2)
    else:
        return p


while True:
    try:
        expr = input('>> ')
    except EOFError:
        break
    parser.parse(expr)
