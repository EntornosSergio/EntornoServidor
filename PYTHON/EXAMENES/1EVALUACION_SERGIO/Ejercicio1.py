from funciones.funciones import fun1,fun2,fun3

with open("EXAMENES/1EVALUACION_SERGIO/assets/sitios_empleados.csv","r+",encoding="latin-1") as f:
    dic=fun1(f)  
    print("APARTADO 1")
    for c,v in dic.items():
        print(str(c)+" : " + str(v)) 
    
    print(50*"-")

with open("EXAMENES/1EVALUACION_SERGIO/assets/sitios_trabajo.txt","r+",encoding="latin-1") as f:
    lista=fun2(f)
    print("EJERCICIO 2")
    print(lista)
    print(50*"-")
    no_duplicados=[]
    [no_duplicados.append(x) for x,v in dic.items() for i in v if i not in lista and x not in no_duplicados]
    print(no_duplicados)


with open("EXAMENES/1EVALUACION_SERGIO/assets/sitios_empleados.csv","r+",encoding="latin-1") as f:
    print(50*"-")
    print("EJERCICIO 3")
    dic=fun3(f)
    for c,v in dic.items():
        print(str(c)+" : " + str(v)) 