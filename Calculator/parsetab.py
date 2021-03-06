
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULDIVleftPOWrightUMINUSDIV FLOAT FUNCTION INT LP MINUS MUL PLUS POW RP\n    calc : expression\n        | empty\n    \n    expression : FUNCTION LP expression RP\n    \n    expression : LP expression RP\n    \n    expression : expression POW expression\n                | expression MUL expression\n                | expression DIV expression\n                | expression PLUS expression\n                | expression MINUS expression\n    \n    expression : MINUS expression %prec UMINUS\n    \n    expression : INT\n                | FLOAT\n    \n    empty :\n    '
    
_lr_action_items = {'FUNCTION':([0,5,6,9,10,11,12,13,14,],[4,4,4,4,4,4,4,4,4,]),'LP':([0,4,5,6,9,10,11,12,13,14,],[5,14,5,5,5,5,5,5,5,5,]),'MINUS':([0,2,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,],[6,13,6,6,-11,-12,6,6,6,6,6,6,13,-10,-5,-6,-7,-8,-9,13,-4,-3,]),'INT':([0,5,6,9,10,11,12,13,14,],[7,7,7,7,7,7,7,7,7,]),'FLOAT':([0,5,6,9,10,11,12,13,14,],[8,8,8,8,8,8,8,8,8,]),'$end':([0,1,2,3,7,8,16,17,18,19,20,21,23,24,],[-13,0,-1,-2,-11,-12,-10,-5,-6,-7,-8,-9,-4,-3,]),'POW':([2,7,8,15,16,17,18,19,20,21,22,23,24,],[9,-11,-12,9,-10,-5,9,9,9,9,9,-4,-3,]),'MUL':([2,7,8,15,16,17,18,19,20,21,22,23,24,],[10,-11,-12,10,-10,-5,-6,-7,10,10,10,-4,-3,]),'DIV':([2,7,8,15,16,17,18,19,20,21,22,23,24,],[11,-11,-12,11,-10,-5,-6,-7,11,11,11,-4,-3,]),'PLUS':([2,7,8,15,16,17,18,19,20,21,22,23,24,],[12,-11,-12,12,-10,-5,-6,-7,-8,-9,12,-4,-3,]),'RP':([7,8,15,16,17,18,19,20,21,22,23,24,],[-11,-12,23,-10,-5,-6,-7,-8,-9,24,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,5,6,9,10,11,12,13,14,],[2,15,16,17,18,19,20,21,22,]),'empty':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','calculator.py',69),
  ('calc -> empty','calc',1,'p_calc','calculator.py',70),
  ('expression -> FUNCTION LP expression RP','expression',4,'p_function','calculator.py',78),
  ('expression -> LP expression RP','expression',3,'p_expression_parentheses','calculator.py',84),
  ('expression -> expression POW expression','expression',3,'p_expression','calculator.py',93),
  ('expression -> expression MUL expression','expression',3,'p_expression','calculator.py',94),
  ('expression -> expression DIV expression','expression',3,'p_expression','calculator.py',95),
  ('expression -> expression PLUS expression','expression',3,'p_expression','calculator.py',96),
  ('expression -> expression MINUS expression','expression',3,'p_expression','calculator.py',97),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calculator.py',103),
  ('expression -> INT','expression',1,'p_expression_number','calculator.py',109),
  ('expression -> FLOAT','expression',1,'p_expression_number','calculator.py',110),
  ('empty -> <empty>','empty',0,'p_empty','calculator.py',119),
]
