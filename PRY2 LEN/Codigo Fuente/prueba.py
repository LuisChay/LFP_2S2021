import sys
import tkinter
from tkinter import *
import sys

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from AnalisisLexico import AnalisisLexico

from AnalisisSintactico import AnalizadorSintactico

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


root = tk.Tk()

def analisis():
    #Analisis lexico
    scanner = AnalisisLexico()
    scanner.analizar(Text1.get(1.0, END))
    scanner.reporteTokens()
    scanner.reporteErrores()
    #Analisis sintactico
    sintactico = AnalizadorSintactico(scanner.listaTokens)
    sintactico.analizar()
    Text2.insert(tk.INSERT, sintactico.cadenaprint)
    Text2.insert(tk.INSERT, sintactico.cadenaprintln)
    Text2.insert(tk.INSERT, sintactico.activador)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.variablefloat)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.variablecontarsi)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.activadordatos)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.variablesuma)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.variablemax)
    Text2.insert(tk.INSERT, sintactico.saltolinea)
    Text2.insert(tk.INSERT, sintactico.variable2)
    Text2.insert(tk.INSERT, sintactico.saltolinea)





contenido = None
def leerArchivo():

    Tk().withdraw()
    entrada = askopenfilename(filetypes=[("Archivos LFP", "*.lfp"), ("All Files", "*.*")])
    archivo = open(entrada, 'r')
    global contenido
    contenido = archivo.read()
    Text1.insert(END, contenido)
    archivo.close()


    #return contenido


'''This class configures and populates the rootlevel window.
root is the rootlevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
style = ttk.Style()
if sys.platform == "win32":
    style.theme_use('winnative')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

root.geometry("760x499+302+114")
root.minsize(116, 1)
root.maxsize(2732, 746)
root.resizable(1,  1)
root.title("Proyecto 2")
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")

TLabel1 = ttk.Label(root)
TLabel1.place(relx=0.017, rely=0.022, height=21, width=274)
TLabel1.configure(background="#d9d9d9")
TLabel1.configure(foreground="#000000")
TLabel1.configure(relief="flat")
TLabel1.configure(anchor='w')
TLabel1.configure(justify='left')
TLabel1.configure(text='''PROYECTO 2 // 202000343''')

Button1 = tk.Button(root,  command = leerArchivo)
Button1.place(relx=0.645, rely=0.02, height=24, width=47)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Cargar''')

Button1_1 = tk.Button(root, command = analisis)
Button1_1.place(relx=0.724, rely=0.02, height=24, width=57)
Button1_1.configure(activebackground="#ececec")
Button1_1.configure(activeforeground="#000000")
Button1_1.configure(background="#d9d9d9")
Button1_1.configure(disabledforeground="#a3a3a3")
Button1_1.configure(foreground="#000000")
Button1_1.configure(highlightbackground="#d9d9d9")
Button1_1.configure(highlightcolor="black")
Button1_1.configure(pady="0")
Button1_1.configure(text='''Analizar''')

Text1 = tk.Text(root)
Text1.place(relx=0.013, rely=0.16, relheight=0.81, relwidth=0.483)
Text1.configure(background="white")
Text1.configure(font="TkTextFont")
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="blue")
Text1.configure(selectforeground="white")
Text1.configure(wrap="word")
#Text1.insert("insert", contenido)

TLabel2 = ttk.Label(root)
TLabel2.place(relx=0.017, rely=0.11, height=21, width=160)
TLabel2.configure(background="#d9d9d9")
TLabel2.configure(foreground="#000000")
TLabel2.configure(relief="flat")
TLabel2.configure(anchor='w')
TLabel2.configure(justify='left')
TLabel2.configure(text='''Contenido archivo''')

TLabel2_1 = ttk.Label(root)
TLabel2_1.place(relx=0.526, rely=0.1, height=21, width=160)
TLabel2_1.configure(background="#d9d9d9")
TLabel2_1.configure(foreground="#000000")
TLabel2_1.configure(relief="flat")
TLabel2_1.configure(anchor='w')
TLabel2_1.configure(justify='left')
TLabel2_1.configure(text='''Consola''')

menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
root.configure(menu =  menubar)

Text2 = tk.Text(root)
Text2.place(relx=0.513, rely=0.16, relheight=0.81, relwidth=0.47)
Text2.configure(background="white")
Text2.configure(font="TkTextFont")
Text2.configure(foreground="black")
Text2.configure(highlightbackground="#d9d9d9")
Text2.configure(highlightcolor="black")
Text2.configure(insertbackground="black")
Text2.configure(selectbackground="blue")
Text2.configure(selectforeground="white")
Text2.configure(wrap="word")
#Text2.configure(state='disabled')


root.mainloop()
