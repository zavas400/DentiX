# este es un avance

import hashlib
# primera password es: 0173490
# segunda password es: Grulla222
dbu =["Secretario1","Secretario2"]
dbp =["97c4fd3c0aada3c1c4ed77854ea0dfa7b9b71ef54bd5cab2d620aab19abce1ea", "db65fb13b0f2ecafcdb3f02f18c698f440b8373502c641b32f45d9b72c2c5fc5"]

# pedimos usuario y contraseña
usuario = input("Escribe tu usuario: ")
password = input("Escribe tu password: ")
# ciframos la contraseña
cifrado = hashlib.sha3_256(password.encode())

#comprobamos el usuario y la contraseña

if usuario in dbu:
    posicion = dbu.index(usuario)
    if cifrado.hexdigest() == dbp[posicion]:
        print("Login existoso")
    else:
        print("Usuario o Password Incorrectos")
        exit()
else:
    print("Usuario o Password Incorrectos")
    exit()


