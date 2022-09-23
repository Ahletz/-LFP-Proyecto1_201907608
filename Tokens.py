class Token:

    lista = []

    def Lista(self):

        self.lista = []

    def Contruccion(self, tipo, contenido, linea, columna): #contructor de tocken 

        Lista = [tipo,contenido,linea,columna]

        self.lista.append(Lista)

    def Mostrar_token(self):

        for i in self.lista:

            print(i)

    def Reporte_Tokens(self):

        #inicio de thml
         
        inicio = '<!doctype html><html lang="en"> <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><title>TOKENS</title></head><body><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script><h1>Lista de Tokens</h1><table class="table"><thead><tr><th scope="col">Tokens: </th></tr></thead><tbody>'

        #final html

        final = '</tbody></body></html>'
        #contenido de html

        contenido = '<tr>' + '<td>' + 'TIPO' + '</td>' + '<td>' + 'TOKEN' + '</td>' + '<td>' + 'LINEA' + '</td>' + '<td>' + 'COLUMNA' + '</td>' +'</tr>'

        for i in self.lista: #agregar a la tabla los respectivos tokens 

            tokenn = '<tr>' + '<td>' +str(i[0]) + '</td>' + '<td>' +str(i[1]) + '</td>' + '<td>' +str(i[2]) + '</td>' + '<td>' +str(i[3]) + '</td>' +'</tr>'

            contenido += tokenn

        texto = inicio + contenido + final

        op = open('REPORTE TOKENS.html','w')

        op.write(texto)

        op.close()