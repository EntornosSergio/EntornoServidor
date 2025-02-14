from django.shortcuts import render
from formulario.forms import Formulario

def form(request):
    if request.method == "POST":
        miFrm = Formulario(request.POST)
        if miFrm.is_valid():
            dicc = miFrm.cleaned_data
            lenguajes_seleccionados = dicc['aficiones']
            nombre= dicc['nombre']
            if len(lenguajes_seleccionados) == 0:
                mensaje = "Eres un soso " + nombre
            elif len(lenguajes_seleccionados) == 1:
                mensaje = nombre + " deberias buscar mas aficiones aparte de " + "".join(lenguajes_seleccionados)
            elif len(lenguajes_seleccionados) == 5:
                mensaje = nombre + " creo que tienes demasiadas aficiones "
            else:
                mensaje = nombre + " tienes estas aficiones: " + ", ".join(lenguajes_seleccionados)
            dicc['mensaje'] = mensaje

            return render(request, "formulario.html", dicc)
    else:
        miFrm = Formulario()

    return render(request, "index.html", {"form": miFrm})



