import csv

# Crear un archivo CSV ficticio
data = [
    {"ID": 1, "Nombre": "Juan Perez", "Edad": 28, "Ciudad": "Madrid", "Salario": 3000, "Anos de Experiencia": 3},
    {"ID": 2, "Nombre": "Maria Lopez", "Edad": 34, "Ciudad": "Barcelona", "Salario": 4200, "Anos de Experiencia": 8},
    {"ID": 3, "Nombre": "Carlos Sanchez", "Edad": 45, "Ciudad": "Valencia", "Salario": 3800, "Anos de Experiencia": 10},
    {"ID": 4, "Nombre": "Ana Ruiz", "Edad": 29, "Ciudad": "Sevilla", "Salario": 2900, "Anos de Experiencia": 4},
    {"ID": 5, "Nombre": "Luis Ortega", "Edad": 50, "Ciudad": "Bilbao", "Salario": 5000, "Anos de Experiencia": 20},
    {"ID": 6, "Nombre": "Olga Ruibal", "Edad": 25, "Ciudad": "Valencia", "Salario": 25000, "Anos de Experiencia": 8}

]

# Guardar los datos en un archivo CSV
with open('REPASO/empleados.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)


# Ejercicio Avanzado
"""
**Ejercicio Complejo de Python**:

1. Lee el archivo 'empleados.csv'.
"""
print("Ejercicio 1")
with open("REPASO/empleados.csv","r",encoding="latin-1") as f:
    lista=[]
    for row in f:
        lista.append(row.strip())
    print(lista[1:])
"""
2. Crea una función que calcule el salario promedio de todos los empleados.
"""
print("-"*50)
print("Ejercicio 2")
with open("REPASO/empleados.csv","r",encoding="latin-1") as f:
    lineas=f.readlines()[1:]
    total=0
    personas=0
    final=0
    for pal in lineas:
        valor=pal.split(",")
        total+=int(valor[4])
        personas+=1

    final=total/personas
    print("Suelo medio es de: " +  str(final))

"""
3. Filtra los empleados que tienen más de 5 años de experiencia y viven en una ciudad específica ingresada por el usuario.
"""
print("-"*50)
print("Ejercicio 3")

with open("REPASO/empleados.csv","r",encoding="latin-1") as f:
    lineas=f.readlines()[1:]
    final=[]
    ciudad=input("Ingrese una ciudad: ")
    for pal in lineas:
        valor=pal.split(",")
        if int(valor[5])> 5 and valor[3]==ciudad:
            final.append([pal])

    print(final)

"""
4. Genera un gráfico de barras que muestre la edad promedio de los empleados agrupados por ciudad.
5. Guarda un nuevo archivo CSV llamado 'empleados_filtrados.csv' que contenga los empleados que cumplen los criterios del punto 3.
"""

with open("REPASO/empleados_filtrados.csv","w",encoding="latin-1") as f:
    p=f.writelines(str(final))
    print("-"*50)
    print("Ejercicio 4")
    print(p)
"""

Pistas:
- Usa `pandas` para trabajar con datos.
- Usa `matplotlib` o `seaborn` para crear el gráfico.
- Maneja excepciones para entradas del usuario que no coincidan con las ciudades del archivo.
"""