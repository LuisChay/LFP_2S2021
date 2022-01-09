from prettytable import PrettyTable
from graphviz import Digraph
import numpy as np
import uuid
import webbrowser
import os
from tkinter import *


'''
Parser que reconoce la siguiente gramatica:
INICIO -> INSTRUCCIONES
INSTRUCCIONES -> INSTRUCCION INSTRUCCIONES2
INSTRUCCIONES2 -> INSTRUCCION INSTRUCCIONES2
                   | epsilon
INSTRUCCION -> INSTRUCCION_SUMAR
               |  INSTRUCCION_RESTAR
               | INSTRUCCION_ASIGNACION
INSTRUCCION_SUMAR -> token_sumar parentesisizquierdo palabra coma entero parentesisderecho puntocoma
INSTRUCCION_RESTAR -> token_restar parentesisizquierdo entero coma entero parentesisderecho puntocoma
INSTRUCCION_ASIGNACION -> palabra igual entero puntoycoma
'''
class AnalizadorSintactico:


    def __init__(self,tokens = []):
        self.errores = []
        self.cadenaprint = ""
        self.cadenaprintln = ""
        self.cadenapromedio = ""
        self.cadenasumar = ""
        self.cadenamax = ""
        self.ccadenacontar = ""
        self.cadenamin = ""
        self.datos = {}
        self.registrosaux = []
        self.contadorreg = 0
        self.activador = 0
        self.variablefloat = 0.00
        self.tokens = tokens
        self.saltolinea = '\n'
        self.activadordatos = {}
        self.variablesuma = 0.00
        self.variablemax = 0.00
        self.variablecontarsi = 0
        self.variable2  = 0.00
        #Para sacar el elemento esperado le doy vuelta a la lista de tokens
        self.tokens.reverse()
        self.tabla = {}


    def agregarError(self,obtenido,esperado,fila,columna):
        self.errores.append(
            "<ERROR SINTACTICO> Se obtuvo {}, se esperaba {}. En la Fila: {}, y Columna: {}".format(
                obtenido,
                esperado,
                fila,
                columna
            )
        )
        tmp = self.tokens.pop()
        while tmp.tipo != "puntoycoma":
            tmp = self.tokens.pop()

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Errores"]
        if len(self.errores)==0:
            print(' ')
        else:
            for i in self.errores:
                x.add_row([i])
            cadenaerrores = x.get_html_string()
            cadenaerroresform = "{}".format(cadenaerrores)
            plantilla2 = """
            <html lang="es">
                    <head>
                    <!-- Required meta tags -->

                    <meta charset="utf-8">
                    <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> -->
                    <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->

                    <!-- Bootstrap CSS -->
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

                    <title>Reporte de Errores</title>
                    </head>

                    <body>

                    {cadenaerroresform}

                    <!-- Optional JavaScript; choose one of the two! -->

                    <!-- Option 1: Bootstrap Bundle with Popper -->
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>

                    <!-- Option 2: Separate Popper and Bootstrap JS -->
                    <!--
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
                    -->
                    </body>
                    </html>
                    """.format(**locals())
            file1= open("reporteErroresSintactico.html","w")
            file1.write(plantilla2)
            file1.close()
            webbrowser.open('reporteErroresSintactico.html')


    def analizar(self):
        self.INICIO()
        self.impErrores()

    def INICIO(self):
        self.INSTRUCCIONES()
