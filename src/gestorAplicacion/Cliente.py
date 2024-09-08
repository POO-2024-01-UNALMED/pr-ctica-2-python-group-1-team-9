from .Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self._ordenes = []
        self._puntos = 0

    def informacion(self):
        return f"{self.nombre} con cédula {self.cedula}"

    def agregar_orden(self, orden):
        self._ordenes.append(orden)
    

    def get_ordenes(self):
        return self._ordenes

    def set_ordenes(self, ordenes):
        self._ordenes = ordenes

    def get_puntos(self):
        return self._puntos

    def set_puntos(self, puntos):
        self._puntos = puntos

    def __str__(self):
        return f"Cliente con nombre {self.nombre} y cédula {self.cedula}"