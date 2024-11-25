def esVocal(letra):
    if letra in ['a','e','i','o','u']:
        return True
    else:
        return False
    
def estaEnLista(letra,lista):
    if letra in lista:
        pos=lista.index(letra)
        return [letra,pos]
    else:
        return [letra,-1]    
    
def transformar(lista):
    for i in lista:
        tupla=()
        tupla.append(i)
        return (i)
    

lista=['a','e','i','o','u']
y=[]
cadena=input("Ingresa una cadena: ").lower()
for i in cadena:
    x=esVocal(i)
    if x == True:
        print(i)
        
for i in cadena:
    y.append(estaEnLista(i,lista))
  
print(y)
  
t=transformar(y)
         
print(t)
         