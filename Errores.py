class Error:


    lista = []

    def Lista(self):

         self.lista = [] # lista de errores

    def Crear(self, contenido, linea, columna):

        a1 = 'Erorr: '
        a2 = ' ,Linea: '
        a3 = ' ,Columna: '

        error = a1 + contenido + a2 + str(linea) + a3 + str(columna) #contrucccion de un error

        self.lista.append(error) #agregar error a la lista
