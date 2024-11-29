import re

def consultarUsuario():
    nombre=input("Introduce nombre: ")
        
    with open("EJERCICIOS/PRACTICA9/listin.txt","r") as t:
        for linea in t:
            datos=linea.strip().split(",")
            if nombre==datos[0]:
                tel=datos[1]
                print(tel)
                t.close()
                return

        print("Nombre no encontrado")
        t.close()
                