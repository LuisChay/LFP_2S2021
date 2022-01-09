import tkinter
from tkinter import *
import sys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from Analisis import AnalisisLexico
from PIL import ImageTk,Image

from reportehtml import get_table
#ventana y botones-------------------------------

ventana = tkinter.Tk()
ventana.title('BITXELART')
ventana.geometry("900x620")

boton1 = tkinter.Button(ventana, text = "Cargar",  command = lambda: leerArchivo())
boton2 = tkinter.Button(ventana, text = "Analizar", command = lambda: analisis())
boton3 = tkinter.Button(ventana, text = "Imagenes y reportes", command = lambda: crearhtml())

boton5 = tkinter.Button(ventana, text = "Original",  command = lambda: originalfoto())
boton6 = tkinter.Button(ventana, text = "Mirror X",  command = lambda: mirrorx())
boton7 = tkinter.Button(ventana, text = "Mirror Y",  command = lambda: mirrory())
boton8 = tkinter.Button(ventana, text = "Double Mirror",  command = lambda: double())
boton4 = tkinter.Button(ventana, text = "Salir", command = lambda: salir())

boton1.pack()
#boton1.place(height=100, width=250, x = 0, y = 0)
boton2.pack()
#boton2.place(height=100, width=250, x = 5, y = 0)
boton3.pack()
#boton3.place(height=100, width=250, x = 10, y = 0)

#boton4.place(height=100, width=250,x = 15, y = 0)
boton5.pack()
boton6.pack()
boton7.pack()
boton8.pack()
boton4.pack()
#boton5.place(height=100, width=250, x = 20, y = 0)


diccionario = {}
#funciones---------------------------------------
def leerArchivo():
    Tk().withdraw()
    entrada = askopenfilename(filetypes=[("Archivos PXLA", "*.pxla"), ("All Files", "*.*")])
    archivo = open(entrada, 'r')
    global contenido
    contenido = archivo.read()
    archivo.close()
    return contenido

def analisis():
    scanner = AnalisisLexico()
    scanner.analizar(contenido)
    scanner.reporteTokens()
    scanner.reporteErrores()

    tokens = scanner.listaTokens

    diccionario['TITULO'] = tokens[2].lexema
    diccionario['ANCHO'] = tokens[6].lexema
    diccionario['ALTO'] = tokens[10].lexema
    diccionario['FILAS'] = int(tokens[14].lexema)
    diccionario['COLUMNAS'] = int(tokens[18].lexema)
    diccionario['CELDAS'] = []
    diccionario['FILTROS'] = []

    contador = -1
    while True:
        if tokens[contador].lexema == 'FILTROS':
            break
        contador -= 1

    for i in range(contador+1,-1):
        if tokens[i].tipo == "MIRRORX":
            diccionario['FILTROS'].append(tokens[i].lexema)

        elif tokens[i].tipo == "MIRRORY":
            diccionario['FILTROS'].append(tokens[i].lexema)

        elif tokens[i].tipo == "DOUBLEMIRROR":
            diccionario['FILTROS'].append(tokens[i].lexema)



    inicio = 24
    tope = len(tokens) + contador

    saltos = 9

    for i in range(inicio,tope,saltos):
        tmp = []
        tmp.append(tokens[i].lexema)
        tmp.append(tokens[i+2].lexema)
        tmp.append(tokens[i+4].lexema)
        tmp.append(tokens[i+6].lexema)
        diccionario['CELDAS'].append(tmp)

    return diccionario



def crearhtml():
    get_table(diccionario['ANCHO'], diccionario['ALTO'], diccionario['FILAS'], diccionario['COLUMNAS'], diccionario['CELDAS'], diccionario['FILTROS'], 'original.html', 'mirrorx.html','mirrory.html','double.html')
    messagebox.showinfo("Felicidades", "Reporte creado exitosamente")


    import imgkit
    config=imgkit.config(wkhtmltoimage=f'C:\Program Files\wkhtmltopdf\\bin\wkhtmltoimage.exe')
    imgkit.from_file('original.html','original.png', config=config)
    imgkit.from_file('mirrorx.html','mirrorx.png', config=config)
    imgkit.from_file('mirrory.html','mirrory.png', config=config)
    imgkit.from_file('double.html','double.png', config=config)

def originalfoto():
    global img
    img = Image.open("original.png")
    test = ImageTk.PhotoImage(img)
    resize = img.resize((200,200), Image.ANTIALIAS)
    nueva = ImageTk.PhotoImage(resize)

    label1 = tkinter.Label(image=nueva)
    label1.image = nueva

    T = Text(ventana, height = 5, width = 25)

    l = Label(ventana, text = "Original")
    l.config(font =("Courier", 14))
    l.pack()

    label1.place(x=15, y=25)

def mirrorx():
    global img2
    img2 = Image.open("mirrorx.png")
    test2 = ImageTk.PhotoImage(img2)
    resize2 = img2.resize((200,200), Image.ANTIALIAS)
    nueva2 = ImageTk.PhotoImage(resize2)

    label2 = tkinter.Label(image=nueva2)
    label2.image = nueva2

    label2.place(x=15, y=300)

    T2 = Text(ventana, height = 5, width = 25)

    l2 = Label(ventana, text = "Mirror X")
    l2.config(font =("Courier", 14))
    l2.pack()

def mirrory():
    global img3
    img3 = Image.open("mirrory.png")
    test3 = ImageTk.PhotoImage(img3)
    resize3 = img3.resize((200,200), Image.ANTIALIAS)
    nueva3 = ImageTk.PhotoImage(resize3)

    label3 = tkinter.Label(image=nueva3)
    label3.image = nueva3

    label3.place(x=600, y=25)

    T3 = Text(ventana, height = 5, width = 25)

    l3 = Label(ventana, text = "Mirror Y")
    l3.config(font =("Courier", 14))
    l3.pack()

def double():
    global img4
    img4 = Image.open("double.png")
    test4 = ImageTk.PhotoImage(img4)
    resize4 = img4.resize((200,200), Image.ANTIALIAS)
    nueva4 = ImageTk.PhotoImage(resize4)

    label4 = tkinter.Label(image=nueva4)
    label4.image = nueva4

    label4.place(x=600, y=300)

    T4 = Text(ventana, height = 5, width = 25)

    l4 = Label(ventana, text = "Double Mirror")
    l4.config(font =("Courier", 14))
    l4.pack()



def salir():
    sys.exit()
#--------------------------------------------------
ventana.mainloop()
