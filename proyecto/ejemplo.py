# este es un pequeño código que nos va a decir si el nombre de un dentista está dentro del archivo

hola = ["hola", "adios", "tal vez", "dedo", "uña"]
a = 1
# le puedo añadir un while
# while a = 1:
palabra = input("escribe la palabra: ")

for fila in hola:
    if fila[0] == "hola":
        continue
    for i in range(1, len(hola)):
        if palabra == (hola[i]):
            a = 2
            break
        else:
            a = 1

if a ==2:
    print("la palabra", palabra, "existe")
else:
    print("la palabra", palabra, " no existe")

def directorio():
    archivo = open(direct,"r")
    lector = csv.reader(archivo)
    print("----------Directorio----------")
    for fila in lector:
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("1.-" + fila[1], "2.-" + fila[2], "3.-" + fila[3], "4.-" + fila[4], "5.-" + fila[5]))
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("6.-" + fila[6],"7.-" +fila[7], "8.-" + fila[8], "9.-" + fila[9],"10.-" + fila[10]))
        print("{:<23s}{:<20s}{:<20s}{:<20s}{:<20s}".format("11.-" + fila[11], "12.-" +fila[12], "13.-" + fila[13], "14.-" + fila[14], "15.-" + fila[15]))
        print("{:<23s}".format("16.-" + fila[16]))
        break
    archivo.close()




