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

def datoss(salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    if salida == 1:
        contador = 0
        for fila in lector:
            if contador == 0:
                Nombre = fila[seleccion]
            elif contador == 1:
                RFC = fila[seleccion]
            elif contador == 2:
                Cedula_federal = fila[seleccion]
            elif contador == 3:
                Telefono_personal = fila[seleccion]
            elif contador == 4:
                Telefono_consultorio = fila[seleccion]
                break

        contador = contador +1
    archivo.close()
    return Nombre, RFC, Cedula_federal