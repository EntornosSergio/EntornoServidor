import re

def validarContraseña(x):
    if len(x) <8:
        return print("Debe de contener un minimo de 8 caracteres")
    elif x.islower()==True:
        return print("Debe contener minusculas")
    elif x.isupper()==True:
        return print("Debe contener mayusculas")
    elif re.search(r'\d',x):
        return print("Debe contener al menos un numero")
    elif x.isalnum() == True:
        return print("Debe tener al menos 1 caracter no alfanumerico")
    elif x.isspace()==True:
        return print("No puede contener espacios en blanco")
    
    return True