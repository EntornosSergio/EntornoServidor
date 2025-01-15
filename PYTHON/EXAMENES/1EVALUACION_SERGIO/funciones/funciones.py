def fun1(f):
    dic={}
    for linea in f:
        l=linea.strip().split("\n")
        for p in l:
            valor=p.split("|")
            if valor[0] not in dic:
                dic[valor[0]]=[valor[1]]
            if valor[1] not in dic[valor[0]]:
                dic[valor[0]]+=[valor[1]]

    return dic

def fun2(f):
    lista=[]
    for linea in f:
        lista.append(linea.strip())

    return lista

def fun3(f):
    lista=[]
    for linea in f:
        l=linea.strip().split("\n")
        for p in l:
            valor=p.split("|")
            lista.append(valor)

    sitios_trabajo = []
    with open("EXAMENES/1EVALUACION_SERGIO/assets/sitios_trabajo.txt","r+",encoding="latin-1") as f:
        for linea in f:
            sitios_trabajo.append(linea.strip())

    dic_filtrado = {}
    
    for usuario, sitio, tiempo in lista:
        tiempo = int(tiempo)
        if sitio not in sitios_trabajo:  
            if usuario not in dic_filtrado:
                dic_filtrado[usuario] = {}
            if sitio in dic_filtrado[usuario]:
                dic_filtrado[usuario][sitio] += tiempo
            else:
                dic_filtrado[usuario][sitio] = tiempo

    resultado = {}
    for usuario in dic_filtrado:
        resultado[usuario] = []  
        for sitio in dic_filtrado[usuario]:
            tiempo = dic_filtrado[usuario][sitio]
            resultado[usuario].append([sitio, tiempo])  

    return resultado
