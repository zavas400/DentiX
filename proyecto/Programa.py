import oh as fd
import contraseñas as cn
import hashlib


# Usuario y contraseñas
def pedir_con():
      usuario = input("Escribe tu nombre de usuario: ")
      cifrado = hashlib.sha3_256(usuario.encode())
      return cifrado

# ciframos la contraseña
cifrado = cn.pedir_con()

# Comprobamos el usuario y la contraseña
def comprobar(usuario, dbu, cifrado, dbp):
      if usuario in dbu:
            posicion = dbu.index(usuario)
            if cifrado.hexdigest() == dbp[posicion]:
                  print("Login exitoso")
            else:
                  print("Usuario o Password incorrectos")
                  exit()
      else:
            print("Usuario o Password incorrectos")
            exit()


continuar = 1

# mostramos el directorio y podemos seleccionar un dentista
while continuar == 1:
      fd.directorio()
      seleccion = int(input("Escribe el número de dentista que quieres consultar: "))
      print()
      fd.datos(seleccion)
      print()
      continuar = int(input("¿Deseas consultar otro dentista? 1= sí, 2= no "))

print("Gracias por usar el programa")