def mas(anchura,caracter):
    for i in range(1,anchura +1):
        print(caracter * i)

def menos (anchura,caracter):
        for i in range(anchura-1,0,-1):
            print(caracter * i)
        
anchura=int(input("Anchura: "))
caracter=input("Elige caracter: ")
mas(anchura,caracter)
menos(anchura,caracter)


