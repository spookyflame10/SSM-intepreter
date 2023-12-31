
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DUP IADD IDIV ILDC IMOD IMUL ISUB JMP JNZ JZ LABEL LOAD NUMBER POP STORE SWAPprogram : instructionsinstructions : instruction\n                    | instructions instruction\n                    | instructions LABELinstruction : ILDC NUMBER\n                   | IADD\n                   | ISUB\n                   | IMUL\n                   | IDIV\n                   | IMOD\n                   | POP\n                   | DUP\n                   | SWAP\n                   | JZ LABEL\n                   | JNZ LABEL\n                   | JMP LABEL\n                   | LOAD\n                   | STORE\n                   | LABEL'
    
_lr_action_items = {'ILDC':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[5,5,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'IADD':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[6,6,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'ISUB':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[7,7,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'IMUL':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[8,8,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'IDIV':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[9,9,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'IMOD':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[10,10,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'POP':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[11,11,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'DUP':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[12,12,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'SWAP':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[13,13,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'JZ':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[14,14,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'JNZ':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[15,15,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'JMP':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[16,16,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'LOAD':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[17,17,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'STORE':([0,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[18,18,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'LABEL':([0,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,],[4,20,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,22,23,24,-17,-18,-3,-4,-5,-14,-15,-16,]),'$end':([1,2,3,4,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24,],[0,-1,-2,-19,-6,-7,-8,-9,-10,-11,-12,-13,-17,-18,-3,-4,-5,-14,-15,-16,]),'NUMBER':([5,],[21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,],[2,]),'instruction':([0,2,],[3,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','main.py',74),
  ('instructions -> instruction','instructions',1,'p_instructions','main.py',78),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','main.py',79),
  ('instructions -> instructions LABEL','instructions',2,'p_instructions','main.py',80),
  ('instruction -> ILDC NUMBER','instruction',2,'p_instruction','main.py',87),
  ('instruction -> IADD','instruction',1,'p_instruction','main.py',88),
  ('instruction -> ISUB','instruction',1,'p_instruction','main.py',89),
  ('instruction -> IMUL','instruction',1,'p_instruction','main.py',90),
  ('instruction -> IDIV','instruction',1,'p_instruction','main.py',91),
  ('instruction -> IMOD','instruction',1,'p_instruction','main.py',92),
  ('instruction -> POP','instruction',1,'p_instruction','main.py',93),
  ('instruction -> DUP','instruction',1,'p_instruction','main.py',94),
  ('instruction -> SWAP','instruction',1,'p_instruction','main.py',95),
  ('instruction -> JZ LABEL','instruction',2,'p_instruction','main.py',96),
  ('instruction -> JNZ LABEL','instruction',2,'p_instruction','main.py',97),
  ('instruction -> JMP LABEL','instruction',2,'p_instruction','main.py',98),
  ('instruction -> LOAD','instruction',1,'p_instruction','main.py',99),
  ('instruction -> STORE','instruction',1,'p_instruction','main.py',100),
  ('instruction -> LABEL','instruction',1,'p_instruction','main.py',101),
]
