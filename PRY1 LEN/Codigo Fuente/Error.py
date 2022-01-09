class Error:

    def __init__(self, descripcion, linea, columna):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna

    def enviarDataErr(self):
        return [self.descripcion,self.linea, self.columna]
