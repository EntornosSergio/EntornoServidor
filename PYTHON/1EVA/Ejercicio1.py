from funciones.funciones import funcion1a
from funciones.funciones import funcion1b
from funciones.funciones import funcion2a
from funciones.funciones import funcion3a



dic={}
with open("1EVA/assets/sitios_empleados.csv", "r", encoding='latin-1') as f:
    dic=funcion1a(f)
    funcion1b(dic)

with open("1EVA/assets/sitios_trabajo.txt","r") as t:
    lista=funcion2a(t)
    print(lista)

nombresList=[c for c,v in dic.items() for site in v if site not in lista] 
nombresListNoDuplicates=[]    
[nombresListNoDuplicates.append(i) for i in nombresList if i not in nombresListNoDuplicates]
print(" ")
for i in nombresListNoDuplicates:
    print(i)
print("-"*50)
    
with open("1EVA/assets/sitios_empleados.csv", "r", encoding='latin-1') as l:
    dic2=funcion3a(l)
    print("APARTADO 3")
    for c,v in dic2.items():
        print(c + " : " + str(v))