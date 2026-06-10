usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su contraseña: ")

if len(clave) < 8:
    print("Contraseña insegura")
else:
    print("Acceso permitido")