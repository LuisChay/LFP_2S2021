class Token:

    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo

    def enviarDataTok(self):
        return [self.lexema, self.tipo, self.linea, self.columna]
