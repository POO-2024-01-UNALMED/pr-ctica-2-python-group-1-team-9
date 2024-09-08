import Producto
import TipoProducto
import Unidad

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
            self.calcular_descuento(1)
        elif isinstance(tipo_o_producto_o_unidad, Producto):
            self._producto_en_promocion = tipo_o_producto_o_unidad
            self.calcular_descuento(2)
        elif isinstance(tipo_o_producto_o_unidad, Unidad):
            self._unidad_en_promocion = tipo_o_producto_o_unidad
            self.calcular_descuento(3)

        Descuento._descuentos.append(self)

    def calcular_descuento(self, i):
        if i == 1:
            for producto in Producto.get_lista_productos():
                if producto.get_tipo() == self._tipo_en_promocion:
                    for unidad in producto.get_unidades():
                        unidad.agregar_descuento(self)
        elif i == 2:
            if self._producto_en_promocion is not None:
                for unidad in self._producto_en_promocion.get_unidades():
                    unidad.agregar_descuento(self)
        elif i == 3:
            if self._unidad_en_promocion is not None:
                self._unidad_en_promocion.agregar_descuento(self)

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo_en_promocion(self):
        return self._tipo_en_promocion

    @tipo_en_promocion.setter
    def tipo_en_promocion(self, tipo_en_promocion):
        self._tipo_en_promocion = tipo_en_promocion

    @property
    def producto_en_promocion(self):
        return self._producto_en_promocion

    @producto_en_promocion.setter
    def producto_en_promocion(self, producto_en_promocion):
        self._producto_en_promocion = producto_en_promocion

    @property
    def unidad_en_promocion(self):
        return self._unidad_en_promocion

    @unidad_en_promocion.setter
    def unidad_en_promocion(self, unidad_en_promocion):
        self._unidad_en_promocion = unidad_en_promocion

    @property
    def is_activo(self):
        return self._is_activo

    @is_activo.setter
    def is_activo(self, is_activo):
        self._is_activo = is_activo

    @property
    def porcentaje_descuento(self):
        return self._porcentaje_descuento

    @porcentaje_descuento.setter
    def porcentaje_descuento(self, porcentaje_descuento):
        self._porcentaje_descuento = porcentaje_descuento

    @staticmethod
    def get_descuentos():
        return Descuento._descuentos

    @staticmethod
    def set_descuentos(descuentos):
        Descuento._descuentos = descuentos
