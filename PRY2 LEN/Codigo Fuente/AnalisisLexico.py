from Token import Token
from Error import Error
from prettytable import PrettyTable
import webbrowser


class AnalisisLexico:

    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0


    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido.', linea, columna))

    def estado0(self,caracter):
        if caracter.isalpha():
            self.buffer += caracter
            self.columna+=1
            self.estado = 1
        elif caracter == '=':
            self.buffer += caracter
            self.columna+=1
            self.estado = 2
        elif caracter == '"':
            self.buffer += caracter
            self.columna+=1
            self.estado = 3
        elif caracter == ";":
            self.buffer += caracter
            self.columna+=1
            self.estado = 4
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
            self.estado = 5
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
            self.estado = 6
        elif caracter == "{":
            self.buffer += caracter
            self.columna+=1
            self.estado = 7
        elif caracter == "[":
            self.buffer += caracter
            self.columna+=1
            self.estado = 8
        elif caracter ==",":
            self.buffer += caracter
            self.columna+=1
            self.estado = 9
        elif caracter == "]":
            self.buffer += caracter
            self.columna+=1
            self.estado = 10
        elif caracter == "}":
            self.buffer += caracter
            self.columna+=1
            self.estado = 11
        elif caracter == "(":
            self.buffer += caracter
            self.columna+=1
            self.estado = 12
        elif caracter == ")":
            self.buffer += caracter
            self.columna+=1
            self.estado = 13
        elif caracter == "#":
            self.buffer += caracter
            self.columna+=1
            self.estado = 14
        elif caracter == "'":
            self.buffer += caracter
            self.columna+=1
            self.estado = 15


        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        elif caracter == '\r':
            pass

        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1


    def estado1(self,caracter):
        if caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        else:
            if self.buffer =="Claves":
                self.agregar_token(self.buffer,'token_claves',self.linea,self.columna)
            elif self.buffer == "Registros":
                self.agregar_token(self.buffer,'token_registros',self.linea,self.columna)
            elif self.buffer == "imprimir":
                self.agregar_token(self.buffer,'token_imprimir',self.linea,self.columna)
            elif self.buffer == "imprimirln":
                self.agregar_token(self.buffer,'token_imprimirln',self.linea,self.columna)
            elif self.buffer == "conteo":
                self.agregar_token(self.buffer,'token_conteo',self.linea,self.columna)
            elif self.buffer == "promedio":
                self.agregar_token(self.buffer,'token_promedio',self.linea,self.columna)
            elif self.buffer == "contarsi":
                self.agregar_token(self.buffer,'token_contarsi',self.linea,self.columna)
            elif self.buffer == "datos":
                self.agregar_token(self.buffer,'token_datos',self.linea,self.columna)
            elif self.buffer == "sumar":
                self.agregar_token(self.buffer,'token_sumar',self.linea,self.columna)
            elif self.buffer == "max":
                self.agregar_token(self.buffer,'token_max',self.linea,self.columna)
            elif self.buffer == "min":
                self.agregar_token(self.buffer,'token_min',self.linea,self.columna)
            elif self.buffer == "exportarReporte":
                self.agregar_token(self.buffer,'token_exportarReporte',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado2(self,caracter):
        if caracter == "=":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'signoigual',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado3(self,caracter):
        if caracter == '"':
            self.buffer+=caracter
            self.columna+=1
        elif caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        elif caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "_":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "*":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "/":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "\\":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "!":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "#":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "$":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "%":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == "&":
            self.buffer+=caracter
            self.columna+=1
        elif caracter == " ":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'cadenacomillas',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado4(self,caracter):
        if caracter == ";":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'puntocoma',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado5(self,caracter):
        if caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        elif caracter == ".":
            self.estado = 6
            self.columna+=1
            self.buffer+=caracter
        else:
            self.agregar_token(self.buffer,'entero',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado6(self,caracter):
        if caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'decimal',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado7(self,caracter):
        if caracter == "{":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'llaveabr',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado8(self,caracter):
        if caracter == "[":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'corcheteabr',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado9(self,caracter):
        if caracter == ",":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'coma',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1


    def estado10(self,caracter):
        if caracter == "]":
            self.buffer+=caracter
            self.columna+=1
            self.linea+=1
        else:
            self.agregar_token(self.buffer,'corchetecer',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado11(self,caracter):
        if caracter == "}":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'llavecer',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado12(self,caracter):
        if caracter == "(":
            self.buffer+=caracter
            self.columna+=1
        elif caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'parentesisabierto',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado13(self,caracter):
        if caracter == ")":
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'parentesiscerrado',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado14(self,caracter):
        if caracter == "#":
            self.buffer+=caracter
            self.columna+=1
        elif caracter != "\n":
            self.buffer+=caracter
            self.columna+=1
        else:
            #self.agregar_token(self.buffer,'comentario',self.linea,self.columna)
            self.estado = 0
            self.buffer = ''
            self.columna+=1
            self.i -= 1

    def estado15(self,caracter):
        if caracter == "´":
            self.buffer+=caracter
            self.columna+=1
        elif caracter != "\n":
            self.buffer+=caracter
            self.columna+=1
        else:
            #self.agregar_token(self.buffer,'comentariomulti',self.linea,self.columna)
            self.buffer = ''
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def analizar(self, cadena):
        '''Analiza léxicamente una cadena'''
        self.listaTokens = []
        self.listaErrores = []
        centinela = '$'
        cadena += centinela

        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado == 1:
                self.estado1(cadena[self.i])
            elif self.estado == 2:
                self.estado2(cadena[self.i])
            elif self.estado == 3:
                self.estado3(cadena[self.i])
            elif self.estado == 4:
                self.estado4(cadena[self.i])
            elif self.estado == 5:
                self.estado5(cadena[self.i])
            elif self.estado == 6:
                self.estado6(cadena[self.i])
            elif self.estado == 7:
                self.estado7(cadena[self.i])
            elif self.estado == 8:
                self.estado8(cadena[self.i])
            elif self.estado == 9:
                self.estado9(cadena[self.i])
            elif self.estado == 10:
                self.estado10(cadena[self.i])
            elif self.estado == 11:
                self.estado11(cadena[self.i])
            elif self.estado == 12:
                self.estado12(cadena[self.i])
            elif self.estado == 13:
                self.estado13(cadena[self.i])
            elif self.estado == 14:
                self.estado14(cadena[self.i])
            elif self.estado == 15:
                self.estado15(cadena[self.i])
            self.i += 1

    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarDataTok())
        print(x)

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarDataErr())
            print(x)

    def reporteTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarDataTok())
        cadenatokens = x.get_html_string()
        cadenatokensform = "{}".format(cadenatokens)
        plantilla1 = """
        <html lang="es">
                <head>
                <!-- Required meta tags -->

                <meta charset="utf-8">
                <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> -->
                <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->

                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

                <title>Reporte de Tokens</title>
                </head>

                <body>

                {cadenatokensform}

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
        file1= open("reporteTokens.html","w")
        file1.write(plantilla1)
        file1.close()
        webbrowser.open('reporteTokens.html')



    def reporteErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarDataErr())
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
            file1= open("reporteErrores.html","w")
            file1.write(plantilla2)
            file1.close()
            webbrowser.open('reporteErrores.html')
