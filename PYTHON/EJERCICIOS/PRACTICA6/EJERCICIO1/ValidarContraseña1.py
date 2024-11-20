import re

def validarContraseña(x):
    if len(x) <8:
        return print("Debe de contener un minimo de 8 caracteres"),False
    elif x.islower()==True:
        return print("Debe contener minusculas"),False
    elif x.isupper()==True:
        return print("Debe contener mayusculas"),False
    elif x.isdigit():
        return print("Debe contener al menos un numero"),False
    elif x.isalnum() == True:
        return print("Debe tener al menos 1 caracter no alfanumerico"),False
    elif ' ' in x:
        return print("No puede contener espacios en blanco"),False
    
    return print("Contraseña valida!!!!"),True