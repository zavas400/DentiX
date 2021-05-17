import oh as fd
import cn



dbu =["7545cf21fc41bb2a55439a268bdf4af200dc833d119e41f338185d2ee47238f0","8654e2facc8f64b198901dab323bed7b7871e50b05335563b3df5075020877f6"]
dbp =["97c4fd3c0aada3c1c4ed77854ea0dfa7b9b71ef54bd5cab2d620aab19abce1ea", "db65fb13b0f2ecafcdb3f02f18c698f440b8373502c641b32f45d9b72c2c5fc5"]


# ciframos el usuario
c_us = cn.pedir_usu()

# ciframos la contraseña
c_cont = cn.pedir_con()

cn.comprobar(c_us, dbu, c_cont, dbp)

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

