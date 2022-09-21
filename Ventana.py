from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Edicion import *

class Ventana:

    direccion =''
    

    def __init__(self):

        print('INICIANDO PROGRAMA...')

    
    #METODO DE INICIACION VENTANA PRINCIPAL
    def Window(self):

        self.ventana = Tk()
        self.ventana.geometry('600x500+550+150')
        self.ventana.configure(background='turquoise1')
        self.ventana.title('Analizador')
        self.ventana.resizable(False,False)

        Frane1 = Frame(self.ventana,width=250, height=350, relief='sunken',bd=5,background='deep sky blue').place(x=30,y=100)
        Frane2 = Frame(self.ventana,width=250, height=350, relief='sunken',bd=5,background='SpringGreen2').place(x=330,y=100)

        self.Etiquetas()
        self.Botones()
        
        self.ventana.mainloop()

        

    #DATOS DEL ESTUDIANTE MEDIANTE LABELS
    def Etiquetas(self):

        #ETIQUETAS PARA LOS FRAME

        label1 = Label(text='Archivos',background='deep sky blue',font=('Arial', 16)).place(x=115,y=80)
        label2 = Label(text='Ayuda',background='SpringGreen2',font=('Arial', 16)).place(x=425,y=80)


    #BOTONES DE LA PANTALLA PRINCIPAL
    def Botones(self):
        
        #BOTONES PARA MANIPULAR ARCHIVO
        boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo,height=2,width=15,background='DodgerBlue2').place(x=100,y=150)
        boton2 = Button(text='Editar',height=2,width=15,background='DodgerBlue2',command=self.Edicion).place(x=100,y=200)
        boton3 = Button(text='Analizar',height=2,width=15,background='DodgerBlue2').place(x=100,y=250)
        boton4 = Button(text='Errores',height=2,width=15,background='DodgerBlue2').place(x=100,y=300)
        boton5 = Button(text='Salir',command=self.ventana.destroy,height=2,width=15,background='DodgerBlue2').place(x=100,y=350)
        
        #BOTONES PARA MANUALES
        boton6 = Button(text='Manual de Usuario',height=2,width=15,background='DarkOliveGreen1').place(x=400,y=200)
        boton7 = Button(text='Manual Técnico',height=2,width=15,background='DarkOliveGreen1').place(x=400,y=250)
        boton8 = Button(text='Ayuda',height=2,width=15,background='DarkOliveGreen1',command=self.Informacion).place(x=400,y=300)



    #METODO PARA LA SELECCION DE ARCHIVO 
    def AbrirArchivo(self):

        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/")
        self.direccion = archivo
        
        print(self.direccion)

    def Informacion(self):

        messagebox.showinfo(message="LENGUAJES FORMALES Y DE PROGRAMACION A+\n LUDWING ALEXANDER LÓPEZ ORTIZ\n 201907608\n Ludwingalexander230@gmail.com", title="INFORMACION DESARROLLADOR")

    def Edicion(self):

        Edicion = Ventana_Edicion()
        Edicion.Ventana_edicion(self.direccion)

    