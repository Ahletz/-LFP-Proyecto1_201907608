from pyparsing import alphanums
from tkinter.filedialog import Open
from Tokens import *
from Errores import *
from Respuesta import *
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
        self.Texto = []
        self.Funciones = []
        self.Estilos = []

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
                
                elif palabra.lower().lstrip().rstrip() == 'texto':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 28 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'funcion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 33 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'estilo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 47 #cambio de estado
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
 
                    estado = 0 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores


            elif estado == 28:

                if i == '>':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 29 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 29:

                if i.isalpha() or i == ' ' or i.isalnum() or i == ',' or i == '.' or i == '{' or i == '}' or i == ';' or i == ':' or i == '[' or i == ']' or i == '-' or i == '_' or i == '+' or i == '*' or i == '¿' or i == '?' or i == '!' or i == '¡' or i == '/' or i == '(' or i == ')' or i == '#' or i == '%' or i == '&' :

                    palabra += i #agregar las letras a la palabra

                elif i == '<':

                    Tipo = 'texto' #tipo de token
                    palabra = palabra.lstrip().rstrip()
                    Lista.append(palabra)
                    self.Texto.append(Lista)
                    token.Contruccion(Tipo,palabra,linea,columna-1) #agregar numero
                    palabra = '' #limpiar contenido de palabra

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 30 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                    Lista = []
                
                elif i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 30:

                if i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 31 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
            
            elif estado == 31:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'texto':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 32 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 32:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 0 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            
            elif estado == 33:

                if i == '=':

                    Tipo = 'IGUAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 34 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 34:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'escribir':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 35 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
            elif estado == 35:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 36 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 36:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 37 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 37:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'titulo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'descripcio':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'contenido':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            
            elif estado == 38:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 39 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 39:

                if i.isalpha() or i == '[' or i == ']':

                    palabra += i #agregar las letras a la palabra

                elif i == '<':

                    Tipo = 'PALABRA RESERVADA' #tipo de token
                    palabra = palabra.lstrip().rstrip()
                    Lista.append(palabra)
                    self.Funciones.append(Lista)
                    token.Contruccion(Tipo,palabra,linea,columna-1) #agregar numero
                    palabra = '' #limpiar contenido de palabra

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 40 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                    Lista = []
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 40:

                if i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 41 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 41:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 
                
                else:

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'titulo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 42 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'descripcion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 42 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'contenido':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 42 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 42:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 43 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores
            
            elif estado == 43:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 44 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 44:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 45 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'titulo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'descripcion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif palabra.lower().lstrip().rstrip() == 'contenido':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 38 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 45:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'funcion':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 46 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 46:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 0 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 47:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 48 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 48:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 49 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 49:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
                elif i == ' ':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    Lista.append(palabra)

                    estado = 50 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
                
            
                elif i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                

            elif estado == 50:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'color':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 51 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 51:

                if i == '=':

                    Tipo = 'IGUAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 52 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 52:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra

                elif i == ' ':

                    Tipo = 'PALABRA RESERVADA' #tipo de token
                    Lista.append(palabra)
                    token.Contruccion(Tipo,palabra,linea,columna-1) #agregar numero
                    palabra = '' #limpiar contenido de palabra
 
                    estado = 53 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 53:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'tamanio':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 54 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 54:

                if i == '=':

                    Tipo = 'IGUAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 55 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 55:

                if i.isalnum():

                    palabra += i #agregar las letras a la palabra

                elif i == '/':

                    Tipo = 'Numero' #tipo de token
                    Lista.append(palabra)
                    token.Contruccion(Tipo,palabra,linea,columna-1) #agregar numero
                    palabra = '' #limpiar contenido de palabra

                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 56 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                    self.Estilos.append(Lista)
                    Lista = []
                
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores


            elif estado == 56:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 57 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 57:

                if i == '<':

                    Tipo = 'MENOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 58 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

            elif estado == 58:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra

                elif i == ' ':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna-1)

                    Lista.append(palabra)

                    estado = 50 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

                elif i == '/':
                    
                    Tipo = 'DIAGONAL' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 59 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                

            elif estado == 59:

                if i.isalpha():

                    palabra += i #agregar las letras a la palabra
                
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

                if palabra.lower().lstrip().rstrip() == 'estilo':

                    Tipo = 'PALABRA RESERVADA'

                    token.Contruccion(Tipo,palabra,linea,columna)

                    estado = 60 #cambio de estado
                    palabra = '' #limpiar contenido de palabra

            elif estado == 60:

                if i == '>':

                    Tipo = 'MAYOR QUE' #tipo de token
                    palabra = i #contenido leido

                    token.Contruccion(Tipo,palabra,linea,columna)
 
                    estado = 0 #cambio de estado
                    palabra = '' #limpiar contenido de palabra
            
                elif i == ' ' or i == '\n' or i == '\t':

                    continue #si vienen espacio 

                else: 

                    error.Crear(i,linea,columna) #lista de errores

        
        token.Reporte_Tokens()
        error.Reporte_Errores()




        print()
        print('TOKEN')
        token.Mostrar_token()
        print()
        print('errores')
        error.Mostrar_error()
        print()

        respuesta = Html_r()
        respuesta.Crear(self.Funciones, self.Operaciones,self.Texto, self.Estilos)

        

    def Mostrar(self):

        for i in self.Operaciones:

                print(i)

        print()
        print('fin')  

        print()

        for h in self.Texto:

            print(h)
        print()

        for k in self.Funciones:

            print(k)

            print()

        for l in self.Estilos:

            print(l)

        print()


   

        

        
        

                
            





                





                












