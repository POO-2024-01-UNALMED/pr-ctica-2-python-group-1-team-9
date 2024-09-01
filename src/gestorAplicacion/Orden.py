from datetime import datetime

class Orden:
    actual_id = 0

    def __init__(self, supermercado, vendedor, comprador):
        Orden.actual_id += 1
        self.id = Orden.actual_id
        self.supermercado = supermercado
        supermercado.agregar_orden(self)
        self.empleado = vendedor
        self.cliente = comprador
        self.productos = []
        self.precio_total = 0
        self.fecha = datetime.now().date().isoformat()
        self.hora = datetime.now().time().isoformat()

    def agregar_producto(self, supermercado, producto, cantidad):
        while cantidad > 0:
            for unidad in producto.unidades:
                if not unidad.oferta and unidad.ubicacion.supermercado == supermercado:
                    self.productos.append(unidad)
                    unidad.tipo.quitar_unidad(unidad)
                    unidad.ubicacion.quitar_producto(unidad)
                    cantidad -= 1
                    break

    def agregar_unidad(self, unidad):
        self.productos.append(unidad)
        unidad.tipo.quitar_unidad(unidad)
        unidad.ubicacion.quitar_producto(unidad)

    def quitar_unidad(self, unidad):
        self.productos.remove(unidad)
        unidad.tipo.agregar_unidad(unidad, unidad.ubicacion)
        unidad.ubicacion.agregar_producto(unidad)

    def calcular_precio_total(self):
        total = sum(unidad.calcular_precio() for unidad in self.productos)
        return total

    def completar_orden(self):
        self.cliente.agregar_orden(self)

    def cancelar_orden(self):
        for unidad in self.productos:
            unidad.tipo.agregar_unidad(unidad, unidad.ubicacion)
            unidad.ubicacion.agregar_producto(unidad)
        self.productos = None
