import re

def añadirUsuario():
    nombre=input("Añade un nombre: ")
    telefono=input("Añade un telefono: ")
    t = open("EJERCICIOS/PRACTICA9/listin.txt","a")
    t.write(nombre+","+telefono+"\n")
    t.close()
    return