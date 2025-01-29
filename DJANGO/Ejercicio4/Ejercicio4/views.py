from django.shortcuts import render
from Ejercicio4.models.Lenguaje import Lenguaje

def progra(request):
    x=[
    Lenguaje(nombre="Java",año=2000,descripcion="Back")
    ]
    
    return render(request, 'index.html', x)
