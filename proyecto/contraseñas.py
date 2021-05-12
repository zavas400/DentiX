import hashlib
# Usuario y contraseñas


# ciframos contraseña
def pedir_con():
    contrasena = input("Escribe tu password: ")
    # ciframos la contraseña
    cifrado = hashlib.sha3_256(contrasena.encode())
    return cifrado

# comprobamos usuario y contraseña
def comprobar(usuario, dbu, cifrado, dbp):
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




