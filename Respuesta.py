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

        #colores

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

        cuerpo +='<p><FONT SIZE='+str(estilos[1][1])+' COLOR='+str(estilos[1][1])+'">'+str(texto[0])+'</FONT></p>'

        tipo = ''

        for i in contenido:

            operaciones = 0

            for j in i:

                if j.isalpha():

                    operaciones+=1

            if operaciones ==1:

                tipo +='<FONT SIZE='+str(estilos[2][2])+'COLOR="'+str(estilos[2][1])+'">'+str(i[0])+'</FONT>'
                tipo += '<p>'

                for j in i:

                    if j.isalnum():

                        tipo += str(j) + ' '
                    
                    tipo += '='

                tipo += str(self.operaciones_simples(i)) + '</p>'

                    

            elif operaciones == 2:

                pass

        
        documento = cabecera + cuerpo + tipo + pie

        doc = open('RESPUESTA.html','w')
        doc.write(documento)
        doc.close()
        webbrowser.open_new_tab('RESPUESTA.html')

 

    def operaciones_simples(self, operacion):

        operacion = operacion
        respuesta = 0

        if operacion[0] == 'SUMA':
            

            for i in operacion:

                if i.isdigit():

                    respuesta +=float(i)
            
            return respuesta
            
        elif operacion[0] == 'RESTA':

            for i in operacion:

                if i.isdigit():

                    respuesta -=float(i)
            
            return respuesta

        elif operacion[0] == 'MULTIPLICACION':
            
            for i in operacion:

                if i.isdigit():

                    respuesta *=float(i)
            
            return respuesta

        elif operacion[0] == 'DIVISION':
            
            for i in operacion:

                if i.isdigit():

                    respuesta /=float(i)
            
            return respuesta

        elif operacion[0] == 'POTENCIA':

            respuesta = int(operacion[1])**int(operacion[2])

            return respuesta
            
        elif operacion[0] == 'RAIZ':

            respuesta = math.sqrt(int(operacion[1]))

            return respuesta
            
        elif operacion[0] == 'INVERSO':
            
            respuesta = 1/int(operacion[1])

            return respuesta


        elif operacion[0] == 'SENO':

            respuesta = math.sin(int(operacion[1]))

            return respuesta

        elif operacion[0] == 'COSENO':
            
            respuesta = math.cos(int(operacion[1]))

            return respuesta

        elif operacion[0] == 'TANGENTE':
            
            respuesta = math.tan(int(operacion[1]))

            return respuesta

        elif operacion[0] == 'MOD':
            
            respuesta = int(operacion[1])%int(operacion[2])

            return respuesta 

    def Operaciones_dobles(self, operaciones):

        operacion = operaciones

        if operacion[0] == 'SUMA':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'MULTIPLICACION':

                respuesta = int(operacion[3]) * int(operacion[4])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'DIVISION':

                respuesta = int(operacion[3]) / int(operacion[4])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'POTENCIA':

                respuesta = int(operacion[3])**int(operacion[4])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta + int(operacion[1])

        elif operacion[0] == 'RESTA':

            if operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'MULTIPLICACION':

                respuesta = int(operacion[3]) * int(operacion[4])

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'DIVISION':

                respuesta = int(operacion[3]) / int(operacion[4])

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'POTENCIA':

                respuesta = int(operacion[3])**int(operacion[4])

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta - int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta - int(operacion[1])

        elif operacion[0] == 'MULTIPLICACION':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'DIVISION':

                respuesta = int(operacion[3]) / int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'POTENCIA':

                respuesta = int(operacion[3])**int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta * int(operacion[1])

        elif operacion[0] == 'DIVISION':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'MULTIPLICACION':

                respuesta = int(operacion[3]) * int(operacion[4])

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'POTENCIA':

                respuesta = int(operacion[3])**int(operacion[4])

                respuesta = respuesta + int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta / int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta / int(operacion[1])

        elif operacion[0] == 'MULTIPLICACION':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'DIVISION':

                respuesta = int(operacion[3]) / int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'POTENCIA':

                respuesta = int(operacion[3])**int(operacion[4])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta * int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta * int(operacion[1])

        elif operacion[0] == 'POTENCIA':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'MULTIPLICACION':

                respuesta = int(operacion[3]) * int(operacion[4])

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta ** int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta ** int(operacion[1])


        elif operacion[0] == 'MOD':

            if operacion[2] == 'RESTA':

                respuesta = int(operacion[3]) - int(operacion[4])

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'MULTIPLICACION':

                respuesta = int(operacion[3]) * int(operacion[4])

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'DIVISION':

                respuesta = int(operacion[3]) / int(operacion[4])

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'SUMA':

                respuesta = int(operacion[3]) + int(operacion[4])

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'RAIZ':

                respuesta = math.sqrt(int(operacion[3])) 

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'INVERSO':

                respuesta = 1/ int(operacion[3])

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'SENO':

                respuesta = math.sin(int(operacion[3])) 

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'COSENO':

                respuesta = math.cos(int(operacion[3]))

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'TANGENTE':

                respuesta = math.tan(int(operacion[3]))

                respuesta = respuesta % int(operacion[1])

            elif operacion[2] == 'MOD':

                respuesta = int(operacion[3]) % int(operacion[4])

                respuesta = respuesta % int(operacion[1])

            

            




