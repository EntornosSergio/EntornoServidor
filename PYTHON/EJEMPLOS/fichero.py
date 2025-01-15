with open("EJEMPLOS/fichero.txt","a",encoding="latin-1") as fichero:
    fichero.write("guapo")
    lista=[1,2]
     
    fichero.writelines(int(lista))
