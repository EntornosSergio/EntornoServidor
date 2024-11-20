from EJERCICIO2.ValidarDNI import validarDNI
from EJERCICIO2.ValidarEdad import ValidarEdad

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