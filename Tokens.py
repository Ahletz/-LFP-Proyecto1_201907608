class Token:

    lista = []

    def Lista(self):

        self.lista = []

    def Contruccion(self, tipo, contenido, linea, columna): #contructor de tocken 

        a1 = 'Tokent tipo: ( '
        a2 = ' ) Token: "'
        a3 = '" Linea: '
        a4 = ' Columna: '

        token = a1 + tipo + a2 + contenido + a3 + str(linea) + a4 + str(columna) #contruccion del tocken 

        self.lista.append(token)

    def Mostrar_token(self):

        for i in self.lista:

            print(i)