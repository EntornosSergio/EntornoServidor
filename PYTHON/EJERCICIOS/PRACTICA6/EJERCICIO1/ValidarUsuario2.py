def validarUsuario(x):
    if (len(x)<6):
        return False
    elif (len(x)>12):
        return False
    elif (x.isalnum() == False):
        return False
    
    return True
    