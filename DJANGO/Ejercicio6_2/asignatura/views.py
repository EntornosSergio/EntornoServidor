from django.shortcuts import render
from django.shortcuts import render
from Ejercicio6_2.models.Asignatura import Asignatura

def asig(request):
    asignaturas_informatica = [
        Asignatura(nombre="Programación Básica", profesor="Rosa Rodríguez", numHoras=20,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Estructuras de Datos y Algoritmos", profesor="Juan Pérez", numHoras=30,img="imagenes/img.webp"),
        Asignatura(nombre="Bases de Datos", profesor="María López", numHoras=25,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Sistemas Operativos", profesor="Carlos Gómez", numHoras=35,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Redes de Computadoras", profesor="Ana Fernández", numHoras=40,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Inteligencia Artificial", profesor="Pedro Sánchez", numHoras=45,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Ciberseguridad", profesor="Lucía Ramírez", numHoras=20,img="imagenes/descarga.jpeg"),
        Asignatura(nombre="Desarrollo Web", profesor="David Herrera", numHoras=30,img="imagenes/descarga.jpeg")
    ]

    return render(request, "asignaturas.html", {"asignaturas": asignaturas_informatica})
