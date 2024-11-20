diccionario = {
    "persona1": {"Nombre": "Jared", "Nota": 10},
    "persona2": {"Nombre": "Marcos", "Nota": 4},
    "persona3": {"Nombre": "Albertostas", "Nota": 6}
}

listaAprobados = list(filter(lambda x: x["Nota"] >= 5, diccionario.values()))
listaSuspensos = list(filter(lambda x: x["Nota"] < 5, diccionario.values()))
listaNotaSuperior = list(filter(lambda x: x["Nota"] >= 9, diccionario.values()))

print("Aprobados:", listaAprobados)
print("Suspensos:", listaSuspensos)
print("Notas mayores o iguales a 9:", listaNotaSuperior)
