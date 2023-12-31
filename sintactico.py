import ply.yacc as yacc
from lexico import tokens
from datetime import datetime


# Regla de inicio para el analizador sintáctico
def p_program(p):
  '''program : repeatLines'''


def p_value(p):
  '''value : INT 
  | FLOAT 
  | STR
  | ID
  '''


#Linea y su regla de produccion
def p_repeatLines(p):
  '''repeatLines : line
                     | line repeatLines
            
    '''


def p_line(p):
  '''
    line : ID EQUALSVAR value
      | stamentFor
       | consulta 
       | push
       | function
       | array
       | slice
       | mathExpProd
       | CASE INT TWODOTS line 
       | switch
       | pila
       | func_declaration
       | ID EQUALSVAR INT
       | retorno
       | declaration
       | sentence
       | return
       | defer_statement
       | case_statements
       | constant_declaration
       | list_function
       | emptySlice
       | mainFunction
       | expression
       | statement
       | functionAppend
       | funcion
    '''


#xavi
def p_retorno(p):
  '''
    retorno : ID
    | ID COMMA
    | RETURN retorno
    '''


def p_expression(p):
  '''expression : ID comparator ID
    | ID comparator INT 
    | ID
    | list_function comparator INT 
    | list_function comparator ID 
    | ID LBRACKETS ID RBRACKETS MORETHAN ID
  '''


def p_comparator(p):
  '''comparator : COMPARE
    | MORETHAN
    | MINUSTHAN
  '''


def p_operator(p):
  '''operator : DIVIDE
  | MINUS
  | PLUS
  | TIMES
  '''


# Estructuras de control


#Gabriel
#FOR
def p_stamentFor(p):
  '''stamentFor : FOR ID EQUALSVAR INT DOTCOMA ID MINUSTHAN LEN LPAREN ID RPAREN DOTCOMA ID PLUS PLUS LCURLY repeatLines RCURLY
  '''


#Xavi
#SWITCH
def p_switch(p):
  '''
  switch : SWITCH ID LCURLY repeatLines RCURLY
  '''


#Raul


#IF
def p_consulta(p):
  '''
  consulta : IF expression LCURLY statements RCURLY
  '''


def p_consultaIfElse(p):
  'consulta : IF expression LCURLY statements RCURLY ELSE LCURLY statements RCURLY'


def p_statements(p):
  '''statements : statement
  | statement statements
  '''


def p_statement(p):
  ''' statement : ID 
      | sentence
      | ID EQUALS ID LBRACKETS ID RBRACKETS
      | functionAppend
  '''


def p_number(p):
  '''number : INT
            | FLOAT
        '''


# Estructuras de Datos


#Gabriel
#Definicion arreglos
def p_array(p):
  '''array : ID EQUALSVAR LBRACKETS INT RBRACKETS ID LCURLY elemArray RCURLY
    '''


def p_elemArray(p):
  '''elemArray : number 
                 | number COMMA elemArray
    '''


#Raul
# Definición de Estructura de Datos Slices
def p_slice(p):
  '''slice : ID EQUALSVAR LBRACKETS RBRACKETS ID LCURLY elemSlice RCURLY
  '''


def p_emptySlice(p):
  '''emptySlice : ID LBRACKETS RBRACKETS ID
  '''


def p_elemSlice(p):
  '''elemSlice : number 
                 | number COMMA elemSlice
  '''


#Xavi
#Definicion de pila
def p_pila(p):
  '''
    pila : TYPE STACK LBRACKETS RBRACKETS ID
    | TYPE STACK INTERFACE LCURLY RCURLY
    | TYPE STACK STRUCT LCURLY ID LBRACKETS RBRACKETS value RCURLY
    '''


def p_push(p):
  '''
    push : FUNC PUSH LPAREN ID STACK COMMA ID ID RPAREN STACK LCURLY RETURN APPEND LPAREN ID COMMA ID RPAREN RCURLY
    '''


#Declaracion de funciones


