import csv

# Nombre del archivo para abrir
direct ="lista.csv"


# esta función me imprime los datos del dentista
def datos(salida, seleccion):
    archivo = open(direct,"r")
    lector = csv.reader(archivo)
    if salida == 1:
        for fila in lector:
            print(fila[0], fila[seleccion])
    archivo.close()
