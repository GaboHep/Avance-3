
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'APPEND CASE COMMA COMPARE CONST DEFAULT DEFER DIVIDE DOTCOMA ELSE EQUALS EQUALSVAR FLOAT FMT FOR FUNC ID IF IMPORT INT INTERFACE LBRACKETS LCURLY LEN LPAREN MAIN MINUS MINUSTHAN MORETHAN NEW PACKAGE PERIOD PI PLUS POW PRINT PRINTF PRINTLN PUSH RBRACKETS RCURLY RETURN RPAREN STACK STR STRUCT SWITCH TIMES TWODOTS TYPE VAR WHILE XCENTAGEprogram : repeatLinesvalue : INT \n  | FLOAT \n  | STR\n  | ID\n  repeatLines : line\n                     | line repeatLines\n            \n    \n    line : ID EQUALSVAR value\n      | stamentFor\n       | consulta \n       | push\n       | function\n       | array\n       | slice\n       | mathExpProd\n       | CASE INT TWODOTS line \n       | switch\n       | pila\n       | func_declaration\n       | ID EQUALSVAR INT\n       | retorno\n       | declaration\n       | sentence\n       | return\n       | defer_statement\n       | case_statements\n       | constant_declaration\n       | list_function\n       | emptySlice\n       | mainFunction\n       | expression\n       | statement\n       | ID EQUALSVAR ID LBRACKETS INT RBRACKETS\n       | functionAppend\n    \n    retorno : ID\n    | ID COMMA\n    | RETURN retorno\n    expression : ID comparator ID\n    | ID comparator INT \n    | ID\n    | list_function comparator INT \n    | list_function comparator ID \n    | ID LBRACKETS ID RBRACKETS MORETHAN ID\n  comparator : COMPARE\n    | MORETHAN\n    | MINUSTHAN\n  operator : DIVIDE\n  | MINUS\n  | PLUS\n  | TIMES\n  stamentFor : FOR ID EQUALSVAR INT DOTCOMA ID MINUSTHAN LEN LPAREN ID RPAREN DOTCOMA ID PLUS PLUS LCURLY repeatLines RCURLY\n  \n  switch : SWITCH ID LCURLY repeatLines RCURLY\n  \n  consulta : IF expression LCURLY statements RCURLY\n  consulta : IF expression LCURLY statements RCURLY ELSE LCURLY statements RCURLYstatements : statement\n  | statement statements\n   statement : ID \n      | sentence\n      | ID EQUALS ID LBRACKETS ID RBRACKETS\n      | functionAppend\n  number : INT\n            | FLOAT\n        array : ID EQUALSVAR LBRACKETS INT RBRACKETS ID LCURLY elemArray RCURLY\n    elemArray : number \n                 | number COMMA elemArray\n    slice : ID EQUALSVAR LBRACKETS RBRACKETS ID LCURLY elemSlice RCURLY\n  emptySlice : ID LBRACKETS RBRACKETS ID\n  elemSlice : number \n                 | number COMMA elemSlice\n  \n    pila : TYPE STACK LBRACKETS RBRACKETS ID\n    | TYPE STACK INTERFACE LCURLY RCURLY\n    | TYPE STACK STRUCT LCURLY ID LBRACKETS RBRACKETS value RCURLY\n    \n    push : FUNC PUSH LPAREN ID STACK COMMA ID ID RPAREN STACK LCURLY RETURN APPEND LPAREN ID COMMA ID RPAREN RCURLY\n    funcion : FUNC ID LPAREN RPAREN ID LCURLY repeatLines RCURLY\n      \n    func_declaration : FUNC ID LPAREN RPAREN LPAREN return_types RPAREN LCURLY repeatLines RCURLY\n    \n    return_types : ID COMMA ID\n                 | ID\n    function : FUNC ID LPAREN param_list RPAREN ID LCURLY repeatLines RETURN ID RCURLY\n    | FUNC ID LPAREN param_list RPAREN LCURLY repeatLines RCURLY\n    functionAppend : ID EQUALSVAR APPEND LPAREN param_list RPAREN\n    mainFunction : FUNC MAIN LPAREN RPAREN LCURLY repeatLines RCURLY\n    param_list : param\n                  | param_list COMMA param\n    param : value ID \n    | emptySlice\n    | ID\n    | STR\n    | INT\n    list_function : ID LPAREN param_list RPAREN\n  | LEN LPAREN ID RPAREN\n  \n  call : ID LPAREN param_list RPAREN\n  \n  declaration : VAR ID ID\n  | VAR ID ID EQUALSVAR number\n  | VAR ID ID EQUALSVAR STR\n  | VAR ID ID EQUALSVAR ID\n  mathExp : number\n  | number operator number\n  mathExpProd : mathExp\n  | mathExp operator mathExpProd\n  sentence : FMT PERIOD PRINTLN LPAREN arguments RPAREN \n    | FMT PERIOD PRINTF LPAREN arguments RPAREN \n    \n  argument : STR\n    | ID\n  arguments : argument\n    | argument COMMA arguments\n    \n  return : RETURN expression \n    | RETURN INT \n    | RETURN sentence \n \n    case_statements : CASE INT TWODOTS line \n                    | CASE INT TWODOTS line case_statements\n                    | DEFAULT TWODOTS line\n    \n    defer_statement : DEFER line\n    \n    constant_declaration : CONST variablenum\n    \n    variablenum : ID EQUALS number\n    '
    
