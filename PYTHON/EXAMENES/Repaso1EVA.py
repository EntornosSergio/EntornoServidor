def esVocal(letra):
    return letra in ['a', 'e', 'i', 'o', 'u']

def estaEnLista(letra, lista):
    i = 0
    while i < len(lista):  
        if lista[i][0] == letra:  
            return i  
        i += 1
    return -1 

def transformar(lista):
    return list(map(tuple, lista))

lista = []
cadena = input("Ingresa una cadena: ").lower()

for letra in cadena:
    if esVocal(letra):  
        print("Es vocal " + letra)
        index = estaEnLista(letra, lista)  
        if index != -1:  
            lista[index][1] += 1
        else: 
            lista.append([letra, 1])
    else:
        print(f"No es vocal {letra}")

print("Lista:", lista)

t = transformar(lista)
print("Tuplas:", t)

t.sort(key=lambda x: x[1], reverse=True)
print("Ordenado de mayor a menor:", t)
