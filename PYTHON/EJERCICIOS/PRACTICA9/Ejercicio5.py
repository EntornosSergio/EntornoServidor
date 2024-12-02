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

"""
import csv

with open("Ejercicios/Practica9/csv/AlumnosFP.csv", "r", encoding='latin-1') as f:
    nombres=list(csv.reader(f, delimiter=";"))
    nombres=nombres[1:]
    

correos=[]
    
for i in nombres:
   correos.append(i[1])
   
with open("Ejercicios/Practica9/csv/ListadoAlumnosFP.csv", "r", encoding='latin-1') as f:
    nombre=list(csv.reader(f, delimiter=";"))
    
    nombre=nombre[1:]
    
    print(nombre)
    
correoAlumno=[]

for i in nombre:
    correo=i[0].lower()+"."+i[1].lower()+"@plazacastilla.salesianas.org"
    if correo in correos:
        correo=i[0].lower()+"."+i[1].lower()+"."+i[2].lower()+"@plazacastilla.salesianas.org"
        correoAlumno.append(correo)
    else:
        correoAlumno.append(correo)
        
print(correoAlumno)

fichero=open("Ejercicios/Practica9/csv/AlumnosFP.csv", "a")
contenido=csv.writer(fichero, delimiter=";")

nombreJunto=[]

for i in nombre:
    nombreJunto.append(" ".join(i))
    
for i in range(0, len(nombre)):
    contenido.writerow([nombreJunto[i], correoAlumno[i], 'Ventajas de uso de Microsoft 365 A3 para estudiantes'])
"""
        