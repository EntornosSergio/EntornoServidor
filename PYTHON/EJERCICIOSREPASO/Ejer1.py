personas=[]
with open("EJERCICIOSREPASO/ejer1.txt","r") as f:
    for linea in f:
        datos = linea.strip().split(";")
        persona = {
            "id": datos[0],
            "nombre": datos[1],
            "apellido": datos[2],
            "nacimiento": datos[3]
        }
        personas.append(persona)

print(personas)

