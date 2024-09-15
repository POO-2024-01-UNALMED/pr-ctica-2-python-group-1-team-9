from gestorAplicacion.Persona import Persona
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Descuento import Descuento
import pickle

class Serializacion:

    @classmethod
    def deserializar(cls):
        pkldescuentos = open("src/baseDatos/descuentos.pkl", "rb")
        pklpersonas = open("src/baseDatos/personas.pkl", "rb")
        pklproductos = open("src/baseDatos/productos.pkl", "rb")
        pklsupermercados = open("src/baseDatos/supermercados.pkl", "rb")
        try:
            Descuento.setDescuentos(pickle.load(pkldescuentos))
        except EOFError:
            print("El archivo de descuentos está vacio")
        try:
            Persona.setPersonas(pickle.load(pklpersonas))
        except EOFError:
            print("El archivo de personas está vacio")
        try:
            Producto.setListaProductos(pickle.load(pklproductos))
        except EOFError:
            print("El archivo de productos está vacio")
        try:
            Supermercado.setSupermercados(pickle.load(pklsupermercados))
        except EOFError:
            print("El archivo de supermercados está vacio")
        pkldescuentos.close()
        pklpersonas.close()
        pklproductos.close()
        pklsupermercados.close()

    @classmethod
    def serializar(cls):
        pkldescuentos = open("src/baseDatos/descuentos.pkl", "wb")
        pklpersonas = open("src/baseDatos/personas.pkl", "wb")
        pklproductos = open("src/baseDatos/productos.pkl", "wb")
        pklsupermercados = open("src/baseDatos/supermercados.pkl", "wb")
        descuentos = Descuento.getDescuentos()
        personas = Persona.getPersonas()
        productos = Producto.getListaProductos()
        supermercados = Supermercado.getSupermercados()
        pickle.dump(descuentos, pkldescuentos)
        pickle.dump(personas, pklpersonas)
        pickle.dump(productos, pklproductos)
        pickle.dump(supermercados, pklsupermercados)
        pkldescuentos.close()
        pklpersonas.close()
        pklproductos.close()
        pklsupermercados.close()