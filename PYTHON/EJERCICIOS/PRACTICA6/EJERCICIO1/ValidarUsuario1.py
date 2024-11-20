def validarUsuario(x):
    if (len(x)<6):
        return print("El nombrede usuario debe contener al menos 6 caracteres")
    elif (len(x)>12):
        return print("El nombrede usuario no puede contener más de 12 caracteres")
    elif (x.isalnum() == False):
        return print("El nombre solo puede contener letras y números")
    
    return print("Usuario valido!!!")
    