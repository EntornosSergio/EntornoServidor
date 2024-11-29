import re

def eliminarUsuario():
    nombre=input("Introduce nombre a eliminar: ")
    with open("EJERCICIOS/PRACTICA9/listin.txt", "r") as t:
        lineas = t.readlines()  

    lineas_nuevas = [linea for linea in lineas if not linea.strip().split(",")[0] == nombre]

    if len(lineas) == len(lineas_nuevas):
        print("Nombre no encontrado.")
    else:
        with open("EJERCICIOS/PRACTICA9/listin.txt", "w") as t:
            t.writelines(lineas_nuevas)  

