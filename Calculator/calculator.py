#lex/yacc calculator
#supports +, -, *, /, ^^, sin, cos, tg, ctg, rad, log
import math
import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'PLUS',
    'MINUS',
    'DIV',
    'MUL',
    'SQRT',
    'POW',
    'LOG',
    'SIN',
    'COS',
    'TG',
    'CTG',
    'INT',
    'FLOAT',
    'VAR'
]
t_ignore = r' '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_SQRT = r'\rad'
t_POW = r'\^^'
"""
t_LOG = r'\log'
t_SIN = r'\sin'
t_COS = r'\cos'
t_TG = r'\tan'
t_CTG = r'\ctan'
"""

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'VAR'
    return t

def t_error(t):
    print("Syntax error")
    t.lexer.skip(1)

lexer = lex.lex()


