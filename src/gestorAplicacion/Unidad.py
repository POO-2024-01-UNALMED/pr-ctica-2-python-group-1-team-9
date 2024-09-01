from datetime import datetime, timedelta
from random import randint

class Unidad:
    actual_codigo = 0

    def __init__(self, vencimiento: str, tipo, ubicacion):
        Unidad.actual_codigo += 1
        self.codigo = Unidad.actual_codigo
        self.vencimiento = vencimiento
        self.tipo_producto = tipo
        self.bodega = ubicacion
        self.descuentos = []
        self.en_paquete = False
        tipo.agregar_unidad(self, ubicacion)
        ubicacion.agregar_producto(self)

    def get_codigo(self) -> int:
        return self.codigo

    def set_codigo(self, codigo: int):
        self.codigo = codigo

    def get_vencimiento(self) -> str:
        return self.vencimiento

    def set_vencimiento(self, vencimiento: str):
        self.vencimiento = vencimiento

    def get_tipo(self):
        return self.tipo_producto

    def set_tipo(self, tipo):
        self.tipo_producto = tipo

    def get_ubicacion(self):
        return self.bodega

    def set_ubicacion(self, ubicacion):
        self.bodega = ubicacion

    @staticmethod
    def generar_fecha_vencimiento() -> str:
        fecha_actual = datetime.now()
        fecha_maxima = fecha_actual + timedelta(days=60)
        dias = (fecha_maxima - fecha_actual).days
        dias_aleatorios = randint(0, dias)
        fecha_aleatoria = fecha_actual + timedelta(days=dias_aleatorios)
        fecha_aleatoria += timedelta(days=30)
        return fecha_aleatoria.strftime('%d-%m-%Y')

    def dias_para_vencimiento(self) -> int:
        hoy = datetime.now()
        venc = datetime.strptime(self.vencimiento, '%Y-%m-%d')
        dias = (venc - hoy).days
        return dias

    def calcular_oferta(self):
        descuento_final = None
        valor_descuento = 0
        if self.descuentos:
            for descuento in self.descuentos:
                if descuento.get_porcentaje_descuento() > valor_descuento:
                    valor_descuento = descuento.get_porcentaje_descuento()
                    descuento_final = descuento
        return descuento_final

    def calcular_precio(self):
        descuento = self.calcular_oferta()
        if descuento:
            return self.get_tipo().get_precio() * (100 - descuento.get_porcentaje_descuento()) / 100
        else:
            return self.get_tipo().get_precio()

    def is_oferta(self) -> bool:
        return len(self.descuentos) > 0

    def get_descuentos(self):
        return self.descuentos

    def set_descuentos(self, descuentos):
        self.descuentos = descuentos

    def agregar_descuento(self, descuento):
        self.descuentos.append(descuento)

    def eliminar_descuento(self, descuento):
        self.descuentos.remove(descuento)

    def is_en_paquete(self) -> bool:
        return self.en_paquete

    def set_en_paquete(self, en_paquete: bool):
        self.en_paquete = en_paquete
