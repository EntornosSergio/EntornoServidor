from funciones import fun1,fun2,fun3

with open("EJERCICIOSREPASO/calificaciones.csv", "r", encoding='latin-1') as f:
    lista=fun1(f)
    print(lista)
    print(50*"-")
    lista2=fun2(lista)
    print(lista2)
    lista3=fun3(lista2)