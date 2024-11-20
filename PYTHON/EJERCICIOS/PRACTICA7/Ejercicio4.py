lista = [("Alberto", 22), ("Marcos", 11), ("AlexBrawl", 18)]
lista = list(filter(lambda x: x[1]<18, lista))
print(lista)