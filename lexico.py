import ply.lex as lex

#Algoritmo Raul Leon

#func processParams(name string, age int, data []int){ if len(data) > 0 {slicedData := append(data, age) fmt.Println("Nombre:", name) fmt.Println("Slice después de añadir la edad:", slicedData)} else {fmt.Println("El slice está vacío")}}
#func main() { slice := []int{1, 2, 3, 4, 5} processParams("Raul", 21, slice) }

# func processParams(name string, age int, data []int) {
# 	if len(data) > 0 {
# 		slicedData := append(data, age) 
# 		fmt.Println("Nombre:", name)
# 		fmt.Println("Slice después de añadir la edad:", slicedData)
# 	} else {
# 		fmt.Println("El slice está vacío")
# 	}
# }

# func main() {
# 	slice := []int{1, 2, 3, 4, 5}
# 	processParams("Raul", 21, slice)

# }

#Algortimo Pablo Herrera

#func Maximo() int {
# max:=nums[0]
# for i:=1;i<len(nums);i++{
#   if nums[i]>max{
#     max=nums[i]
#   }
# }
# return max
#}

#Algoritmo Xavier Cobos
#Realice mi aporte en Replit, así que lo pase directamente a este trabajo colaborativo c:
#https://replit.com/@XavierCobos/TurboLinedSpof#main.py

# package main
# import (
#     "fmt"
#     "math"
# )
# func calcularAreaCirculo(radio float64) float64 {
#     return math.Pi * math.Pow(radio, 2)
# }
# func main() {
#     radio := 5.0
#     area := calcularAreaCirculo(radio)
#     fmt.Printf("El área del círculo con radio %.2f es %.2f\n", radio, area)
# }

#Diccionario de palabras reservadas
reserved = {
  'while': 'WHILE',
  'if': 'IF',
  'func': 'FUNC',
  'return': 'RETURN',
  'for': 'FOR',
  'len': 'LEN',
  'package': 'PACKAGE',
  'main': 'MAIN',
  'switch': 'SWITCH',
  'case': 'CASE',
  'Printf': 'PRINTF',
  'Println': 'PRINTLN',
  'else': 'ELSE',
  'import': 'IMPORT',
  'Pi': 'PI',
  'Pow': 'POW',
  'print': 'PRINT',
  'type': 'TYPE',
  'Stack': 'STACK',
  'interface': 'INTERFACE',
  'struct': 'STRUCT',
  'Push': 'PUSH',
  'append': 'APPEND',
  'var': 'VAR',
  'fmt': 'FMT',
  'default': 'DEFAULT',
  'defer': 'DEFER',
  'const': 'CONST'
}

#Sequencia de tokens, puede ser lista o tupla
tokens = ('INT', 'FLOAT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN',
          'RPAREN', 'ID', 'EQUALS', 'COMPARE', 'LCURLY', 'RCURLY', 'EQUALSVAR',
          'LBRACKETS', 'RBRACKETS', 'DOTCOMA', 'MINUSTHAN', 'MORETHAN',
          'COMMA', 'PERIOD', 'STR', 'XCENTAGE', 'NEW', 'TWODOTS') + tuple(
            reserved.values())

#Exp Regulares para tokens de símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INT = r'(-)?\d+'
t_FLOAT = r'(-)?\d+\.\d+'
t_EQUALS = r'='

#Raul Leon
t_COMPARE = r'=='
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALSVAR = r':='

#Pablo Herrera
t_LBRACKETS = r'\['
t_RBRACKETS = r'\]'
t_DOTCOMA = r'\;'
t_MINUSTHAN = r'\<'
t_MORETHAN = r'\>'

#Xavier Cobos
t_COMMA = r','
t_PERIOD = r'\.'
t_STR = r'"[^".]*"'
t_XCENTAGE = r'\%'
#t_CHAIN = r'\"[^\"]*\"'
t_TWODOTS = r'\:'

#t_DATATYPEPREMIUM = r" '\[\]int' | '\[\]float' | '\[\]boolean' "


#la creación de una nueva instancia de un objeto
def t_NEW(t):
  r'new'
  t.type = 'NEW'
  return t


#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_ID(t):
  r"[a-zA-Z][a-zA-Z0-9_]*"
  t.type = reserved.get(t.value, "ID")
  return t


# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


def t_COMMENT(t):
  r'\/\/.*'
  pass


#Contruir analizador
lexer = lex.lex()
tokensList = []

def getTokensList(lexer):
  tokensList.clear()
  for tok in lexer:
    product = f'Type: {tok.type} Value: {tok.value} Line: {tok.lineno} Position: {tok.lexpos}'
    tokensList.append(product)

