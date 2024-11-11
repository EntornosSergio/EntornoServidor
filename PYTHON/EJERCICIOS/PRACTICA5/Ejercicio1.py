cadena = "hola cómo estás hola hola bien cómo estás"

palabras = cadena.split()

conteo = {}

# Contar las palabras
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print(conteo)