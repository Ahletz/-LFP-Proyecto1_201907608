import math
from turtle import position
from pyparsing import alphanums
import webbrowser

class Html_r:

    def Crear(self, Posicion, Contenido, texto, estilos):

        orden = Posicion

        contenido = Contenido

        texto = texto

        estilos = estilos

        #cAMBIO DE COLORES 

        for i in estilos:

            if i[1] == 'AMARILLO':

                i[1] = 'yellow'

            elif i[1] == 'ROJO':

                i[1] = 'red'
            
            elif i[1] == 'VERDE':

                i[1] = 'green'

            elif i[1] == 'ROSADO':

                i[1] = 'pink'

            elif i[1] == 'GRIS':

                i[1] = 'gray'

            elif i[1] == 'AZUL':

                i[1] = 'blue'

            elif i[1] == 'ANARANJADO':

                i[1] = 'orange'

            elif i[1] == 'CAFE':

                i[1] = 'brown'

            elif i[1] == 'NEGRO':

                i[1] = 'black'

        cabecera = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>'
        pie = '</body></html>'

        cuerpo = ''

        cuerpo +='RESPUESTA'+'</title></head><body>'+'<h1>'+'<FONT SIZE='+str(estilos[0][1])+' COLOR='+str(estilos[0][2])+'">'+str(Posicion[0])+'</FONT>'+'</h1>'

        
        titulo ='<p><FONT SIZE='+str(estilos[1][1])+' COLOR='+str(estilos[1][1])+'">'+str(texto[0])+'</FONT></p>'

        tipo = ''

        

        for i in contenido:

            contador = 0

            for j in i:

                if j.isalpha():

                    contador += 1 #saber cuantas operaciones existen dentro del documento
            
            if contador == 1:

                tip = i[0]

                tipo +='<p>'+ tip + '</p>' + '<p>'

                for j in range(1, len(i)):

                    numero = str(i[j])

                    tipo += numero + ' -> '

                tipo = tipo[:-3]
                tipo += '=' 

                resultado = self.operaciones_simples(i)

                tipo += str(resultado) + '</p>' 

            elif contador >= 2:

                tip = i[0]

                tipo +='<p>'+ tip + '</p>' + '<p>'

                lugar = 0

                for j in i:

                    lugar +=1

                    if j.isalpha():

                        break

                for k in range(1, lugar-1):
                    pass



                

            




        

        
        documento = cabecera + cuerpo + titulo + tipo + pie

        doc = open('RESPUESTA.html','w')
        doc.write(documento)
        doc.close()
        webbrowser.open_new_tab('RESPUESTA.html')

 

    def operaciones_simples(self, operacion):

        respuesta = 0

        if operacion[0] == 'SUMA':

            for i in range(1, len(operacion)):

                respuesta += float(operacion[i])

        elif operacion[0] == 'RESTA':

            respuesta = float(operacion[1])

            for i in range(2, len(operacion)):

                respuesta = respuesta - float(operacion[i])
        
        elif operacion[0] == 'MULTIPLICACION':

            respuesta = float(operacion[1])

            for i in range(1, len(operacion)):

                respuesta = respuesta * float(operacion[i])

        elif operacion[0] == 'DIVISION':

            respuesta = float(operacion[1])

            for i in range(1, len(operacion)):

                respuesta = respuesta / float(operacion[i])

        elif operacion[0] == 'POTENCIA':

            respuesta = float(operacion[1])**float(operacion[1])

        elif operacion[0] == 'RAIZ':
            
            respuesta = math.sqrt(float(operacion[1]))

        elif operacion[0] == 'INVERSO':
            
            respuesta = 1/float(operacion[1])

        elif operacion[0] == 'SENO':
            
            respuesta = math.sin(float(operacion[1]))
        
        elif operacion[0] == 'COSENO':
            
            respuesta = math.cos(float(operacion[1]))

        
        elif operacion[0] == 'TANGENTE':
            
            respuesta = math.tan(float(operacion[1]))

        elif operacion[0] == 'MOD':
            
            respuesta = float(operacion[1])%float(operacion[2])

        return respuesta



            

            




