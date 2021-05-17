import csv

# Nombre del archivo para abrir
direct ="lista.csv"

def conseguir_nombre (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 0:
                Nombre = fila[seleccion]
                break
    archivo.close()
    return Nombre

def conseguir_rfc (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 1:
                RFC = fila[seleccion]
                break
            else:
                contador = contador +1
    archivo.close()
    return RFC

def conseguir_cedula (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 2:
                cedula = fila[seleccion]
                break
            else:
                contador = contador +1
    archivo.close()
    return cedula

def conseguir_tel_personal (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 3:
                Telefono_personal = fila[seleccion]
                break
            else:
                contador = contador +1
    archivo.close()
    return Telefono_personal

def conseguir_tel_consultorio (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 4:
                Telefono_consultorio = fila[seleccion]
                break
            else:
                contador = contador +1
    archivo.close()
    return Telefono_consultorio

def conseguir_correo (salida, seleccion):
    archivo = open(direct, "r")
    lector = csv.reader(archivo)
    contador = 0
    if salida == 1:
        for fila in lector:
            if contador == 5:
                Correo = fila[seleccion]
                break
            else:
                contador = contador +1
    archivo.close()
    return Correo


