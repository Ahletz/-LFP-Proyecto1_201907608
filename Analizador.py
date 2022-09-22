from pyparsing import alphanums
from tkinter.filedialog import Open
from Tokens import *
from Errores import *

class Analizando:



    def Analizar(self, direccion):

        #Obtener el contenido del documento
        direccion = direccion
        archivo = open(direccion, encoding='utf-8')
        texto = archivo.read()

        linea = 1 #linea del archivo
        columna = 0 #columna del archivo 
        palabra = '' #contenido 
        estado = 0 # estado inicial 

        #llamar clases Tokens y errores
        token = Token()
        error = Error()

        self.Operaciones = []

        Lista = []

        for i in texto:

            columna +=1 #aumnetar la columna
            
            if i == '\n': #si encuentra un salto de linea
                
                linea+=1 #aumentar linea
                columna = 0 #regresar columna a 0

            if estado == 0:
                
                if i == '<':
                    
                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 1 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 1:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'tipo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 2 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 2:

                if i == '>':
                    
                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 3 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 3:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 4 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 4:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 5 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
            elif estado == 5:

                if i == '=':

                    Tipo = 'IGUAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 6 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 6:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'suma':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'resta':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif palabra.lower().lstrip().rstrip() == 'multiplicacion':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'division':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'potencia':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'raiz':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'inverso':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'seno':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif palabra.lower().lstrip().rstrip() == 'coseno':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'tangente':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'mod':

                    Tipo = 'PALABRA RESERVADA'

                    Lista.append(palabra)

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 7 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 7:

                if i == '>':
                    
                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 8 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 8:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 9 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
            
            elif estado == 9:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'numero':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 10 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 10:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 11 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 11:

                if i.isalnum() or i == '.':

                    palabra += i #agregar las letras a la palabra

                elif i == '<':

                    Tipo = 'NUMERO' #tipo de token
                    Lista.append(palabra)
                    token.Contruccion(Tipo,palabra,linea,columna-1) #agregar numero
                    palabra = '' #limpiar contenido de palabra

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 13 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 13:

                if i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 14 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
            
            elif estado == 14:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'numero':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 15 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 15:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 16 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
            
            elif estado == 16:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 17 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 17:

                if i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 18 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'numero':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 10 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 5 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 18:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 19 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                    self.Operaciones.append(Lista)
                    Lista = []
            
            elif estado == 19:

                if i == '>':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 20 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 20:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 21 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
                    
            
            elif estado == 21:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra

                elif i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 22 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 5 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            
            elif estado == 22:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 23 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            
            elif estado == 23:

                if i == '>':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 24 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 24:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 25 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            
            elif estado == 25:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 26 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'operacion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 5 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 26:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'tipo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 27 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 27:

                if i == '>':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 28 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            
            

            





         

        print()
        print('TOKEN')
        token.Mostrar_token()
        print()
        print('errores')
        error.Mostrar_error()
        print()


        

    def Mostrar(self):

        for i in self.Operaciones:

            for j in i:

                print(j, end='')

            print()
        print('fin')  

        print()

        
        

                
            





                





                












