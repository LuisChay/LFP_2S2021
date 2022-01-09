from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile


def menu():
    print("==========PRACTICA 1==========")
    print("Selecciona una opción")
    print("\t1 - Cargar Archivo")
    print("\t2 - Mostrar Reporte")
    print("\t3 - Exportar Reporte")
    print("\t4 - Salir")
    print("==============================")
    print("")


while True:
    menu()
    opcionMenu = input("Eliga una opcion >> ")

    if opcionMenu == "1":
        print("")
        try:
            # APERTURA ARCHIVO
            listamadre = []
            listanombres = []
            listafinal = []
            listainicio = []
            listamin = []

            Tk().withdraw()
            entrada = askopenfilename(
                filetypes=[("Archivos LFP", "*.lfp"), ("All Files", "*.*")])

            entrada = open(entrada, 'r')

            linea = entrada.readline()

            while linea:
                llave = False
                if linea.strip() != '':
                    for letra in linea:
                        if letra == "{":
                            lineainicio = linea.replace('{', '').replace(
                                "_", ' ').replace("=", '').replace("\n", '')
                            listainicio.append(lineainicio)
                            # lineainicio = lineainicio.strip()
                            # listainicio = lineainicio.split("_")
                            llave = True
                        elif letra == "}":
                            lineafinal = linea.replace(
                                '}', '').replace(" ", '')
                            lineafinal = lineafinal.strip()
                            listafinal = lineafinal.split(",")
                            llave = True
                    if llave is False:
                        lineaactual = linea.strip()
                        linealimpia = lineaactual.replace("<", '').replace(">", '').replace(
                            ",", '').replace('"', '').replace("=", '').replace("_", ' ')

                        listanombres = linealimpia.split(";")
                        nota = listanombres[1]
                        nota = int(nota)
                        listamadre.append([listanombres[0], nota])

                linea = entrada.readline()
            entrada.close
            titulo = listainicio[0]
            listaformateada = '{}'.format(listamadre)
            # PALABRAS CLAVES (ultima linea)
            # ltimopre = listamadre.pop()

            # ultimo1 = ultimopre.replace("}", '')
            # ultimo = ultimo1.replace(",", '')

            # claves = ultimo.split()

            # TITULO (primera linea)
            # titulolista = listamadre.pop(0)

            # titulolista3 = titulolista.replace("{", '')
            # titulolista2 = titulolista3.replace("=", '')
            # titulolimpio = titulolista2.replace("_", ' ')

            # print(titulolimpio)
            # print(claves)

            print("Archivo procesado")

            print("")
        except entrada:
            print("Hubo un problema con el archivo")

    elif opcionMenu == "2":
        # ANALISIS
        print("")
        print(">> Curso: ", listainicio[0], sep='')
        print("")
        print(">> El total de estudiantes que contiene el archivo es: ",
              len(listamadre), sep='\n')
        print("")

        cantidad = str(len(listamadre))


        cantidadformateada = "{}".format(cantidad)

        print(">> La información de los estudiantes en el archivo es la siguiente: ")
        print("")
        print(listamadre)
        print("")
        print("<<==========REPORTES==========>>")
        print("")
        promedioformateado = 0
        minimoformateado = 0
        maximoformateado = 0
        aprobadoformateado = 0
        reprobadoformateado = 0

        for palabraclave in listafinal:

            if palabraclave == "ASC":
                print("** Notas de los estudiantes de forma ascendente")
                print("")

                for j in range(len(listamadre)):
                    cambio = False
                    i = 0
                    while i < len(listamadre)-1:
                        if listamadre[i][1] > listamadre[i+1][1]:
                            listamadre[i][1], listamadre[i
                                                         + 1][1] = listamadre[i+1][1], listamadre[i][1]
                            cambio = True
                        i = i+1
                    if cambio is False:
                        break

                print(listamadre)
                print("")
            elif palabraclave == "DESC":

                print("** Notas de los estudiantes de forma descendente")
                print("")

                for j in range(len(listamadre)):
                    cambio2 = False
                    i = 0
                    while i < len(listamadre)-1:
                        if listamadre[i][1] < listamadre[i+1][1]:
                            listamadre[i][1], listamadre[i
                                                         + 1][1] = listamadre[i+1][1], listamadre[i][1]
                            cambio2 = True
                        i = i+1
                    if cambio2 is False:
                        break
                print(listamadre)
                print("")

            elif palabraclave == "AVG":
                print("** Promedio de los estudiantes")
                print("")
                i = 0
                cua = 0
                for j in range(len(listamadre)):
                    if listamadre[i][1] >= 0:
                        cua += listamadre[i][1]
                    i = i+1
                avg = (cua / len(listamadre))
                print(">> La nota promedio es: ", avg, sep='')
                print("")

                promedio = str(avg)
                promedioformateado = "{}".format(promedio)

            elif palabraclave == "MIN":
                print("** Nota minima de los estudiantes")
                print("")

                i = 0
                grande = 100
                for j in listamadre:

                    if grande >= listamadre[i][1]:

                        grande = listamadre[i][1]
                        i += 1

                # minima = Minimo(listamadre)

                print(">> La nota minima de los estudiantes es: ", grande, sep='')
                print("")

                minimo = str(grande)
                minimoformateado = "{}".format(minimo)

            elif palabraclave == "MAX":
                print("** Nota maxima de los estudiantes")
                print("")
                i = 0
                pequeno = 0
                for k in listamadre:
                    # print(listamadre[i][1])
                    if pequeno < listamadre[i][1]:
                        pequeno = listamadre[i][1]
                        i += 1
                # maximo = Maximo(listamadre)

                print(">> La nota maxima de los estudiantes es: ", pequeno, sep='')

                print("")
                maximo = str(pequeno)
                maximoformateado = "{}".format(maximo)

            elif palabraclave == "APR":

                print("** Estudiantes aprobados")
                print("")

                i = 0
                apr = 0
                for j in range(len(listamadre)):
                    if listamadre[i][1] >= 61:
                        apr += 1
                    i = i+1

                print(">> El numero de estudiantes aprobados es: ", apr, sep='')
                print("")

                aprobado = str(apr)
                aprobadoformateado = "{}".format(aprobado)

            elif palabraclave == "REP":
                print("** Estudiantes reprobados")
                print("")

                i = 0
                cuan = 0
                for j in range(len(listamadre)):
                    if listamadre[i][1] <= 61:
                        cuan += 1
                    i = i+1

                print(">> El numero de estudiantes reprobados es: ", cuan, sep='')
                print("")

                reprobado = str(cuan)
                reprobadoformateado = "{}".format(reprobado)

            else:
                print("Fallo al detectar la palabra clave")

    elif opcionMenu == "3":
        print("")

        Tk().withdraw()
        reporte = asksaveasfile(
            filetypes=[("HTML", "*.html"), ("All Files", "*.*")])

        plantilla = """
                <html lang="es">
                <head>
                <!-- Required meta tags -->

                <meta charset="utf-8">
                <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> -->
                <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->

                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

                <title>Reporte de curso</title>
                </head>

                <body>
                <p class="text-center fw-bold">** REPORTE DEL CURSO **</p>
                <p class="text-center fw-bold">Curso:</p>
                <p class="text-center">{titulo}</p>
                <p class="text-center fw-bold">Cantidad de estudiantes:</p>
                <p class="text-center">{cantidadformateada}</p>
                <p class="text-center fw-bold">Listado de estudiantes:</p>
                <p class="text-center">{listaformateada}</p>




                <p class="text-center fw-bold">** REPORTES **</p>
                <p class="text-center fw-bold">Notas en orden ascendente:</p>
                <p class="text-center fw-bold">Notas en orden descendente:</p>
                <p class="text-center fw-bold">Promedio:</p>
                <p class="text-center">{promedioformateado}</p>
                <p class="text-center fw-bold">Nota m&iacute;nima:</p>
                <p class="text-center">{minimoformateado}</p>
                <p class="text-center fw-bold">Nota m&aacute;xima:</p>
                <p class="text-center">{maximoformateado}</p>
                <p class="text-center fw-bold">Estudiantes aprobados:</p>
                <p class="text-center">{aprobadoformateado}</p>
                <p class="text-center fw-bold">Estudiantes reprobados:</p>
                <p class="text-center">{reprobadoformateado}</p>

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

        reporte.write(plantilla)
        reporte.close()

        print("El reporte ha sido generado")
        print("")

    elif opcionMenu == "4":
        print("")
        print("Gracias por usar el programa, que tenga un buen día :)")
        print("")
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\n Pulse una tecla para continuar ")
        input("No has pulsado ninguna opción correcta...\n Pulse una tecla para continuar ")