_lr_action_items = {'ID':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,38,39,41,43,44,46,47,48,49,50,51,52,53,54,56,58,65,66,67,68,69,70,78,81,82,83,85,86,87,90,91,93,94,97,99,100,101,102,104,105,106,109,110,111,112,114,115,116,120,121,124,128,129,131,133,134,136,137,139,141,142,143,144,150,152,153,154,155,156,158,161,165,166,167,171,172,173,174,175,176,178,179,180,186,189,190,191,195,197,202,203,204,208,210,211,212,214,216,217,221,223,228,230,234,237,238,240,242,247,250,251,256,259,260,263,265,],[4,4,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,57,60,63,70,-98,76,78,-96,4,84,-62,85,92,-36,94,101,-45,103,-44,-46,106,108,114,-37,-106,-107,-108,-35,120,-112,4,-113,-5,-8,-2,-3,-4,131,-5,135,-4,-2,-38,-39,4,-41,-42,142,92,145,94,-35,-99,4,-92,-97,-111,159,94,-67,-89,94,163,-16,-90,142,-57,-58,-60,175,177,178,184,184,-114,187,190,-110,193,-53,196,198,4,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,211,4,-100,184,-101,4,142,226,4,229,-81,231,-66,-109,-79,4,-63,244,-54,246,-72,-75,-78,253,258,4,262,-51,-73,]),'CASE':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[12,12,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,12,-62,-36,-37,-106,-107,-108,-35,-112,12,-113,-5,-8,-2,-3,-4,-38,-39,12,-41,-42,-35,-99,12,-92,-97,-111,-67,-89,164,-90,-114,-110,-53,12,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,12,-100,-101,12,12,-81,-66,164,-79,12,-63,-54,-72,-75,-78,12,-51,-73,]),'FOR':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[30,30,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,30,-62,-36,-37,-106,-107,-108,-35,-112,30,-113,-5,-8,-2,-3,-4,-38,-39,30,-41,-42,-35,-99,30,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,30,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,30,-100,-101,30,30,-81,-66,-109,-79,30,-63,-54,-72,-75,-78,30,-51,-73,]),'IF':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[32,32,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,32,-62,-36,-37,-106,-107,-108,-35,-112,32,-113,-5,-8,-2,-3,-4,-38,-39,32,-41,-42,-35,-99,32,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,32,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,32,-100,-101,32,32,-81,-66,-109,-79,32,-63,-54,-72,-75,-78,32,-51,-73,]),'FUNC':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[33,33,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,33,-62,-36,-37,-106,-107,-108,-35,-112,33,-113,-5,-8,-2,-3,-4,-38,-39,33,-41,-42,-35,-99,33,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,33,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,33,-100,-101,33,33,-81,-66,-109,-79,33,-63,-54,-72,-75,-78,33,-51,-73,]),'SWITCH':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[36,36,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,36,-62,-36,-37,-106,-107,-108,-35,-112,36,-113,-5,-8,-2,-3,-4,-38,-39,36,-41,-42,-35,-99,36,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,36,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,36,-100,-101,36,36,-81,-66,-109,-79,36,-63,-54,-72,-75,-78,36,-51,-73,]),'TYPE':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[37,37,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,37,-62,-36,-37,-106,-107,-108,-35,-112,37,-113,-5,-8,-2,-3,-4,-38,-39,37,-41,-42,-35,-99,37,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,37,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,37,-100,-101,37,37,-81,-66,-109,-79,37,-63,-54,-72,-75,-78,37,-51,-73,]),'RETURN':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,34,35,39,41,44,45,48,65,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,227,228,230,234,238,242,247,249,250,259,263,265,],[34,34,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,65,-98,-96,34,-62,-7,-36,65,-37,-106,-107,-108,-35,-112,34,-113,-5,-8,-2,-3,-4,-38,-39,34,-41,-42,-35,-99,34,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,34,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,34,-100,-101,34,34,-81,-66,-109,240,-79,34,-63,-54,-72,-75,252,-78,34,-51,-73,]),'VAR':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[38,38,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,38,-62,-36,-37,-106,-107,-108,-35,-112,38,-113,-5,-8,-2,-3,-4,-38,-39,38,-41,-42,-35,-99,38,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,38,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,38,-100,-101,38,38,-81,-66,-109,-79,38,-63,-54,-72,-75,-78,38,-51,-73,]),'FMT':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,34,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,109,114,115,116,120,121,124,131,133,137,139,141,142,143,144,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,210,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[40,40,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,40,-98,-96,40,-62,-36,-37,-106,-107,-108,-35,-112,40,-113,-5,-8,-2,-3,-4,-38,-39,40,-41,-42,40,-35,-99,40,-92,-97,-111,-67,-89,-16,-90,40,-57,-58,-60,-114,-110,-53,40,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,40,-100,-101,40,40,40,-81,-66,-109,-79,40,-63,-54,-72,-75,-78,40,-51,-73,]),'DEFER':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[41,41,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,41,-62,-36,-37,-106,-107,-108,-35,-112,41,-113,-5,-8,-2,-3,-4,-38,-39,41,-41,-42,-35,-99,41,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,41,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,41,-100,-101,41,41,-81,-66,-109,-79,41,-63,-54,-72,-75,-78,41,-51,-73,]),'DEFAULT':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[42,42,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,42,-62,-36,-37,-106,-107,-108,-35,-112,42,-113,-5,-8,-2,-3,-4,-38,-39,42,-41,-42,-35,-99,42,-92,-97,-111,-67,-89,42,-90,-114,-110,-53,42,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,42,-100,-101,42,42,-81,-66,42,-79,42,-63,-54,-72,-75,-78,42,-51,-73,]),'CONST':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[43,43,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,43,-62,-36,-37,-106,-107,-108,-35,-112,43,-113,-5,-8,-2,-3,-4,-38,-39,43,-41,-42,-35,-99,43,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,43,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,43,-100,-101,43,43,-81,-66,-109,-79,43,-63,-54,-72,-75,-78,43,-51,-73,]),'LEN':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,34,35,39,41,44,48,66,67,68,69,70,81,82,83,85,86,87,90,91,101,102,104,105,106,114,115,116,120,121,124,131,133,137,139,156,165,167,173,174,175,176,178,179,180,186,189,190,191,197,202,204,208,209,212,216,221,223,228,230,234,238,242,247,250,259,263,265,],[31,31,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,31,31,-98,-96,31,-62,-36,-37,-106,-107,-108,-35,-112,31,-113,-5,-8,-2,-3,-4,-38,-39,31,-41,-42,-35,-99,31,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,31,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,31,-100,-101,31,224,31,-81,-66,-109,-79,31,-63,-54,-72,-75,-78,31,-51,-73,]),'INT':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,34,35,39,41,44,46,48,49,50,51,53,54,56,66,67,68,69,70,71,72,73,74,75,79,81,82,83,85,86,87,88,90,91,101,102,104,105,106,107,112,114,115,116,120,121,124,125,126,129,131,133,134,137,139,153,156,164,165,167,173,174,175,176,178,179,180,186,188,189,190,191,197,202,204,205,208,212,216,217,221,222,223,228,230,234,235,238,242,247,250,259,263,265,],[13,13,-35,-9,-10,-11,-12,-13,-14,-15,55,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,68,-98,-96,13,-62,87,-36,100,102,-45,-44,-46,105,-37,-106,-107,-108,-35,13,-47,-48,-49,-50,13,-112,13,-113,-5,-8,-2,127,-3,-4,-38,-39,13,-41,-42,138,100,-35,-99,13,-92,-97,-111,13,157,100,-67,-89,100,-16,-90,13,-114,192,-110,-53,13,-52,-70,-71,-95,-93,-94,-33,13,-80,-43,-59,13,-100,-101,13,13,13,-81,233,-66,13,-109,-79,13,-63,13,-54,-72,-75,-78,13,-51,-73,]),'FLOAT':([0,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,41,44,46,48,49,66,67,68,69,70,71,72,73,74,75,79,81,82,83,85,86,87,90,91,101,102,104,105,106,112,114,115,116,120,121,124,125,129,131,133,134,137,139,153,156,165,167,173,174,175,176,178,179,180,186,188,189,190,191,197,202,204,205,208,212,216,217,221,222,223,228,230,234,235,238,242,247,250,259,263,265,],[44,44,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,44,-62,90,-36,90,-37,-106,-107,-108,-35,44,-47,-48,-49,-50,44,-112,44,-113,-5,-8,-2,-3,-4,-38,-39,44,-41,-42,90,-35,-99,44,-92,-97,-111,44,90,-67,-89,90,-16,-90,44,-114,-110,-53,44,-52,-70,-71,-95,-93,-94,-33,44,-80,-43,-59,44,-100,-101,44,44,44,-81,90,-66,44,-109,-79,44,-63,44,-54,-72,-75,-78,44,-51,-73,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,44,45,48,66,67,68,69,70,81,83,85,86,87,90,91,101,102,105,106,114,115,120,121,124,131,133,137,139,156,165,167,174,175,176,178,179,180,186,189,190,191,202,204,216,221,223,228,234,238,242,247,250,263,265,],[0,-1,-6,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,-62,-7,-36,-37,-106,-107,-108,-35,-112,-113,-5,-8,-2,-3,-4,-38,-39,-41,-42,-35,-99,-92,-97,-111,-67,-89,-16,-90,-114,-110,-53,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,-100,-101,-81,-66,-109,-79,-63,-54,-72,-75,-78,-51,-73,]),'RCURLY':([3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,35,39,44,45,48,66,67,68,69,70,81,83,85,86,87,90,91,101,102,105,106,114,115,120,121,124,131,133,137,139,140,141,142,143,144,149,151,156,165,167,168,174,175,176,178,179,180,186,189,190,191,200,202,204,206,207,213,216,219,220,221,223,225,228,231,232,233,234,236,238,241,242,243,246,247,250,261,263,264,265,],[-6,-35,-9,-10,-11,-12,-13,-14,-15,-61,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-34,-98,-96,-62,-7,-36,-37,-106,-107,-108,-35,-112,-113,-5,-8,-2,-3,-4,-38,-39,-41,-42,-35,-99,-92,-97,-111,-67,-89,-16,-90,167,-55,-57,-58,-60,174,176,-114,-110,-53,-56,-52,-70,-71,-95,-93,-94,-33,-80,-43,-59,216,-100,-101,221,-68,228,-81,234,-64,-66,-109,238,-79,-5,242,-2,-63,-69,-54,247,-72,-65,250,-75,-78,263,-51,265,-73,]),'EQUALSVAR':([4,57,120,142,],[46,107,153,169,]),'COMMA':([4,13,44,70,94,95,96,98,99,100,114,131,135,146,160,162,170,182,183,184,198,207,220,258,],[48,-61,-62,48,-86,134,-82,-85,-87,-88,48,-67,-84,134,134,-83,195,203,-102,-103,214,222,235,260,]),'LPAREN':([4,31,60,62,63,64,70,89,122,123,147,224,254,],[49,58,49,111,112,113,49,129,154,155,172,237,256,]),'LBRACKETS':([4,46,60,70,77,85,94,103,177,],[47,88,110,110,117,126,132,136,201,]),'EQUALS':([4,84,142,],[52,125,52,]),'COMPARE':([4,24,60,61,70,133,139,],[53,53,53,53,53,-89,-90,]),'MORETHAN':([4,24,60,61,70,130,133,139,],[51,51,51,51,51,161,-89,-90,]),'MINUSTHAN':([4,24,60,61,70,133,139,193,],[54,54,54,54,54,-89,-90,209,]),'DIVIDE':([13,35,39,44,121,],[-61,72,72,-62,-97,]),'MINUS':([13,35,39,44,121,],[-61,73,73,-62,-97,]),'PLUS':([13,35,39,44,121,253,255,],[-61,74,74,-62,-97,255,257,]),'TIMES':([13,35,39,44,121,],[-61,75,75,-62,-97,]),'PUSH':([33,],[62,]),'MAIN':([33,],[64,]),'STACK':([37,145,239,],[77,170,245,]),'PERIOD':([40,],[80,]),'TWODOTS':([42,55,192,],[82,104,208,]),'APPEND':([46,169,252,],[89,89,254,]),'STR':([46,49,112,129,134,153,154,155,203,217,],[91,99,99,99,99,180,183,183,183,91,]),'RBRACKETS':([47,88,92,117,127,132,157,163,201,],[93,128,130,150,158,93,186,191,217,]),'LCURLY':([59,60,76,101,102,105,106,118,119,148,159,171,187,190,194,196,215,245,257,],[109,-40,116,-38,-39,-41,-42,151,152,173,188,197,205,-43,210,212,230,249,259,]),'INTERFACE':([77,],[118,]),'STRUCT':([77,],[119,]),'PRINTLN':([80,],[122,]),'PRINTF':([80,],[123,]),'RPAREN':([94,95,96,98,99,100,108,112,113,131,135,146,160,162,181,182,183,184,185,198,199,218,226,229,244,262,],[-86,133,-82,-85,-87,-88,139,147,148,-67,-84,171,189,-83,202,-104,-102,-103,204,-77,215,-105,239,-76,248,264,]),'DOTCOMA':([138,248,],[166,251,]),'ELSE':([167,],[194,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'repeatLines':([0,3,116,173,197,212,230,259,],[2,45,149,200,213,227,241,261,]),'line':([0,3,41,82,104,116,173,197,208,212,230,259,],[3,3,81,124,137,3,3,3,223,3,3,3,]),'stamentFor':([0,3,41,82,104,116,173,197,208,212,230,259,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'consulta':([0,3,41,82,104,116,173,197,208,212,230,259,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'push':([0,3,41,82,104,116,173,197,208,212,230,259,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'function':([0,3,41,82,104,116,173,197,208,212,230,259,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'array':([0,3,41,82,104,116,173,197,208,212,230,259,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'slice':([0,3,41,82,104,116,173,197,208,212,230,259,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'mathExpProd':([0,3,41,71,82,104,116,173,197,208,212,230,259,],[11,11,11,115,11,11,11,11,11,11,11,11,11,]),'switch':([0,3,41,82,104,116,173,197,208,212,230,259,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'pila':([0,3,41,82,104,116,173,197,208,212,230,259,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'func_declaration':([0,3,41,82,104,116,173,197,208,212,230,259,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'retorno':([0,3,34,41,65,82,104,116,173,197,208,212,230,259,],[17,17,66,17,66,17,17,17,17,17,17,17,17,17,]),'declaration':([0,3,41,82,104,116,173,197,208,212,230,259,],[18,18,18,18,18,18,18,18,18,18,18,18,]),'sentence':([0,3,34,41,82,104,109,116,141,173,197,208,210,212,230,259,],[19,19,69,19,19,19,143,19,143,19,19,19,143,19,19,19,]),'return':([0,3,41,82,104,116,173,197,208,212,230,259,],[20,20,20,20,20,20,20,20,20,20,20,20,]),'defer_statement':([0,3,41,82,104,116,173,197,208,212,230,259,],[21,21,21,21,21,21,21,21,21,21,21,21,]),'case_statements':([0,3,41,82,104,116,137,173,197,208,212,223,230,259,],[22,22,22,22,22,22,165,22,22,22,22,165,22,22,]),'constant_declaration':([0,3,41,82,104,116,173,197,208,212,230,259,],[23,23,23,23,23,23,23,23,23,23,23,23,]),'list_function':([0,3,32,34,41,82,104,116,173,197,208,212,230,259,],[24,24,61,61,24,24,24,24,24,24,24,24,24,24,]),'emptySlice':([0,3,41,49,82,104,112,116,129,134,173,197,208,212,230,259,],[25,25,25,98,25,25,98,25,98,98,25,25,25,25,25,25,]),'mainFunction':([0,3,41,82,104,116,173,197,208,212,230,259,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'expression':([0,3,32,34,41,82,104,116,173,197,208,212,230,259,],[27,27,59,67,27,27,27,27,27,27,27,27,27,27,]),'statement':([0,3,41,82,104,109,116,141,173,197,208,210,212,230,259,],[28,28,28,28,28,141,28,141,28,28,28,141,28,28,28,]),'functionAppend':([0,3,41,82,104,109,116,141,173,197,208,210,212,230,259,],[29,29,29,29,29,144,29,144,29,29,29,144,29,29,29,]),'mathExp':([0,3,41,71,82,104,116,173,197,208,212,230,259,],[35,35,35,35,35,35,35,35,35,35,35,35,35,]),'number':([0,3,41,71,79,82,104,116,125,153,173,188,197,205,208,212,222,230,235,259,],[39,39,39,39,121,39,39,39,156,179,39,207,39,220,39,39,207,39,220,39,]),'comparator':([4,24,60,61,70,],[50,56,50,56,50,]),'operator':([35,39,],[71,79,]),'variablenum':([43,],[83,]),'value':([46,49,112,129,134,217,],[86,97,97,97,97,232,]),'param_list':([49,112,129,],[95,146,160,]),'param':([49,112,129,134,],[96,96,96,162,]),'statements':([109,141,210,],[140,168,225,]),'arguments':([154,155,203,],[181,185,218,]),'argument':([154,155,203,],[182,182,182,]),'return_types':([172,],[199,]),'elemSlice':([188,222,],[206,236,]),'elemArray':([205,235,],[219,243,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> repeatLines','program',1,'p_program','sintactico.py',8),
  ('value -> INT','value',1,'p_value','sintactico.py',12),
  ('value -> FLOAT','value',1,'p_value','sintactico.py',13),
  ('value -> STR','value',1,'p_value','sintactico.py',14),
  ('value -> ID','value',1,'p_value','sintactico.py',15),
  ('repeatLines -> line','repeatLines',1,'p_repeatLines','sintactico.py',21),
  ('repeatLines -> line repeatLines','repeatLines',2,'p_repeatLines','sintactico.py',22),
  ('line -> ID EQUALSVAR value','line',3,'p_line','sintactico.py',29),
  ('line -> stamentFor','line',1,'p_line','sintactico.py',30),
  ('line -> consulta','line',1,'p_line','sintactico.py',31),
  ('line -> push','line',1,'p_line','sintactico.py',32),
  ('line -> function','line',1,'p_line','sintactico.py',33),
  ('line -> array','line',1,'p_line','sintactico.py',34),
  ('line -> slice','line',1,'p_line','sintactico.py',35),
  ('line -> mathExpProd','line',1,'p_line','sintactico.py',36),
  ('line -> CASE INT TWODOTS line','line',4,'p_line','sintactico.py',37),
  ('line -> switch','line',1,'p_line','sintactico.py',38),
  ('line -> pila','line',1,'p_line','sintactico.py',39),
  ('line -> func_declaration','line',1,'p_line','sintactico.py',40),
  ('line -> ID EQUALSVAR INT','line',3,'p_line','sintactico.py',41),
  ('line -> retorno','line',1,'p_line','sintactico.py',42),
  ('line -> declaration','line',1,'p_line','sintactico.py',43),
  ('line -> sentence','line',1,'p_line','sintactico.py',44),
  ('line -> return','line',1,'p_line','sintactico.py',45),
  ('line -> defer_statement','line',1,'p_line','sintactico.py',46),
  ('line -> case_statements','line',1,'p_line','sintactico.py',47),
  ('line -> constant_declaration','line',1,'p_line','sintactico.py',48),
  ('line -> list_function','line',1,'p_line','sintactico.py',49),
  ('line -> emptySlice','line',1,'p_line','sintactico.py',50),
  ('line -> mainFunction','line',1,'p_line','sintactico.py',51),
  ('line -> expression','line',1,'p_line','sintactico.py',52),
  ('line -> statement','line',1,'p_line','sintactico.py',53),
  ('line -> ID EQUALSVAR ID LBRACKETS INT RBRACKETS','line',6,'p_line','sintactico.py',54),
  ('line -> functionAppend','line',1,'p_line','sintactico.py',55),
  ('retorno -> ID','retorno',1,'p_retorno','sintactico.py',62),
  ('retorno -> ID COMMA','retorno',2,'p_retorno','sintactico.py',63),
  ('retorno -> RETURN retorno','retorno',2,'p_retorno','sintactico.py',64),
  ('expression -> ID comparator ID','expression',3,'p_expression','sintactico.py',69),
  ('expression -> ID comparator INT','expression',3,'p_expression','sintactico.py',70),
  ('expression -> ID','expression',1,'p_expression','sintactico.py',71),
  ('expression -> list_function comparator INT','expression',3,'p_expression','sintactico.py',72),
  ('expression -> list_function comparator ID','expression',3,'p_expression','sintactico.py',73),
  ('expression -> ID LBRACKETS ID RBRACKETS MORETHAN ID','expression',6,'p_expression','sintactico.py',74),
  ('comparator -> COMPARE','comparator',1,'p_comparator','sintactico.py',79),
  ('comparator -> MORETHAN','comparator',1,'p_comparator','sintactico.py',80),
  ('comparator -> MINUSTHAN','comparator',1,'p_comparator','sintactico.py',81),
  ('operator -> DIVIDE','operator',1,'p_operator','sintactico.py',86),
  ('operator -> MINUS','operator',1,'p_operator','sintactico.py',87),
  ('operator -> PLUS','operator',1,'p_operator','sintactico.py',88),
  ('operator -> TIMES','operator',1,'p_operator','sintactico.py',89),
  ('stamentFor -> FOR ID EQUALSVAR INT DOTCOMA ID MINUSTHAN LEN LPAREN ID RPAREN DOTCOMA ID PLUS PLUS LCURLY repeatLines RCURLY','stamentFor',18,'p_stamentFor','sintactico.py',99),
  ('switch -> SWITCH ID LCURLY repeatLines RCURLY','switch',5,'p_switch','sintactico.py',107),
  ('consulta -> IF expression LCURLY statements RCURLY','consulta',5,'p_consulta','sintactico.py',117),
  ('consulta -> IF expression LCURLY statements RCURLY ELSE LCURLY statements RCURLY','consulta',9,'p_consultaIfElse','sintactico.py',122),
  ('statements -> statement','statements',1,'p_statements','sintactico.py',126),
  ('statements -> statement statements','statements',2,'p_statements','sintactico.py',127),
  ('statement -> ID','statement',1,'p_statement','sintactico.py',132),
  ('statement -> sentence','statement',1,'p_statement','sintactico.py',133),
  ('statement -> ID EQUALS ID LBRACKETS ID RBRACKETS','statement',6,'p_statement','sintactico.py',134),
  ('statement -> functionAppend','statement',1,'p_statement','sintactico.py',135),
  ('number -> INT','number',1,'p_number','sintactico.py',140),
  ('number -> FLOAT','number',1,'p_number','sintactico.py',141),
  ('array -> ID EQUALSVAR LBRACKETS INT RBRACKETS ID LCURLY elemArray RCURLY','array',9,'p_array','sintactico.py',151),
  ('elemArray -> number','elemArray',1,'p_elemArray','sintactico.py',156),
  ('elemArray -> number COMMA elemArray','elemArray',3,'p_elemArray','sintactico.py',157),
  ('slice -> ID EQUALSVAR LBRACKETS RBRACKETS ID LCURLY elemSlice RCURLY','slice',8,'p_slice','sintactico.py',164),
  ('emptySlice -> ID LBRACKETS RBRACKETS ID','emptySlice',4,'p_emptySlice','sintactico.py',169),
  ('elemSlice -> number','elemSlice',1,'p_elemSlice','sintactico.py',174),
  ('elemSlice -> number COMMA elemSlice','elemSlice',3,'p_elemSlice','sintactico.py',175),
  ('pila -> TYPE STACK LBRACKETS RBRACKETS ID','pila',5,'p_pila','sintactico.py',183),
  ('pila -> TYPE STACK INTERFACE LCURLY RCURLY','pila',5,'p_pila','sintactico.py',184),
  ('pila -> TYPE STACK STRUCT LCURLY ID LBRACKETS RBRACKETS value RCURLY','pila',9,'p_pila','sintactico.py',185),
  ('push -> FUNC PUSH LPAREN ID STACK COMMA ID ID RPAREN STACK LCURLY RETURN APPEND LPAREN ID COMMA ID RPAREN RCURLY','push',19,'p_push','sintactico.py',191),
  ('funcion -> FUNC ID LPAREN RPAREN ID LCURLY repeatLines RCURLY','funcion',8,'p_funcionSinPar','sintactico.py',201),
  ('func_declaration -> FUNC ID LPAREN RPAREN LPAREN return_types RPAREN LCURLY repeatLines RCURLY','func_declaration',10,'p_func_declaration','sintactico.py',209),
  ('return_types -> ID COMMA ID','return_types',3,'p_return_types','sintactico.py',215),
  ('return_types -> ID','return_types',1,'p_return_types','sintactico.py',216),
  ('function -> FUNC ID LPAREN param_list RPAREN ID LCURLY repeatLines RETURN ID RCURLY','function',11,'p_function','sintactico.py',224),
  ('function -> FUNC ID LPAREN param_list RPAREN LCURLY repeatLines RCURLY','function',8,'p_function','sintactico.py',225),
  ('functionAppend -> ID EQUALSVAR APPEND LPAREN param_list RPAREN','functionAppend',6,'p_functionAppend','sintactico.py',229),
  ('mainFunction -> FUNC MAIN LPAREN RPAREN LCURLY repeatLines RCURLY','mainFunction',7,'p_mainFunction','sintactico.py',234),
  ('param_list -> param','param_list',1,'p_param_list','sintactico.py',239),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','sintactico.py',240),
  ('param -> value ID','param',2,'p_param','sintactico.py',245),
  ('param -> emptySlice','param',1,'p_param','sintactico.py',246),
  ('param -> ID','param',1,'p_param','sintactico.py',247),
  ('param -> STR','param',1,'p_param','sintactico.py',248),
  ('param -> INT','param',1,'p_param','sintactico.py',249),
  ('list_function -> ID LPAREN param_list RPAREN','list_function',4,'p_list_function','sintactico.py',254),
  ('list_function -> LEN LPAREN ID RPAREN','list_function',4,'p_list_function','sintactico.py',255),
  ('call -> ID LPAREN param_list RPAREN','call',4,'p_call','sintactico.py',260),
  ('declaration -> VAR ID ID','declaration',3,'p_declaration','sintactico.py',272),
  ('declaration -> VAR ID ID EQUALSVAR number','declaration',5,'p_declaration','sintactico.py',273),
  ('declaration -> VAR ID ID EQUALSVAR STR','declaration',5,'p_declaration','sintactico.py',274),
  ('declaration -> VAR ID ID EQUALSVAR ID','declaration',5,'p_declaration','sintactico.py',275),
  ('mathExp -> number','mathExp',1,'p_mathExp','sintactico.py',282),
  ('mathExp -> number operator number','mathExp',3,'p_mathExp','sintactico.py',283),
  ('mathExpProd -> mathExp','mathExpProd',1,'p_mathExpProd','sintactico.py',288),
  ('mathExpProd -> mathExp operator mathExpProd','mathExpProd',3,'p_mathExpProd','sintactico.py',289),
  ('sentence -> FMT PERIOD PRINTLN LPAREN arguments RPAREN','sentence',6,'p_sentence','sintactico.py',298),
  ('sentence -> FMT PERIOD PRINTF LPAREN arguments RPAREN','sentence',6,'p_sentence','sintactico.py',299),
  ('argument -> STR','argument',1,'p_argument','sintactico.py',305),
  ('argument -> ID','argument',1,'p_argument','sintactico.py',306),
  ('arguments -> argument','arguments',1,'p_arguments','sintactico.py',311),
  ('arguments -> argument COMMA arguments','arguments',3,'p_arguments','sintactico.py',312),
  ('return -> RETURN expression','return',2,'p_return','sintactico.py',321),
  ('return -> RETURN INT','return',2,'p_return','sintactico.py',322),
  ('return -> RETURN sentence','return',2,'p_return','sintactico.py',323),
  ('case_statements -> CASE INT TWODOTS line','case_statements',4,'p_case_statements','sintactico.py',331),
  ('case_statements -> CASE INT TWODOTS line case_statements','case_statements',5,'p_case_statements','sintactico.py',332),
  ('case_statements -> DEFAULT TWODOTS line','case_statements',3,'p_case_statements','sintactico.py',333),
  ('defer_statement -> DEFER line','defer_statement',2,'p_defer_statement','sintactico.py',340),
  ('constant_declaration -> CONST variablenum','constant_declaration',2,'p_constant_declaration','sintactico.py',347),
  ('variablenum -> ID EQUALS number','variablenum',3,'p_variablenum','sintactico.py',353),
]
