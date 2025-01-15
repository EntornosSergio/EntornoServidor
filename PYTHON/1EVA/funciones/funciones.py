import re
import csv

def funcion1a(f):
    dic={}
    contenido=list(csv.reader(f,delimiter="|"))
    for l in contenido:
        if l[0] not in dic:
            dic[l[0]] = []
        
        if l[1] not in dic[l[0]]:
            dic[l[0]].append(l[1])

    return dic 


def funcion1b(dic):
    print("APARTADO 1")
    for c,v in dic.items():
        print(c + " : " + str(v))
    
    print("------------------------------------")


def funcion2a(f):
    lista=[]
    """
    for linea in f:
        num=linea.strip().split("\n")
        lista.extend(num)
    return lista
    """
    print("APARTADO 2: ")
    for row in f:
        lista.append(row.strip())
    return lista

    
def funcion3a(f):
    # Leer el contenido del archivo CSV
    contenido = list(csv.reader(f, delimiter="|"))
    
    # Leer el archivo de sitios de trabajo
    sitios_trabajo = []
    with open("1EVA/assets/sitios_trabajo.txt", "r") as t:
        for row in t:
            sitios_trabajo.append(row.strip())
    
    dic_filtrado = {}
    
    for usuario, sitio, tiempo in contenido:
        tiempo = int(tiempo)  # Convertir el tiempo a entero
        if sitio not in sitios_trabajo:  # Si no es un sitio de trabajo
            if usuario not in dic_filtrado:
                dic_filtrado[usuario] = {}
            # Sumar el tiempo si ya existe, de lo contrario, añadir el sitio
            if sitio in dic_filtrado[usuario]:
                dic_filtrado[usuario][sitio] += tiempo
            else:
                dic_filtrado[usuario][sitio] = tiempo

    # Convertir el diccionario interno a una lista con formato deseado
    resultado = {}
    for usuario in dic_filtrado:
        resultado[usuario] = []  # Inicializar la lista de sitios para este usuario
        for sitio in dic_filtrado[usuario]:
            tiempo = dic_filtrado[usuario][sitio]
            resultado[usuario].append([sitio, tiempo])  # Añadir el sitio y tiempo como lista

    return resultado