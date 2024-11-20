def validarUsuario(x):
    if (len(x)<6):
        return print("El nombrede usuario debe contener al menos 6 caracteres")
    elif (len(x)>12):
        return print("El nombrede usuario no puede contener más de 12 caracteres")
    elif (x.isalpha() == False):
        return print("El nombre solo puede contener letras")
    
    return print("Usuario valido!!!")
    