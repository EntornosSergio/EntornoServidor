import re

def fun1(f):
    lista=[]
    lineas = f.readlines()[1:]

    for linea in lineas:
        campos = linea.strip().split(";")  
        dic = {
                "Apellidos": campos[0],
                "Asistencia": campos[2],
                "Parcial 1": campos[3],
                "Parcial 2": campos[4],
                "Practicas": campos[7]
            }
        lista.append(dic)

    lista.sort(key=lambda x: x["Apellidos"])
    
    return lista


def fun2(lista):
    for l in lista: 
        p1 = float(l["Parcial 1"].replace(",", ".") if l["Parcial 1"] else "0")
        p2 = float(l["Parcial 2"].replace(",", ".") if l["Parcial 2"] else "0")
        p3 = float(l["Practicas"].replace(",", ".") if l["Practicas"] else "0")
        parcial1=p1*0.3
        parcial2=p2*0.3
        practicas=p3*0.4
        total=parcial1+parcial2+practicas
        l["Nota final"]=total

    return lista


def fun3():
    

        
    