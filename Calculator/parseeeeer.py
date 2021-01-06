import ply.yacc as yacc
import math

"""
expression : expression + term
            | expression - term
            | term

 term       : term * factor
            | term / factor
            | factor

 factor     : NUMBER
            | ( expression )

"""

def p_calc(p):   #start
    '''
    calc: expression
        | empty
    '''
    print(evaluate(p[1]))

def p_empty(p):
    ''' 
    empty: 
    '''
    p[0]=None

parser = yacc.yacc()

def p_expression(p):   # creates a "tree" -> basic operations
    '''
    expression: expression POW expression
              | expression DIV expression
              | expression MUL expression
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

def p_function(p): #trig, log, sqrt

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
            return pow(evaluate(p[1]), evaluate(p[2]))

    else:
        return p