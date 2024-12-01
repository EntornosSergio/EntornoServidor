import csv
from EJERCICIO6.Informacion import informacion
from EJERCICIO6.AñadirNota import añadirNota
from EJERCICIO6.Aprobados import aprobados


lista=0
numero=0
print("CALIFICACIONES DEL CURSO")
while numero!= 4:
    numero=int(input("1. Informacion \n2. Nota Final \n3. Aprobados/Suspensos \n4. Salir \n"))
    if numero == 1:
        with open("EJERCICIOS/PRACTICA9/calificaciones.csv","r+",encoding="latin-1") as fichero1:
            datos=csv.reader(fichero1,delimiter=";")
            encabezados2=next(datos)
            lista=informacion(datos)
            print(lista)
    if numero == 2:
        lista2=añadirNota(lista)
        print(lista2)
    if numero == 3:
        final=aprobados(lista2)
        print("APROBADOSS")
        print(final[0])
        print("SUSPENSOS")
        print(final[1])
