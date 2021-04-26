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






