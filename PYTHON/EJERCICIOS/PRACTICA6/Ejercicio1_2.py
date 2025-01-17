from EJERCICIO1.ValidarUsuario2 import validarUsuario
from EJERCICIO1.ValidarContraseña2 import validarContraseña

diccionario = {}

while True:
    val1 = False
    val2 = False
    
    while not val1:
        usuario = input("Introduce usuario (o '*' para salir): ")
        if usuario == "*":
            print("Saliendo del programa.")
            exit()
        if usuario in diccionario:
            print("Este usuario ya está registrado. Introduce un usuario diferente.")
        else:
            val1 = validarUsuario(usuario)  # Retorna True o False
            if not val1:
                print("Usuario inválido. Inténtalo de nuevo.")
    
    while not val2:
        contraseña = input("Introduce contraseña: ")
        if contraseña in diccionario.values():
            print("Esta contraseña ya está en uso. Introduce una contraseña diferente.")
        else:
            val2 = validarContraseña(contraseña)  # Retorna True o False
            if not val2:
                print("Contraseña inválida. Inténtalo de nuevo.")
    
    # Registrar el usuario y la contraseña
    diccionario[usuario] = contraseña
    print("Usuario y contraseña registrados con éxito.")
    
    print("Usuarios registrados:", diccionario)
