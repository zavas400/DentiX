from tkinter1 import *

# creamos la ventana
ventana = Tk()
ventana.title("DentiX")
ventana.geometry("500x700")


boton1 = Button(text="Ingresar")
boton1.grid(column=0, row=0)

boton2 = Button(text="Ingresar")
boton2.grid(column=1, row=0)

boton3 = Button(text="Ingresar")
boton3.grid(column=2, row=0)

boton4 = Button(text="Ingresar")
boton4.grid(column=3, row=0)

boton5 = Button(text="Ingresar")
boton5.grid(column=4, row=0)



ventana.mainloop()