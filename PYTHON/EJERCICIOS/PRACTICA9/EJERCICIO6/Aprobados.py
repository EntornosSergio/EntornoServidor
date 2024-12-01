import re

def aprobados(lista):
    aprobados=[]
    suspensos=[]
    for row in lista:
        asistencia = float(row["Asistencia"].replace("%", "").strip())
        parcial1 = float(row["Parcial1"].replace(",", ".").strip()) 
        parcial2 = float(row["Parcial2"].replace(",", ".").strip())
        nota_final = row.get("Nota final", 0)  

        if asistencia >= 75 and parcial1 >= 4 and parcial2 >= 4 and nota_final >= 5:            
            aprobados.append(row)
        else:
            suspensos.append(row)

    return aprobados,suspensos
            

 