from datetime import datetime, timedelta
from random import randint

class Unidad:
    actual_codigo = 0

    def __init__(self, vencimiento: str, tipo, ubicacion, oferta=False):
        Unidad.actual_codigo += 1
        self.codigo = Unidad.actual_codigo
        self.vencimiento = vencimiento
        self.tipo = tipo
        self.bodega = ubicacion
        self.descuentos = []
        self.en_paquete = False
        tipo.agregarUnidad(self, ubicacion)
        ubicacion.agregarProducto(self)
        self.oferta = oferta
        self.ubicacion = ubicacion

    def getCodigo(self) -> int:
        return self.codigo

    def setCodigo(self, codigo: int):
        self.codigo = codigo

    def getVencimiento(self) -> str:
        return self.vencimiento

    def setVencimiento(self, vencimiento: str):
        self.vencimiento = vencimiento

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getUbicacion(self):
        return self.bodega

    def setUbicacion(self, ubicacion):
        self.bodega = ubicacion

    @staticmethod
    def generarFechaVencimiento() -> str:
        fecha_actual = datetime.now()
        # Generar un número aleatorio de días entre -8 y 60
        dias_aleatorios = randint(-3, 45)
        # Sumar esos días a la fecha actual
        fecha_aleatoria = fecha_actual + timedelta(days=dias_aleatorios)
        return fecha_aleatoria.strftime('%Y-%m-%d')

    def diasParaVencimiento(self) -> int:
        hoy = datetime.now()
        venc = datetime.strptime(self.vencimiento, '%Y-%m-%d')
        dias = (venc - hoy).days
        return dias

    def calcularOferta(self):
        descuento_final = None
        valor_descuento = 0
        if self.descuentos:
            for descuento in self.descuentos:
                if descuento.getPorcentajeDescuento() > valor_descuento:
                    valor_descuento = descuento.getPorcentajeDescuento()
                    descuento_final = descuento
        return descuento_final

    def calcularPrecio(self):
        descuento = self.calcularOferta()
        if descuento:
            return self.getTipo().getPrecio() * (100 - descuento.getPorcentajeDescuento()) / 100
        else:
            return self.getTipo().getPrecio()

    def isOferta(self) -> bool:
        return len(self.descuentos) > 0

    def getDescuentos(self):
        return self.descuentos

    def setDescuentos(self, descuentos):
        self.descuentos = descuentos

    def agregarDescuento(self, descuento):
        self.descuentos.append(descuento)

    def eliminarDescuento(self, descuento):
        self.descuentos.remove(descuento)

    def isEnPaquete(self) -> bool:
        return self.en_paquete

    def setEnPaquete(self, en_paquete: bool):
        self.en_paquete = en_paquete

    def __str__(self):
        tipo_str = str(self.getTipo())  # Llama al método getTipo y convierte a string
        return (f"{self.diasParaVencimiento()})")