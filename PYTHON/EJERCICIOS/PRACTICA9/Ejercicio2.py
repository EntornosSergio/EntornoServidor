dic1={}
dic2={}
dic3={}
dic4={}
personas=[]
with open("EJERCICIOS/PRACTICA9/personas.txt","r") as t:
    for linea in t:
        num=linea.strip().split(";")
        dic1={num[0]+","+num[1]+","+num[2]+","+num[3]}
        personas.append(dic1)

print(personas)
