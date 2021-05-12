import csv

# Nombre del archivo para abrir
direct ="lista.csv"



def directorio():
    archivo = open(direct,"r")
    lector = csv.reader(archivo)
    for fila in lector:
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("1.-" + fila[1], "2.-" + fila[2], "3.-" + fila[3], "4.-" + fila[4], "5.-" + fila[5]))
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("6.-" + fila[6],"7.-" +fila[7], "8.-" + fila[8], "9.-" + fila[9],"10.-" + fila[10]))
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("11.-" + fila[11], "12.-" +fila[12], "13.-" + fila[13], "14.-" + fila[14], "15.-" + fila[15]))
        print("{:<23s}".format("16.-" + fila[16]))
        break
    archivo.close()

# esta función me imprime los datos del dentista
def datos(seleccion):
    archivo = open(direct,"r")
    lector = csv.reader(archivo)
    contador = 0
    for fila in lector:
        longitud = len(fila)
        if seleccion >= longitud:
            print("Ese dentista no existe")
            break
        if contador == 0:
           print("Nombre:", fila[seleccion])
        elif contador == 1:
           print("RFC:", fila[seleccion])
        elif contador == 2:
           print("Cédula federal:", fila[seleccion])
        elif contador == 3:
           print("Teléfono personal:", fila[seleccion])
        elif contador == 4:
           print("Teléfono del consultorio:", fila[seleccion])
           break
        contador = contador +1
    archivo.close()
