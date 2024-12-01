import re

def añadirNota(lista):
    for row in lista:
        parciales = float(row["Parcial1"].replace(",", ".")) + float(row["Parcial2"].replace(",", "."))
        parciales = parciales % 2
        parciales = parciales * 0.70
        if row["Practicas"].strip()=="":
            row["Nota final"] = parciales
        else: 
            practicas = float(row["Practicas"].replace(",", "."))
            practicas = practicas * 0.60
            suma = parciales + practicas
            row["Nota final"]=suma

    return lista