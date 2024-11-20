from EJERCICIO1.ValidarUsuario2 import validarUsuario
from EJERCICIO1.ValidarContraseña2 import validarContraseña

val1=False
val2=False
diccionario = {}
usuario= " "

while usuario!= "*":
    while val1==False:
        usuario=input("Introduce usuario: ")
        if usuario == "*":
            exit()
        else:
            validarUsuario(usuario)
            if validarUsuario==False:
                val1=False
            else:
                val1=True
            
    while val2==False:
        contraseña=input("Introduce contraseña: ")
        validarContraseña(contraseña)
        if validarContraseña==False:
            val2=False
        else:
            val2=True
        
if usuario in diccionario:
    print("Este usuario ya esta")
else:
    diccionario.update({usuario})

if contraseña in diccionario:
    print("Esta contraseña ya esta")
else:
    diccionario.update({contraseña})
    
print(diccionario)
