def filtrar_palabras(lista,letras):
     for i in lista:
        if len(i)>=letras:
            print(i)
            


lista=["En", "la", "granja", "la", "vaca", "pasea", "tranquila", "por", "el", "prado", "disfrutando", "del", "sol"]
filtrar_palabras(lista,7)