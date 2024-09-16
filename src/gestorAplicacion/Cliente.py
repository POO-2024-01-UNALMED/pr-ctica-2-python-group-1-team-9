from gestorAplicacion.Persona import Persona
from gestorAplicacion.Supermercado import Supermercado

class Cliente(Persona):
    def __init__(self, nombre, cedula, supermercado):
        super().__init__(nombre, cedula, "Cliente")
        self._supermercado = supermercado
        self._ordenes = []
        self._puntos = 0

    def informacion(self):
        return f"{self.nombre} con cédula {self.cedula} en el supermercado {self._supermercado.getNombre()}"

    def agregarOrden(self, orden):
        self._ordenes.append(orden)
        self._actualizarPuntos()

    def _actualizarPuntos(self):
        self._puntos = len(self._ordenes)

    def getOrdenes(self):
        return self._ordenes

    def setOrdenes(self, ordenes):
        self._ordenes = ordenes

    def getPuntos(self):
        return self._puntos

    def setPuntos(self, puntos):
        self._puntos = puntos

    def getSupermercado(self):
        return self._supermercado

    def __str__(self):
        return f"Cliente con nombre {self.nombre}, cédula {self.cedula}, y supermercado {self._supermercado.getNombre()}"
