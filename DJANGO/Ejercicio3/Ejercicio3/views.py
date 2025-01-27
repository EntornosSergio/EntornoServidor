from django.shortcuts import render
from datetime import datetime

def mostrar_fecha(request):
    # Obtiene la fecha y hora actuales
    fecha_actual = datetime.now()
    contexto = {
        'Dia': fecha_actual.day,
        'Mes': fecha_actual.month,
        'Año': fecha_actual.year,
    }
    return render(request, 'index.html', contexto)
