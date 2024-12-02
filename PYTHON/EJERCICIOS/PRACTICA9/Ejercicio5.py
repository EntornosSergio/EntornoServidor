import csv

correos=[]
correos2=[]


with open("EJERCICIOS/PRACTICA9/ListadoAlumnosFP.csv","r+",encoding="latin-1") as fichero2:
    datos2=csv.reader(fichero2,delimiter=";")
    encabezados2=next(datos2)
    for row in datos2:
        alumno=row[0].lower()+"."+row[1].lower()+"@plazacastilla.salesianas.org"
        alumno2=row[0].lower()+"."+row[1].lower()+"."+row[2].lower()+"@plazacastilla.salesianas.org"
        correos.append((alumno, alumno2))  
        
with open("EJERCICIOS/PRACTICA9/AlumnosFP.csv","r+",encoding="latin-1") as fichero1:
    datos1=csv.reader(fichero1,delimiter=";")
    encabezados1=next(datos1)
    for row in datos1:
        alum=row[1]
        correos2.append(alum)
        
    for alumno,alumno2 in correos:
        if alumno not in correos2:
            correos2.append(alumno)
        else:
            correos2.append(alumno2)
        
    
print(correos)
print("--------------------------")
print(correos2)


        