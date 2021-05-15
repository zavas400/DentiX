import hashlib
# Usuario y contraseñas

def pedir_usu():
    usuario = input("Escribe tu nombre de usuario: ")
    cifrado = hashlib.sha3_256(usuario.encode())
    return cifrado


# ciframos contraseña
def pedir_con():
    contrasena = input("Escribe tu password: ")
    # ciframos la contraseña
    cifrado = hashlib.sha3_256(contrasena.encode())
    return cifrado

# comprobamos usuario y contraseña
def comprobar(usuario, dbu, cifrado, dbp):
    if usuario.hexdigest() in dbu:
        posicion = dbu.index(usuario.hexdigest())
        if cifrado.hexdigest() == dbp[posicion]:
            print("Login existoso")
        else:
            print("Usuario o Password Incorrectos")
            exit()
    else:
        print("Usuario  Incorrectos")
        exit()




