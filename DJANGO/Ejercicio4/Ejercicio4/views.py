from django.shortcuts import render
from Ejercicio4.models.Lenguaje import Plantilla 

def progra(request):
    x = [  
        Plantilla(nombre="Java", año=2000, descripcion="Lenguaje orientado a objetos"),
        Plantilla(nombre="Python", año=1991, descripcion="Lenguaje de programación fácil de aprender"),
        Plantilla(nombre="C++", año=1985, descripcion="Lenguaje poderoso con control de bajo nivel"),
        Plantilla(nombre="JavaScript", año=1995, descripcion="Lenguaje usado para desarrollo web"),
        Plantilla(nombre="Ruby", año=1995, descripcion="Lenguaje con sintaxis elegante"),         
    ]
    
    return render(request, 'lenguajes.html', {'plantillas': x})  

