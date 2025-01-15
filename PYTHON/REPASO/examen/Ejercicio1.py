from funciones.fun import esvocal
from funciones.fun import estaenlista
from funciones.fun import transformar


palabra=input("Escribe una palabra: ")
letras=list(palabra.upper())
lista_frecuencias=[]
for l in letras:
    if esvocal(l):
        p=estaenlista(l,lista_frecuencias)
        if p!=-1:
            lista_frecuencias[p][1]+=1    
        else:
            lista_frecuencias.append([l,1])

print(lista_frecuencias)
tupla=transformar(lista_frecuencias)
print(tupla)
lista_frecuencias.sort(key=lambda x:x[1],reverse=True)
print(lista_frecuencias)


