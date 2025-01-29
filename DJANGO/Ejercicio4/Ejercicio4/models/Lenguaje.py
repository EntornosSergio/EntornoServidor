class Plantilla:
    def __init__(self, nombre, año, descripcion):
        self._nombre = nombre 
        self._año = año
        self._descripcion = descripcion

    def get_nombre(self):
        return self._nombre

    def get_año(self):
        return self._año

    def get_ciudad(self):
        return self._descripcion