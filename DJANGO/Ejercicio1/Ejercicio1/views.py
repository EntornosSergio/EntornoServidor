from django.http import HttpResponse
from django.shortcuts import render

def edad(request,e,a):
    total=a-2025
    total+=e
    contexto={'edad':total}
    return render(request,'index.html',contexto)