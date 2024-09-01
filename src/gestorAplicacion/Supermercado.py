import Bodega
import Empleado
import TipoProducto
import Producto
import Orden
import Unidad
import random
import datetime

class Supermercado:
    supermercados = []

    def __init__(self, nombre: str, saldo: float = 0.0):
        self.nombre = nombre
        self.saldo = saldo
        self.empleados = []
        self.bodegas = []
        self.ordenes = []
        self.productos_promocion = []
        self.paquetes_promocion = []
        Supermercado.supermercados.append(self)

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_saldo(self) -> float:
        return self.saldo

    def set_saldo(self, saldo: float):
        self.saldo = saldo

    def actualizar_saldo(self, monto: float):
        self.saldo += monto

    def get_empleados(self):
        return self.empleados

    def set_empleados(self, empleados):
        self.empleados = empleados

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def quitar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)

    def get_bodegas(self):
        return self.bodegas

    def set_bodegas(self, bodegas):
        self.bodegas = bodegas

    def agregar_bodega(self, bodega):
        self.bodegas.append(bodega)

    def quitar_bodega(self, bodega):
        if bodega in self.bodegas:
            self.bodegas.remove(bodega)

    def get_ordenes(self):
        return self.ordenes

    def set_ordenes(self, ordenes):
        self.ordenes = ordenes

    def agregar_orden(self, orden):
        self.ordenes.append(orden)

    def quitar_orden(self, orden):
        if orden in self.ordenes:
            self.ordenes.remove(orden)

    @staticmethod
    def get_supermercados():
        return Supermercado.supermercados

    @staticmethod
    def set_supermercados(supermercados):
        Supermercado.supermercados = supermercados

    def get_productos_promocion(self):
        return self.productos_promocion

    def set_productos_promocion(self, productos_promocion):
        self.productos_promocion = productos_promocion

    def get_paquetes_promocion(self):
        return self.paquetes_promocion

    def set_paquetes_promocion(self, paquetes_promocion):
        self.paquetes_promocion = paquetes_promocion

    def agregar_paquete_promocion(self, paquete_promocion):
        self.paquetes_promocion.append(paquete_promocion)

    def quitar_paquete_promocion(self, paquete_promocion):
        if paquete_promocion in self.paquetes_promocion:
            self.paquetes_promocion.remove(paquete_promocion)

    def productos_por_tipo(self, tipo: 'TipoProducto'):
        resultado = []
        for bodega in self.bodegas:
            productos = bodega.get_productos()
            for unidad in productos:
                if unidad.get_tipo().get_tipo() == tipo:
                    if unidad.get_tipo() not in resultado:
                        resultado.append(unidad.get_tipo())
        return resultado

    def numero_unidades(self, producto):
        if self in producto.get_supermercados():
            indice = producto.get_supermercados().index(self)
            return producto.get_unidades_supermercado()[indice]
        return 0
