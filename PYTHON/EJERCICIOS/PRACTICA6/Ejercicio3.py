from EJERCICIO1.ValidarUsuario2 import validarUsuario
from EJERCICIO1.ValidarContraseña2 import validarContraseña
from EJERCICIO2.ValidarDNI import validarDNI
from EJERCICIO2.ValidarEdad import ValidarEdad


diccionario = {}

while True:
    val1 = False
    val2 = False
    val3 = False
    
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
                
    dni = input("Introduce DNI: ")
    if validarDNI(dni):
        print("DNI válido.")
    else:
        print("DNI incorrecto.")

    edad = input("Introduce edad: ")
    if ValidarEdad(edad):
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad o la edad ingresada no es válida.")
    
    # Registrar el usuario y la contraseña
    """ ASI ES PARA AÑADIR EN UNA TUPLA
    diccionario[usuario] = contraseña,dni,edad """
    
    """ ASI PARA UNA LISTA """
    diccionario[usuario] = [contraseña,dni,edad]
    print("Usuario y contraseña registrados con éxito.")
    
    print("Usuarios registrados:", diccionario)

