import re

def validarContraseña(x):
    if len(x) <8:
        return False    
    elif x.islower()==True:
        return False    
    elif x.isupper()==True:
        return False    
    elif x.isdigit():
        return False    
    elif x.isalnum() == True:
        return False    
    elif ' ' in x:
        return False    
    
    return True