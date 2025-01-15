import re   

vocales=["A","E","I","O","U"]

def esvocal(l):
    return l in vocales

def estaenlista(l,lista):
    for i in range(0,len(lista)):
        if lista[i][0]==l:
            return i
    return -1

def transformar(lista):
    listaf_tuplas=[]
    for item in lista:
        listaf_tuplas.append((item[0],item[1]))
    return listaf_tuplas
