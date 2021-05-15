import hashlib
print("hola mundo")

password = "Secretario1"
duh = "Secretario2"

hola = hashlib.sha3_256(password.encode())
caca = hashlib.sha3_256(duh.encode())
print(hola.hexdigest())
print(caca.hexdigest())
