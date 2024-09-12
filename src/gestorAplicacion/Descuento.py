from Producto import Producto
from TipoProducto import TipoProducto
from Unidad import Unidad

class Descuento:
    _descuentos = []

    def __init__(self, nombre, tipo_o_producto_o_unidad, porcentaje_descuento):
        self._nombre = nombre
        self._tipo_en_promocion = None
        self._producto_en_promocion = None
        self._unidad_en_promocion = None
        self._is_activo = True
        self._porcentaje_descuento = porcentaje_descuento

        if isinstance(tipo_o_producto_o_unidad, TipoProducto):
            self._tipo_en_promocion = tipo_o_producto_o_unidad
            self.calcularDescuento(1)
        elif isinstance(tipo_o_producto_o_unidad, Producto):
            self._producto_en_promocion = tipo_o_producto_o_unidad
            self.calcularDescuento(2)
        elif isinstance(tipo_o_producto_o_unidad, Unidad):
            self._unidad_en_promocion = tipo_o_producto_o_unidad
            self.calcularDescuento(3)

        Descuento._descuentos.append(self)

    def calcularDescuento(self, i):
        if i == 1:
            for producto in Producto.getListaProductos():
                if producto.getTipo() == self._tipo_en_promocion:
                    for unidad in producto.getUnidades():
                        unidad.agregarDescuento(self)
        elif i == 2:
            if self._producto_en_promocion is not None:
                for unidad in self._producto_en_promocion.getUnidades():
                    unidad.agregarDescuento(self)
        elif i == 3:
            if self._unidad_en_promocion is not None:
                self._unidad_en_promocion.agregarDescuento(self)

    # Getters y Setters
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getTipoEnPromocion(self):
        return self._tipo_en_promocion

    def setTipoEnPromocion(self, tipo_en_promocion):
        self._tipo_en_promocion = tipo_en_promocion

    def getProductoEnPromocion(self):
        return self._producto_en_promocion

    def setProductoEnPromocion(self, producto_en_promocion):
        self._producto_en_promocion = producto_en_promocion

    def getUnidadEnPromocion(self):
        return self._unidad_en_promocion

    def setUnidadEnPromocion(self, unidad_en_promocion):
        self._unidad_en_promocion = unidad_en_promocion

    def isActivo(self):
        return self._is_activo

    def setIsActivo(self, is_activo):
        self._is_activo = is_activo

    def getPorcentajeDescuento(self):
        return self._porcentaje_descuento

    def setPorcentajeDescuento(self, porcentaje_descuento):
        self._porcentaje_descuento = porcentaje_descuento

    @staticmethod
    def getDescuentos():
        return Descuento._descuentos

    @staticmethod
    def setDescuentos(descuentos):
        Descuento._descuentos = descuentos
