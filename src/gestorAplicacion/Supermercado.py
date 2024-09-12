from gestorAplicacion.Bodega import Bodega
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Orden import Orden
from gestorAplicacion.Unidad import Unidad
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
    
    def getNombre(self) -> str:
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getSaldo(self) -> float:
        return self.saldo

    def setSaldo(self, saldo: float):
        self.saldo = saldo

    def actualizarSaldo(self, monto: float):
        self.saldo += monto

    def getEmpleados(self):
        return self.empleados

    def setEmpleados(self, empleados):
        self.empleados = empleados

    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)

    def quitarEmpleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)

    def getBodegas(self):
        return self.bodegas

    def setBodegas(self, bodegas):
        self.bodegas = bodegas

    def agregarBodega(self, bodega):
        self.bodegas.append(bodega)

    def quitarBodega(self, bodega):
        if bodega in self.bodegas:
            self.bodegas.remove(bodega)

    def getOrdenes(self):
        return self.ordenes

    def setOrdenes(self, ordenes):
        self.ordenes = ordenes

    def agregarOrden(self, orden):
        self.ordenes.append(orden)

    def quitarOrden(self, orden):
        if orden in self.ordenes:
            self.ordenes.remove(orden)

    @staticmethod
    def getSupermercados():
        return Supermercado.supermercados

    @staticmethod
    def setSupermercados(supermercados):
        Supermercado.supermercados = supermercados

    def getProductosPromocion(self):
        return self.productos_promocion

    def setProductosPromocion(self, productos_promocion):
        self.productos_promocion = productos_promocion

    def getPaquetesPromocion(self):
        return self.paquetes_promocion

    def setPaquetesPromocion(self, paquetes_promocion):
        self.paquetes_promocion = paquetes_promocion

    def agregarPaquetePromocion(self, paquete_promocion):
        self.paquetes_promocion.append(paquete_promocion)

    def quitarPaquetePromocion(self, paquete_promocion):
        if paquete_promocion in self.paquetes_promocion:
            self.paquetes_promocion.remove(paquete_promocion)

    def productosPorTipo(self, tipo: 'TipoProducto'):
        resultado = []
        for bodega in self.bodegas:
            productos = bodega.getProductos()
            for unidad in productos:
                if unidad.getTipo().getTipo() == tipo:
                    print("Agregando " + unidad.getTipo().getNombre())
                    if unidad.getTipo() not in resultado:
                        resultado.append(unidad.getTipo())
        return resultado

    def numeroUnidades(self, producto):
        if self in producto.getSupermercados():
            indice = producto.getSupermercados().index(self)
            return producto.getUnidadesSupermercado()[indice]
        return 0
    