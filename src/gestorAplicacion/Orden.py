from datetime import datetime

class Orden:
    actual_id = 0

    def __init__(self, supermercado, vendedor, comprador):
        Orden.actual_id += 1
        self.id = Orden.actual_id
        self.supermercado = supermercado
        supermercado.agregarOrden(self)
        self.empleado = vendedor
        self.cliente = comprador
        self.productos = []
        self.precio_total = 0
        self.fecha = datetime.now().date().isoformat()
        self.hora = datetime.now().time().isoformat()

    def agregarProducto(self, supermercado, producto, cantidad):
        while cantidad > 0:
            for unidad in producto.unidades:
                if not unidad.oferta and unidad.ubicacion.supermercado == supermercado:
                    self.productos.append(unidad)
                    unidad.tipo.quitarUnidad(unidad)
                    unidad.ubicacion.quitarProducto(unidad)
                    cantidad -= 1
                    break

    def agregarUnidad(self, unidad):
        self.productos.append(unidad)
        unidad.tipo.quitarUnidad(unidad)
        unidad.ubicacion.quitarProducto(unidad)

    def quitarUnidad(self, unidad):
        self.productos.remove(unidad)
        unidad.tipo.agregarUnidad(unidad, unidad.ubicacion)
        unidad.ubicacion.agregarProducto(unidad)

    def calcularPrecioTotal(self):
        total = sum(unidad.calcularPrecio() for unidad in self.productos)
        return total

    def completarOrden(self):
        self.cliente.agregarOrden(self)

    def cancelarOrden(self):
        for unidad in self.productos:
            unidad.tipo.agregarUnidad(unidad, unidad.ubicacion)
            unidad.ubicacion.agregarProducto(unidad)
        self.productos = None

    def setSupermercado(self, supermercado):
        self.supermercado = supermercado

    def getSupermercado(self):
        return self.supermercado
    
    def setEmpleado(self, empleado):
        self.empleado = empleado

    def getEmpleado(self):
        return self.empleado
    
    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente
    
    def setProductos(self, productos):
        self.productos = productos

    def getProductos(self):
        return self.productos
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id