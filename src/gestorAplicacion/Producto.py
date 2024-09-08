from .TipoProducto import TipoProducto
from .Unidad import Unidad

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
    def listar_productos_por_tipo(tipo_producto, supermercado, cantidad):
        resultado = []
        for bodega in supermercado.get_bodegas():
            for producto in bodega.get_productos():
                if producto.get_tipo().tipo == tipo_producto:
                    resultado.append(producto)
        return resultado

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_precio(self):
        return self.precio_venta

    def set_precio(self, precio):
        self.precio_venta = precio

    def cantidad_unidades(self):
        return len(self.unidades)

    def get_precio_compra(self):
        return self.precio_compra

    def set_precio_compra(self, precio_compra):
        self.precio_compra = precio_compra

    def get_unidades(self):
        return self.unidades

    def get_unidades_supermercado(self, supermercado):
        unidadessup = []
        for bodega in supermercado.get_bodegas():
            for unidad in bodega.get_productos():
                if unidad.get_tipo() == self:
                    unidadessup.append(unidad)
        return unidadessup

    def set_unidades(self, unidades):
        self.unidades = unidades

    def agregar_unidad(self, unidad, bodega):
        self.unidades.append(unidad)
        if bodega.get_supermercado() not in self.supermercados:
            self.supermercados.append(bodega.get_supermercado())
            self.unidades_supermercado.append(1)
        else:
            indice = self.supermercados.index(bodega.get_supermercado())
            self.unidades_supermercado[indice] += 1

    def actualizar_unidad(self, unidad):
        if unidad.get_ubicacion().get_supermercado() not in self.supermercados:
            self.supermercados.append(unidad.get_ubicacion().get_supermercado())
            self.unidades_supermercado.append(1)
            print(f"Añadiendo {unidad.get_ubicacion().get_supermercado().get_nombre()} indice {self.supermercados.index(unidad.get_ubicacion().get_supermercado())}")
        else:
            indice = self.supermercados.index(unidad.get_ubicacion().get_supermercado())
            self.unidades_supermercado[indice] += 1
            print(f"{unidad.get_ubicacion().get_supermercado().get_nombre()} ya está índice {self.supermercados.index(unidad.get_ubicacion().get_supermercado())}")
            print(f"Nuevo valor {self.unidades_supermercado[self.supermercados.index(unidad.get_ubicacion().get_supermercado())]}")

    def quitar_unidad(self, unidad):
        self.unidades.remove(unidad)

    @staticmethod
    def get_lista_productos():
        return Producto.lista_productos

    @staticmethod
    def set_lista_productos(lista_productos):
        Producto.lista_productos = lista_productos

    def get_precio_venta(self):
        return self.precio_venta

    def set_precio_venta(self, precio_venta):
        self.precio_venta = precio_venta

    def get_supermercados(self):
        return self.supermercados

    def set_supermercados(self, supermercados):
        self.supermercados = supermercados

    def get_unidades_supermercado(self):
        return self.unidades_supermercado

    def set_unidades_supermercado(self, unidades_supermercado):
        self.unidades_supermercado = unidades_supermercado
