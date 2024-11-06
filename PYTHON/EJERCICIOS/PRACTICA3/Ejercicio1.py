def pintar(altura,anchura,caracter="*"):

    for i in range(altura):
        for k in range(anchura):
            print(caracter,end=" ")    
        print()

altura=(int(input("Altura: ")))
anchura=(int(input("Anchura: ")))

pintar(altura,anchura)
