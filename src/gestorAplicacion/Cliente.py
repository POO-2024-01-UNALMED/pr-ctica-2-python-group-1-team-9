from gestorAplicacion.Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula, "Cliente")
        self._ordenes = []
        self._puntos = 0

    def informacion(self):
        return f"{self.nombre} con cédula {self.cedula}"

    def agregarOrden(self, orden):
        self._ordenes.append(orden)
    
    def getOrdenes(self):
        return self._ordenes

    def setOrdenes(self, ordenes):
        self._ordenes = ordenes

    def getPuntos(self):
        return self._puntos

    def setPuntos(self, puntos):
        self._puntos = puntos

    def __str__(self):
        return f"Cliente con nombre {self.nombre} y cédula {self.cedula}"