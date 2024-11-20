lista = [("Alberto", 22), ("Marcos", 11), ("AlexBrawl", 44)]
lista = list(map(lambda x: (x[0], x[1] + 1), lista))
print(lista)
