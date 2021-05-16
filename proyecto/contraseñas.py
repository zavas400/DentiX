import hashlib
# Usuario y contraseñas

dbu =["7545cf21fc41bb2a55439a268bdf4af200dc833d119e41f338185d2ee47238f0","8654e2facc8f64b198901dab323bed7b7871e50b05335563b3df5075020877f6"]
dbp =["97c4fd3c0aada3c1c4ed77854ea0dfa7b9b71ef54bd5cab2d620aab19abce1ea", "db65fb13b0f2ecafcdb3f02f18c698f440b8373502c641b32f45d9b72c2c5fc5"]

def pedir_usu():
    cifrado = hashlib.sha3_256(usuario.encode())
    return cifrado


# ciframos contraseña
def pedir_con():
    # ciframos la contraseña
    cifrado = hashlib.sha3_256(contrasena.encode())
    return cifrado

# comprobamos usuario y contraseña
def comprobar(usuario, dbu, cifrado, dbp):
    if usuario.hexdigest() in dbu:
        posicion = dbu.index(usuario.hexdigest())
        if cifrado.hexdigest() == dbp[posicion]:
            hola = 1
        else:
            exit()
    else:
        exit()


def nueva ():
    usuario_cifrado = pedir_usu()
    contrasena_cifrada = pedir_con()
    comp = comprobar(usuario_cifrado, dbu, contrasena_cifrada, dbp )

