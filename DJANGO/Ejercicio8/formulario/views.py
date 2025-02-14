from django.shortcuts import render
from formulario.forms import Formulario

def formulario(request):
    if request.method == "POST":
        miFrm = Formulario(request.POST)
        if miFrm.is_valid():
            dicc = miFrm.cleaned_data
            return render(request, "formulario.html", {"Formulario":[dicc]})
    else:
        miFrm = Formulario()

    return render(request, "index.html", {"form": miFrm})
