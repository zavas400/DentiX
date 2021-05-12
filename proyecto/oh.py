import csv

# Nombre del archivo para abrir
direct ="lista.csv"


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
        print(fila[0], fila[seleccion])
    archivo.close()

def directorio():
    archivo = open(direct,"r")
    lector = csv.reader(archivo)
    print("----------Directorio----------")
    for fila in lector:
        Num = (len(fila) -1)
        mas_cinco = 0
        while mas_cinco < Num:
            primero = str(mas_cinco + 1)
            segundo = str(mas_cinco + 2)
            tercero = str(mas_cinco + 3)
            cuarto = str(mas_cinco + 4)
            quinto = str(mas_cinco + 5)
            print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format(primero + ".-" + fila[1 + mas_cinco], segundo + ".-" + fila[2+ mas_cinco], tercero + ".-" +  fila[3 + mas_cinco], cuarto + ".-" +  fila[4 + mas_cinco], quinto + ".-" +  fila[5 + mas_cinco]))
            mas_cinco = mas_cinco + 5
        break
    archivo.close()