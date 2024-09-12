import random
from gestorAplicacion import Supermercado 
from datetime import datetime, timedelta

#aquí creo los elementos que ya existian con sus constructores (la lista d elos productos diferentes)
#lo de lso supermercados, biodega y unidad q es lo q usaremos para administrar
class TipoProducto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Unidad:
    def __init__(self, tipo, codigo, ubicacion, fecha_vencimiento):
        self.tipo = tipo
        self.codigo = codigo
        self.ubicacion = ubicacion
        self.fecha_vencimiento = fecha_vencimiento
        self.en_paquete = False
        self.descuentos = []

    def dias_para_vencimiento(self):
        return (self.fecha_vencimiento - datetime.now()).days

    def calcular_precio(self):
        if len(self.descuentos) > 0:
            return self.tipo.precio * (1 - max(self.descuentos) / 100)
        return self.tipo.precio

    def agregar_descuento(self, descuento):
        self.descuentos.append(descuento)

class Supermercado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bodegas = []
        self.paquetes_promocion = []

    def agregar_bodega(self, bodega):
        self.bodegas.append(bodega)

    def agregar_paquete_promocion(self, paquete):
        self.paquetes_promocion.append(paquete)

class Bodega:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)


        #aquía ya creo la funcionalidad que me cuenta de una lista proporcionada los elementos que no estaban ahí desde antes

def contar_tipos_diferentes(unidades):
    tipos_unicos = []
    for unidad in unidades:
        if unidad.tipo not in tipos_unicos:
            tipos_unicos.append(unidad.tipo)
    print(f"Retornando: {len(tipos_unicos)}")
    return len(tipos_unicos)

