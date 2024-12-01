import re

def informacion(fichero):
    lista=[]
    for row in fichero:
        diccionario = {
                "Nombre": row[1],
                "Apellidos": row[0],
                "Asistencia": row[2],
                "Parcial1": row[3],
                "Parcial2": row[4],
                "Ordinario1": row[5],
                "Ordinario2": row[6],
                "Asistencia": row[2],
                "Practicas" : row[7],
            }
        lista.append(diccionario)

    lista_ordenada = sorted(lista, key=lambda alumno: alumno["Apellidos"])


    return lista_ordenada