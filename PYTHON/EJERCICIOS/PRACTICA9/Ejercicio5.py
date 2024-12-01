import csv

with open("EJERCICIOS/PRACTICA9/AlumnosFP.csv","r+",encoding="latin-1") as fichero1:
    datos1=list(csv.reader(fichero1,delimiter=";"))
    encabezados1=iter(datos1)
    with open("EJERCICIOS/PRACTICA9/calificaciones.csv","r+",encoding="latin-1") as fichero2:
        datos2=csv.reader(fichero2,delimiter=";")
        encabezados2=next(datos2)
        print(encabezados2) 
        for row in datos2:
            apellidos=row[0].split(" ")
            alumno=row[1]+"."+apellidos[0]+"@estudiantes.plaza.com"
            print(alumno)
            for row2 in datos1:
                if alumno not in datos1[1]:
                    añadir=list(csv.writer(datos2[0]+","+datos2[0]+","+alumno))