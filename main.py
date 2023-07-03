from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from lexico import *
from sintactico import *
from tkinter import filedialog

def updateList(lst):
    global errorList

    errorList.delete(0,END)

    for line in lst:
        errorList.insert(END, line + '\n')
    if len(lst) == 0:
        errorList.insert(END,'No presenta errores  \n')

def clear():
    GUIinput.set("")

#Conecto mi entrada por texto con el analizador léxico
def lexicalAnalizer():
    entry=GUIinput.get()
    lexer.input(entry)
    getTokensList(lexer)
    updateList(tokensList)  


#Conecto mi entrada por texto con el analizador sintactico
def syntaxSemanticAnalizer(): 
    s = GUIinput.get()
    syntaxValidator(s)  
    updateList(sintaxisErrors)



#Main codigo ventana

panel = Tk()
ventana = Frame(panel,width=800,height=300)
ventana.pack()


title = tk.Label(ventana,text="GOLANG ANALYZER",font=("Times New Roman",20), fg="black", bg="aliceblue").grid(row=0,column=0, columnspan=2)
lbl1 = tk.Label( ventana,text="Input data for testing",fg="black").grid(row=1,column=0)
GUIinput = tk.StringVar()
tk.Entry(ventana,textvariable=GUIinput, font=("Arial",8), width=90, bg="aliceBlue").grid(row=2,column=0, rowspan=3, sticky="nsew")
lexicBttn = tk.Button(ventana,text="RUN LEXICAL ANALISIS",  command=lexicalAnalizer).grid(row=2,column=1)
syntaxSemanticBttn = tk.Button(ventana,text="RUN SYNTACTICAL AND SEMANTIC",  command=syntaxSemanticAnalizer).grid(row=3,column=1)
clearBttn = tk.Button(ventana,text="CLEAR INPUT",  command=clear).grid(row=4,column=1)
lbl2=tk.Label(ventana,text="",fg="black", bg="ivory").grid(row=5,column=0, columnspan=2)

#Configuracion de Consola

errorList = Listbox(ventana, width=100)
errorList.grid(row=6,column=0, columnspan=2, sticky="nsew")



ventana.mainloop()