from functools import reduce

dic={}

def generar_diccionario(cadena):
    jugador=cadena.strip().split(";")
    total=0
    for linea in jugador[:-1]:
        claves=linea.split(",")
        nombre=claves[0]
        valores = map(int, claves[1:])

        total=reduce(lambda x,y: x+y,valores)

        if nombre in dic:
            dic[nombre]+=[total]  
            total=0
        else:
            dic[nombre]=[total]
            total=0

    return dic


def ordenar_diccionario(dic):
    dic2 = {}
    for clave, valor in dic.items():
        dic2[clave] = sorted(valor,reverse=True)
    return dic2

def menor_numero_tiradas(dic):
    resultado = {}
    for clave, valores in dic.items():
        resultado[clave] = len(valores)
    return resultado

def igualar_tiradas(dic):
    resultado = {}
    for clave, valores in dic.items():
        resultado[clave] = [max(valores)]
    return resultado

def generar_lista_tuplas(dic):
    lista=[]
    for clave, valores in dic.items():
        lista.append((clave, max(valores)))  

    lista.sort(key=lambda x: x[1], reverse=True)  
    return lista

def jugador_ganador(lista):
    max_puntaje = 0
    ganadores = []
    
    for jugador in lista:
        if jugador[1] > max_puntaje:  
            max_puntaje = jugador[1]  
    
    for jugador in lista:
        if jugador[1] == max_puntaje:  
            ganadores.append(jugador) 
    return ganadores

def printar(titulo,elemento):
    print()
    print("----------------------------------------------------------")
    print(titulo)
    print(elemento)
    print("----------------------------------------------------------")
    print()
