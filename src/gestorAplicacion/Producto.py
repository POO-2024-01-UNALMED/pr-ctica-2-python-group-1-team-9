from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Unidad import Unidad

class Producto:
    actual_id = 0
    lista_productos = []

    def __init__(self, nombre: str, tipo: 'TipoProducto', precio: float = 0.0, precio_compra: float = 0.0):
        Producto.actual_id += 1
        self.id = Producto.actual_id
        self.nombre = nombre
        self.tipo = tipo
        self.precio_venta = precio
        self.precio_compra = precio_compra
        self.unidades = []
        self.supermercados = []
        self.unidades_supermercado = []
        Producto.lista_productos.append(self)

    @staticmethod
    def listarProductosPorTipo(tipo_producto, supermercado, cantidad):
        resultado = []
        for bodega in supermercado.getBodegas():
            for producto in bodega.getProductos():
                if producto.getTipo().tipo == tipo_producto:
                    resultado.append(producto)
        return resultado

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getPrecio(self):
        return self.precio_venta

    def setPrecio(self, precio):
        self.precio_venta = precio

    def cantidadUnidades(self):
        return len(self.unidades)

    def getPrecioCompra(self):
        return self.precio_compra

    def setPrecioCompra(self, precio_compra):
        self.precio_compra = precio_compra

    def getUnidades(self):
        return self.unidades

    def getUnidadesSupermercado(self, supermercado):
        unidadessup = []
        for bodega in supermercado.getBodegas():
            for unidad in bodega.getProductos():
                if unidad.getTipo() == self:
                    unidadessup.append(unidad)
        return unidadessup

    def setUnidades(self, unidades):
        self.unidades = unidades

    def agregarUnidad(self, unidad, bodega):
        self.unidades.append(unidad)
        if bodega.getSupermercado() not in self.supermercados:
            self.supermercados.append(bodega.getSupermercado())
            self.unidades_supermercado.append(1)
        else:
            indice = self.supermercados.index(bodega.getSupermercado())
            self.unidades_supermercado[indice] += 1

    def actualizarUnidad(self, unidad):
        if unidad.getUbicacion().getSupermercado() not in self.supermercados:
            self.supermercados.append(unidad.getUbicacion().getSupermercado())
            self.unidades_supermercado.append(1)
            print(f"Añadiendo {unidad.getUbicacion().getSupermercado().getNombre()} indice {self.supermercados.index(unidad.getUbicacion().getSupermercado())}")
        else:
            indice = self.supermercados.index(unidad.getUbicacion().getSupermercado())
            self.unidades_supermercado[indice] += 1
            print(f"{unidad.getUbicacion().getSupermercado().getNombre()} ya está índice {self.supermercados.index(unidad.getUbicacion().getSupermercado())}")
            print(f"Nuevo valor {self.unidades_supermercado[self.supermercados.index(unidad.getUbicacion().getSupermercado())]}")

    def quitarUnidad(self, unidad):
        self.unidades.remove(unidad)

    @staticmethod
    def getListaProductos():
        return Producto.lista_productos

    @staticmethod
    def setListaProductos(lista_productos):
        Producto.lista_productos = lista_productos

    def getPrecioVenta(self):
        return self.precio_venta

    def setPrecioVenta(self, precio_venta):
        self.precio_venta = precio_venta

    def getSupermercados(self):
        return self.supermercados

    def setSupermercados(self, supermercados):
        self.supermercados = supermercados

    def getUnidadesSupermercado(self):
        return self.unidades_supermercado

    def setUnidadesSupermercado(self, unidades_supermercado):
        self.unidades_supermercado = unidades_supermercado
