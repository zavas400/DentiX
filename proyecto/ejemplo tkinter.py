from tkinter1 import *

# creamos la ventana
ventana = .Tk()
ventana.title("DentiX")
ventana.geometry("500x700")

titulo = .Label(text="Ingrese usuario y contraseña")
titulo.grid()

etiqueta_usuario = .Label(text="Usuario:")
etiqueta_usuario.grid(column=0, row=1)

entrada_usuario = .Entry()
entrada_usuario.grid(column=1, row=1)

etiqueta_contra = Label(text="Contraseña:")
etiqueta_contra.grid(column=0, row=2)

entrada_contra = .Entry()
entrada_contra.grid(column=1, row=2)




boton1 = .Button(text="Ingresar")
boton1.grid(column=3, row=3)


ventana.mainloop()