#Gabriel
# Regla declaracion de funciones sin parametros
def p_funcionSinPar(p):
  '''funcion : FUNC ID LPAREN RPAREN ID LCURLY repeatLines RCURLY
      '''


#Xavi
# Varios valores de retorno, sin parametros :D
def p_func_declaration(p):
  '''
    func_declaration : FUNC ID LPAREN RPAREN LPAREN return_types RPAREN LCURLY repeatLines RCURLY
    '''


def p_return_types(p):
  '''
    return_types : ID COMMA ID
                 | ID
    '''


#Raul


def p_function(p):
  '''function : FUNC ID LPAREN param_list RPAREN ID LCURLY repeatLines RETURN ID RCURLY
    | FUNC ID LPAREN param_list RPAREN LCURLY repeatLines RCURLY
    '''

def p_functionAppend(p):
  '''functionAppend : ID EQUALSVAR APPEND LPAREN param_list RPAREN
    '''


def p_mainFunction(p):
  '''mainFunction : FUNC MAIN LPAREN RPAREN LCURLY repeatLines RCURLY
    '''


def p_param_list(p):
  '''param_list : param
                  | param_list COMMA param
    '''


def p_param(p):
  '''param : value ID 
    | emptySlice
    | ID
    | STR
    | INT
    '''


def p_list_function(p):
  '''list_function : ID LPAREN param_list RPAREN
  | LEN LPAREN ID RPAREN
  
  '''

def p_call(p):
  '''call : ID LPAREN param_list RPAREN
  
  '''


#REGLAS SEMANTICAS

#Gabriel


#Regla las variables deben siempre ser declarados usando VAR
def p_declaration(p):
  '''declaration : VAR ID ID
  | VAR ID ID EQUALSVAR number
  | VAR ID ID EQUALSVAR STR
  | VAR ID ID EQUALSVAR ID
  | VAR ID EQUALSVAR ID LBRACKETS INT RBRACKETS
  '''


# Regla Produccion de expresiones matematicas estilo 9+10/3-5
# Este tipo de expresiones siguen la regla de que solo cierto tipo de dato pueden hacer uso de ciertas operaciones.
def p_mathExp(p):
  '''mathExp : number
  | number operator number
  '''


def p_mathExpProd(p):
  '''mathExpProd : mathExp
  | mathExp operator mathExpProd
  '''


#Raul
#Regla Semántica para una Sentencia de Impresión


def p_sentence(p):
  '''sentence : FMT PERIOD PRINTLN LPAREN arguments RPAREN 
    | FMT PERIOD PRINTF LPAREN arguments RPAREN 
    
  '''


def p_argument(p):
  '''argument : STR
    | ID
  '''


def p_arguments(p):
  '''arguments : argument
    | argument COMMA arguments
    
  '''


#Regla Semántica para una Sentencia de Return


def p_return(p):
  '''return : RETURN expression 
    | RETURN INT 
    | RETURN sentence 
 '''


#Xavi
#Regla Semántica para Casos en una Sentencia "switch"
def p_case_statements(p):
  '''
    case_statements : CASE INT TWODOTS line 
                    | CASE INT TWODOTS line case_statements
                    | DEFAULT TWODOTS line
    '''


#Regla Semántica para defer
def p_defer_statement(p):
  '''
    defer_statement : DEFER line
    '''


#Regla Semántica para declarar const
def p_constant_declaration(p):
  '''
    constant_declaration : CONST variablenum
    '''


def p_variablenum(p):
  '''
    variablenum : ID EQUALS number
    '''



def p_error(p):
    if p:
        msg = f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
        # print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        sintaxisErrors.append(msg)
        sintactico.errok()
    else:
        msg = "Error de sintaxis al fin de Linea"
        sintaxisErrors.append(msg)


# Build the parser
sintactico = yacc.yacc()

sintaxisErrors = list()

def syntaxValidator(s):
  sintaxisErrors.clear()
  result = sintactico.parse(s)
  return result


