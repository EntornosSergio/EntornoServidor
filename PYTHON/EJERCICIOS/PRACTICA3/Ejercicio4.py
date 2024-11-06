def ConvertirEspaciado(texto,numero):
    for letra in texto:
        print(" " * numero + letra,end=" ")
    
    
texto=input("Escriba un texto: ")
numero=int(input("Numero de espacios: "))

ConvertirEspaciado(texto,numero)