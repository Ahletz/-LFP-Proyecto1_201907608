from tkinter import *

class Ventana_Edicion:

    def Ventana_edicion(self, direccion):

        self.direccion = direccion

        self.ventana2 = Tk()
        self.ventana2.geometry('600x500+550+150')
        self.ventana2.configure(background='turquoise1')
        self.ventana2.title('Edicion')
        self.ventana2.resizable(False,False)

        self.Text_Area()
        self.Botones()

        self.ventana2.mainloop()

        

    def Text_Area(self):

        self.area = Text(self.ventana2, width=50, height=30)
        self.area.place(x=10,y=10)
        archivo = open(self.direccion, encoding='utf-8')
        self.texto = archivo.read()
        print(self.texto)
        self.area.insert('end',self.texto)

    def Botones(self):

        boton1 = Button(self.ventana2, text='Guardar',height=2,width=15,background='DodgerBlue2', command=self.Guardar).place(x=450,y=100)
        boton2 = Button(self.ventana2, text='Guardar Como',height=2,width=15,background='DodgerBlue2', command=self.Guardar_como).place(x=450,y=150)
        boton3 = Button(self.ventana2, text='Salir',command=self.ventana2.destroy,height=2,width=15,background='DodgerBlue2').place(x=450,y=200) 

    def Guardar(self):

        texto = self.area.get("1.0","end")
        archivo = open(self.direccion, 'w')
        archivo.write(texto)
        archivo.close()

    def Guardar_como(self):

        texto = self.area.get("1.0","end")
        archivo = open('Nuevo_Archivo.form', 'w')
        archivo.write(texto)
        archivo.close()
     