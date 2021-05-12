import oh as fd
import contraseñas as cn


# Usuario y contraseñas
dbu =["Secretario1","Secretario2"]
dbp =["97c4fd3c0aada3c1c4ed77854ea0dfa7b9b71ef54bd5cab2d620aab19abce1ea", "db65fb13b0f2ecafcdb3f02f18c698f440b8373502c641b32f45d9b72c2c5fc5"]

# pedimos el usuario
usuario = input("Escribe tu nombre de usuario: ")

# ciframos la contraseña
cifrado = cn.pedir_con()

# Comprobamos el usuario y la contraseña
cn.comprobar(usuario, dbu, cifrado, dbp)

continuar = 1

# mostramos el directorio y podemos seleccionar un dentista
while continuar == 1:
      fd.directorio()
      seleccion = int(input("Escribe el número de dentista que quieres consultar: "))
      print()
      fd.datos(seleccion)
      print()
      continuar = int(input("¿Deseas consultar otro dentista? 1= sí, 2=no "))

print("Gracias por usar el programa")

