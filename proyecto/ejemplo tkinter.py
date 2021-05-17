from tkinter import *
import hashlib
import contraseñas as cn

dbu =["7545cf21fc41bb2a55439a268bdf4af200dc833d119e41f338185d2ee47238f0","8654e2facc8f64b198901dab323bed7b7871e50b05335563b3df5075020877f6"]
dbp =["97c4fd3c0aada3c1c4ed77854ea0dfa7b9b71ef54bd5cab2d620aab19abce1ea", "db65fb13b0f2ecafcdb3f02f18c698f440b8373502c641b32f45d9b72c2c5fc5"]

def pedir_usu():
    usuario = str(entrada_usuario.get())
    cifrado = hashlib.sha3_256(usuario.encode())
    return cifrado

def pedir_con():
    contrasena = str(entrada_contra.get())
    cifrado = hashlib.sha3_256(contrasena.encode())
    return cifrado


def salida (salida):
    if salida == 2:
        continue

# Creamos la ventana
ventana = Tk()
ventana.title("DentiX")
ventana.geometry("500x700")

titulo = Label(text="Ingrese usuario y contraseña")
titulo.grid()

etiqueta_usuario = Label(text="Usuario:")
etiqueta_usuario.grid(column=0, row=1)

entrada_usuario = Entry()
entrada_usuario.grid(column=1, row=1)

etiqueta_contra = Label(text="Contraseña:")
etiqueta_contra.grid(column=0, row=2)

entrada_contra = Entry()
entrada_contra.grid(column=1, row=2)

usuario_cifrado = pedir_usu()
contrasena_cifrada = pedir_con()
salidaa = int(cn.comprobar(usuario_cifrado, dbu, contrasena_cifrada, dbp ))

boton1 = Button(text="Ingresar" , command = salida(salidaa))
boton1.grid(column=3, row=3)


ventana.mainloop()