#--------------------------------------------------------instrucciones----------------------------------------------------

    def INSTRUCCIONES(self):
        self.INSTRUCCION()
        self.INSTRUCCIONES2()

    def INSTRUCCIONES2(self):
        try:
            tmp = self.tokens[-1]
            if tmp.tipo == 'token_claves' or tmp.tipo == 'token_registros' or tmp.tipo == 'token_imprimir' or tmp.tipo == 'token_imprimirln' or tmp.tipo == 'token_conteo' or tmp.tipo == 'token_promedio' or tmp.tipo == 'token_contarsi' or tmp.tipo == 'token_datos' or tmp.tipo == 'token_sumar' or tmp.tipo == 'token_max' or tmp.tipo == 'token_min' or tmp.tipo == 'token_exportarReporte':
                self.INSTRUCCION()
                self.INSTRUCCIONES2()
            else:
                pass
        except:
            pass

    def INSTRUCCION(self):
        try:
            tmp = self.tokens[-1]
            if tmp.tipo == 'token_claves':
                self.INSTRUCCION_CLAVES()
            elif tmp.tipo == 'token_registros':
                self.INSTRUCCION_REGISTROS()
            elif tmp.tipo == 'token_imprimir':
                self.INSTRUCCION_IMPRIMIR()
            elif tmp.tipo == 'token_imprimirln':
                self.INSTRUCCION_IMPRIMIRLN()
            elif tmp.tipo == 'token_conteo':
                self.INSTRUCCION_CONTEO()
            elif tmp.tipo == 'token_promedio':
                self.INSTRUCCION_PROMEDIO()
            elif tmp.tipo == 'token_contarsi':
                self.INSTRUCCION_CONTARSI()
            elif tmp.tipo == 'token_datos':
                self.INSTRUCCION_DATOS()
            elif tmp.tipo == 'token_sumar':
                self.INSTRUCCION_SUMAR()
            elif tmp.tipo == 'token_max':
                self.INSTRUCCION_MAX()
            elif tmp.tipo == 'token_min':
                self.INSTRUCCION_MIN()
            elif tmp.tipo == 'token_exportarReporte':
                self.INSTRUCCION_EXPORTARREPORTE()
        except:
            pass




    def INSTRUCCION_CLAVES(self):
        tmp = self.tokens.pop()

        if tmp.tipo == "token_claves":

            tmp = self.tokens.pop()
            if tmp.tipo == "signoigual":

                tmp = self.tokens.pop()
                if tmp.tipo == "corcheteabr":

                    self.LISTACLAVES()
                    if tmp.tipo == "corchetecer":

                        tmp = self.tokens.pop()
                    else:
                        self.agregarError(
                            tmp.tipo,
                            "corchetecer",
                            tmp.linea,
                            tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "corcheteabr",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "signoigual",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_claves",
                tmp.linea,
                tmp.columna
            )

    def LISTACLAVES(self):
        tmp = self.tokens.pop()

        if tmp.tipo == "cadenacomillas":

            clave = tmp.lexema.replace('""', '')
            self.datos[clave]=[]

            self.CLAVES()
        else:

            self.agregarError(
                tmp.tipo,
                "cadenacomillas",
                tmp.linea,
                tmp.columna
            )

    def CLAVES(self):
        tmp = self.tokens.pop()
        if tmp.tipo == "coma":
            tmp = self.tokens.pop()
            if tmp.tipo == "cadenacomillas":
                clave = tmp.lexema.replace('""', '')

                self.datos[clave]=[]

                self.CLAVES()
            else:
                self.agregarError(
                    tmp.tipo,
                    "cadenacomillas",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.tokens.apppend(tmp)


## REGISTROS
    def INSTRUCCION_REGISTROS(self):
        tmp = self.tokens.pop()
        if tmp.tipo == "token_registros":

            tmp = self.tokens.pop()
            if tmp.tipo == "signoigual":

                tmp = self.tokens.pop()
                if tmp.tipo == "corcheteabr":
                    self.FILA()
                    return

                    if tmp.tipo == "corchetecer":
                        self.registrosaux.reverse()
                        for i in self.datos:
                            self.contadorreg += 1
                            self.datos[i].append(self.registrosaux.pop())

                        return
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "corchetecer",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                else:
                    self.agregarError(
                        tmp.tipo,
                        "corcheteabr",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "signoigual",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_registros",
                tmp.linea,
                tmp.columna
            )


    def FILA(self):

        tmp = self.tokens.pop()
        if  tmp.tipo == "llaveabr":
            self.CAMPO()
            return
        elif tmp.tipo == "corchetecer":
            self.registrosaux.reverse()
            while len(self.registrosaux) > 0:
                for i in self.datos:
                    self.contadorreg += 1
                    self.datos[i].append(self.registrosaux.pop())
        else:
            self.agregarError(
                    tmp.tipo,
                    "llaveabr",
                    tmp.linea,
                    tmp.columna
                )

    def CAMPO(self):
        tmp = self.tokens.pop()

        if tmp.tipo == "cadenacomillas" or tmp.tipo == "entero" or tmp.tipo ==  "decimal":
            #LLENADO
            self.registrosaux.append(tmp.lexema)
            self.CAMPO()
            return

        elif tmp.tipo == "coma":
            self.CAMPO()
            return

        elif tmp.tipo == "llavecer":
            self.FILA()
            return

        else:
            self.agregarError(
                    tmp.tipo,
                    "cadena",
                    tmp.linea,
                    tmp.columna
                )

    '''
    def REGISTRO(self):
        print("llegue a registro")
        tmp = self.tokens.pop()
        if tmp.tipo == "coma":
            self.CAMPO()
            self.REGISTRO()
        else:
            self.FIlA()
            self.tokens.apppend(tmp)
    '''

    def INSTRUCCION_IMPRIMIR(self):
        tmp = self.tokens.pop()
        if tmp.tipo == "token_imprimir":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenaprint += tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            pass
                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_imprimir",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_IMPRIMIRLN(self):
        saltodelinea = '\n'
        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_imprimirln":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenaprintln += saltodelinea
                    self.cadenaprintln += tmp.lexema
                    self.cadenaprintln += saltodelinea
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        ########
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            pass
                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_imprimirln",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_CONTEO(self):

        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_conteo":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "parentesiscerrado":
                    sumando1 = tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "puntocoma":

                        self.activador += self.contadorreg

                    else:
                        self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_conteo",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_PROMEDIO(self):
        tmp = self.tokens.pop()
        if tmp.tipo == "token_promedio":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenapromedio = tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        ########
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            aux1 = []

                            aux1 = self.datos[self.cadenapromedio]

                            cua = 0
                            for j in aux1:
                                if float(j) >= 0:
                                    cua += float(j)
                            avg = (cua / len(aux1))
                            self.variablefloat += avg
                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_promedio",
                tmp.linea,
                tmp.columna
            )


    def INSTRUCCION_CONTARSI(self):

        tmp = self.tokens.pop()
        if tmp.tipo == "token_contarsi":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":

                    #self.cadenacontar += tmp.lexema
                    tmp = self.tokens.pop()

                    if tmp.tipo == "coma":

                        tmp = self.tokens.pop()
                        if tmp.tipo == "entero" or tmp.tipo == "decimal":

                            #self.cantidadcontar += tmp.lexema
                            #print("entero o decimal ")

                            tmp = self.tokens.pop()
                            if tmp.tipo == "parentesiscerrado":


                                tmp = self.tokens.pop()
                                if tmp.tipo == "puntocoma":
                                    pass
                                    '''
                                    aux8 = []
                                    contarsi = self.cantidadcontar

                                    aux8 = self.datos[self.cadenacontar]
                                    print(aux8)
                                    contador = 0

                                    for j in aux8:
                                        print("for")
                                        if j == contarsi:
                                            contador += 1
                                    self.variablecontarsi += contador
                                    '''





                                else:
                                    self.agregarError(
                                    tmp.tipo,
                                    "puntocoma",
                                    tmp.linea,
                                    tmp.columna
                                    )
                                ##########
                            else:
                                self.agregarError(
                                tmp.tipo,
                                "parentesiscerrado",
                                tmp.linea,
                                tmp.columna
                                )
                            ##########
                        else:
                            self.agregarError(
                        tmp.tipo,
                        "entero",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "coma",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_contarsi",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_DATOS(self):

        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_datos":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "parentesiscerrado":
                    sumando1 = tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "puntocoma":

                        self.activadordatos = self.datos


                    else:
                        self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_datos",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_SUMAR(self):

        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_sumar":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenasumar += tmp.lexema

                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        ########
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            aux2 = []

                            aux2 = self.datos[self.cadenasumar]

                            cua = 0
                            for j in aux2:
                                if float(j) >= 0:
                                    cua += float(j)

                            self.variablesuma += cua


                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_sumar",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_MAX(self):
        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_max":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenamax += tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            aux3 = []

                            aux3 = self.datos[self.cadenamax]

                            max = 0
                            for j in aux3:
                                if (float(j) > max):
                                    max = float(j)
                            self.variablemax += max


                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_max",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_MIN(self):
        #Obtiene el siguiente token
        tmp = self.tokens.pop()
        if tmp.tipo == "token_min":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    self.cadenamin += tmp.lexema
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":


                            aux4 = []
                            aux4 = self.datos[self.cadenamin]
                            #min = 0.00
                            '''
                            min = aux4[0]
                            for j in aux4:
                                if (float(j) < min):
                                    min = float(j)
                            '''
                            prueba = float(min(aux4))
                            self.variable2 += prueba


                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,+
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.ce,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_min",
                tmp.linea,
                tmp.columna
            )

    def INSTRUCCION_EXPORTARREPORTE(self):

        tmp = self.tokens.pop()
        if tmp.tipo == "token_exportarReporte":
            tmp = self.tokens.pop()
            if tmp.tipo == "parentesisabierto":
                tmp = self.tokens.pop()
                if tmp.tipo == "cadenacomillas":
                    tmp = self.tokens.pop()
                    if tmp.tipo == "parentesiscerrado":
                        tmp = self.tokens.pop()
                        if tmp.tipo == "puntocoma":
                            print("Reporte creado exitosamente")

                            data = ""
                            for k in self.datos:
                                data += "<td>" + k + "</td>"
                                for d in self.datos[k]:
                                    data += "<td>" + d + "</td>"
                                data += "<tr>"
                            data = "<table border=1>" + data + "<table>"
                            with open("reporte.html", "w") as file:
	                               file.write(data)

                            os.startfile("reporte.html")

                        else:
                            self.agregarError(
                        tmp.tipo,
                        "puntocoma",
                        tmp.linea,
                        tmp.columna
                        )
                        ########
                    else:
                        self.agregarError(
                        tmp.tipo,
                        "parentesiscerrado",
                        tmp.linea,
                        tmp.columna
                        )
                else:
                    self.agregarError(
                        tmp.tipo,
                        "cadenacomillas",
                        tmp.linea,
                        tmp.columna
                    )
            else:
                self.agregarError(
                    tmp.tipo,
                    "parentesisabierto",
                    tmp.linea,
                    tmp.columna
                )
        else:
            self.agregarError(
                tmp.tipo,
                "token_exportarReporte",
                tmp.linea,
                tmp.columna
            )
