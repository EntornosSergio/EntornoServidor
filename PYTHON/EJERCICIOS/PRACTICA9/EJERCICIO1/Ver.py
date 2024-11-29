import re

def verUsuarios():
    with open("EJERCICIOS/PRACTICA9/listin.txt","r") as t:
        print("LISTIN TELEFONICO:  ")
        for linea in t:
            print(linea.strip())
        t.close()
        return