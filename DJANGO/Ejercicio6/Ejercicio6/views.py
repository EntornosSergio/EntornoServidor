from django.shortcuts import render
from Ejercicio6.models.Asignatura import Asignatura

def asig(request):
    asignaturas_informatica = [
        Asignatura(nombre="Programación Básica", profesor="Rosa Rodríguez", numHoras=20),
        Asignatura(nombre="Estructuras de Datos y Algoritmos", profesor="Juan Pérez", numHoras=30),
        Asignatura(nombre="Bases de Datos", profesor="María López", numHoras=25),
        Asignatura(nombre="Sistemas Operativos", profesor="Carlos Gómez", numHoras=35),
        Asignatura(nombre="Redes de Computadoras", profesor="Ana Fernández", numHoras=40),
        Asignatura(nombre="Inteligencia Artificial", profesor="Pedro Sánchez", numHoras=45),
        Asignatura(nombre="Ciberseguridad", profesor="Lucía Ramírez", numHoras=20),
        Asignatura(nombre="Desarrollo Web", profesor="David Herrera", numHoras=30)
    ]

    return render(request, "asignaturas.html", {"asignaturas": asignaturas_informatica})
