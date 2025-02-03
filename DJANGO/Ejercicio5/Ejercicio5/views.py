from django.http import HttpResponse
from django.shortcuts import render
from Ejercicio5.models.Lenguaje import Plantilla 
from Ejercicio5.forms import FormularioLenguaje

def progra(request):
    x = [  
        Plantilla(nombre="Java", año=2000, descripcion="Lenguaje orientado a objetos"),
        Plantilla(nombre="Python", año=1991, descripcion="Lenguaje de programación fácil de aprender"),
        Plantilla(nombre="C++", año=1985, descripcion="Lenguaje poderoso con control de bajo nivel"),
        Plantilla(nombre="JavaScript", año=1995, descripcion="Lenguaje usado para desarrollo web"),
        Plantilla(nombre="Ruby", año=1995, descripcion="Lenguaje con sintaxis elegante"),         
    ]
    
    return render(request, 'lenguajes.html', {'plantillas': x})  

def inicio(request):
    if request.method == "POST":
        miFrm = FormularioLenguaje(request.POST)
        if miFrm.is_valid():
            dicc = miFrm.cleaned_data
            lenguajes_seleccionados = dicc['lenguajes']
            if len(lenguajes_seleccionados) == 0:
                mensaje = "Espabila y ponte a estudiar ya"
            elif len(lenguajes_seleccionados) == 1:
                mensaje = "Estás empezando...."
            else:
                mensaje = "Sabes muchos lenguajes: " + ", ".join(lenguajes_seleccionados)
            dicc['mensaje'] = mensaje
            
            return render(request, "resultado.html", dicc)
    else:
        miFrm = FormularioLenguaje()

    return render(request, "index.html", {"form": miFrm})

