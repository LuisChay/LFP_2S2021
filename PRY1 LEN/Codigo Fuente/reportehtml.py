def get_table(ancho,alto,filas,columnas,celdas,filtros, nombre_archivo_og, nombre_archivo_x, nombre_archivo_y, nombre_archivo_db):
    head = '<table>\n'
    body = ''
    bottom = '</table>'
    matriz = []


    for i in range(0,filas):
        fila_temporal = []
        for j in range(0,columnas):
            fila_temporal.append(crearceldavacia(ancho, alto))
        matriz.append(fila_temporal)


    for celda in range(0, len(celdas)-1):
        if celdas[celda][2] == "FALSE":
            matriz[int(celdas[celda][1])][int(celdas[celda][0])] = crearceldavacia(ancho, alto)
        else:
            matriz[int(celdas[celda][1])][int(celdas[celda][0])] = crearcelda(ancho, alto, celdas[celda][3])

    for fila in range(0,filas):
        body += '\t<tr>'
        for columna in range(0,columnas):
            body+=matriz[fila][columna]
        body += '\t</tr>'


    html = open(nombre_archivo_og,'w+')
    html.write(head+body+bottom)


    for filtro in filtros:

        if filtro == "MIRRORX":
            head = '<table>\n'
            body = ''
            bottom = '</table>'
            matriz = []


            for i in range(0,filas):
                fila_temporal = []
                for j in range(0,columnas):
                    fila_temporal.append(crearceldavacia(ancho, alto))
                matriz.append(fila_temporal)


            for celda in range(0, len(celdas)-1):
                if celdas[celda][2] == "FALSE":
                    matriz[int(celdas[celda][1])][(filas) -1 - int(celdas[celda][0])] = crearceldavacia(ancho, alto)
                else:
                    matriz[int(celdas[celda][1])][(filas) -1 - int(celdas[celda][0])] = crearcelda(ancho, alto, celdas[celda][3])

            for fila in range(0,filas):
                body += '\t<tr>'
                for columna in range(0,columnas):
                    body+=matriz[fila][columna]
                body += '\t</tr>'

                html = open(nombre_archivo_x,'w+')
                html.write(head+body+bottom)

        elif filtro == "MIRRORY":
            head = '<table>\n'
            body = ''
            bottom = '</table>'
            matriz = []


            for i in range(0,filas):
                fila_temporal = []
                for j in range(0,columnas):
                    fila_temporal.append(crearceldavacia(ancho, alto))
                matriz.append(fila_temporal)


            for celda in range(0, len(celdas)-1):
                if celdas[celda][2] == "FALSE":
                    matriz[(columnas) -1 - int(celdas[celda][1])][int(celdas[celda][0])] = crearceldavacia(ancho, alto)
                else:
                    matriz[(columnas) -1 - int(celdas[celda][1])][int(celdas[celda][0])] = crearcelda(ancho, alto, celdas[celda][3])

            for fila in range(0,filas):
                body += '\t<tr>'
                for columna in range(0,columnas):
                    body+=matriz[fila][columna]
                body += '\t</tr>'

            html = open(nombre_archivo_y,'w+')
            html.write(head+body+bottom)

        elif filtro == "DOUBLEMIRROR":
            head = '<table>\n'
            body = ''
            bottom = '</table>'
            matriz = []


            for i in range(0,filas):
                fila_temporal = []
                for j in range(0,columnas):
                    fila_temporal.append(crearceldavacia(ancho, alto))
                matriz.append(fila_temporal)


            for celda in range(0, len(celdas)-1):
                if celdas[celda][2] == "FALSE":
                    matriz[(columnas) -1 - int(celdas[celda][1])][(filas) -1 - int(celdas[celda][0])] = crearceldavacia(ancho, alto)
                else:
                    matriz[(columnas) -1 - int(celdas[celda][1])][(filas) -1 - int(celdas[celda][0])] = crearcelda(ancho, alto, celdas[celda][3])

            for fila in range(0,filas):
                body += '\t<tr>'
                for columna in range(0,columnas):
                    body+=matriz[fila][columna]
                body += '\t</tr>'

            html = open(nombre_archivo_db,'w+')
            html.write(head+body+bottom)




def crearcelda(texto1, texto2, texto3):
        return '\t\t<td width="{}" height="{}" bgcolor="{}"></td>\n'.format(texto1, texto2, texto3)

def crearceldavacia(texto1, texto2):
        return '\t\t<td width="{}" height="{}"></td>\n'.format(texto1, texto2)
