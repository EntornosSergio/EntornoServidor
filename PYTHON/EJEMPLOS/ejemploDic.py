diccionario_1=dict()
diccionario_2={}
diccionario_3={'Francia':'francés','España':'español'}
diccionario_4={'España':['Madrid',50000000,6666],}
#La lista entera
print(diccionario_4['España'])
#la capital
print(diccionario_4['España'][0])

#cambio la población
diccionario_4['España'][1]=49000000

diccionario_5={
    'España':{'capital':'Madrid',
              'poblacion':49000000,
              'superficie':888888,
              'playas': 3000
              },
    'Francia':{
             'capital':'París',
             'poblacion':666666,
             'superficie':999999
            }
}

len(diccionario_4)
len(diccionario_4['España'])

pais=input('Introduce un pais europeo')
if pais in diccionario_5:
    print("Si lo tengo registrado")
else:
    print("No lo tengo registrado")
    
#escribo los nombre de los paises
"""for p in diccionario_5:
    print(p)
for p in diccionario_5.keys():
    print(p)
    
#todos los datos de cada pais    
for p in diccionario_5:
    print(diccionario_5[p])
    
for p in diccionario_5.values():
    print(p)

#todo el diccionario    
for p in diccionario_5.items():
    print(p)    
 
#la población de todos los paises
for p in diccionario_5:
    print(str(p) + " - " + str(diccionario_5[p]['poblacion']))  
  
for p in diccionario_5.items():
    print(str(p[0])+" - "+ str(p[1]['poblacion']) )  

"""
for c,v in zip(diccionario_5.keys(),diccionario_5.values()):
    print(str(c)+ " - " + str(v['poblacion']))
    
for p in diccionario_5:
    if 'playas' in diccionario_5[p]:
        print(str(p)+" tiene "+ str(diccionario_5[p]['playas'])+" playas") 
    else:
        print(p + " no tiene playa")       