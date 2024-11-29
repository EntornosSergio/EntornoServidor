import re

def añadirUsuario():
    nombre=input("Añade un nombre:")
    telefono=input("Añade un telefono")
    t = open("EJERCICIOS/PRACTICA9/listin.txt","w")
    t.write(nombre+","+telefono)
    