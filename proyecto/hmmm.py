import oh

continuar = 1

while continuar == 1:
      oh.directorio()
      seleccion = int(input("Escribe el número de dentista que quieres consultar: "))
      print()
      oh.datos(seleccion)
      print()
      continuar = int(input("¿Deseas consultar otro dentista? 1= sí, 2=no "))

print("Gracias por usar el programa")

