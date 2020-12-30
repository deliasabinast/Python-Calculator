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

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_SQRT = r'\rad'
t_POW = r'\^^'
t_LOG = r'\log'
t_SIN = r'\sin'
t_COS = r'\cos'
t_TG = r'\tan'
t_CTG = r'\ctan'


