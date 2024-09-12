import pickle
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Descuento import Descuento
from gestorAplicacion.Persona import Persona

class Serializable:
    def __init__(self):
        self.lista_de_objetos_Supermercado = Supermercado.getSupermercados() 
        self.lista_de_objetos_Producto = Producto.getListaProductos()  
        self.lista_de_objetos_Descuento = Descuento.getDescuentos() 
        self.lista_de_objetos_Persona = Persona.getPersonas()  

        self.lista_de_objetos = [
            self.lista_de_objetos_Supermercado,
            self.lista_de_objetos_Producto,
            self.lista_de_objetos_Descuento,
            self.lista_de_objetos_Persona
        ]

    def serializar(self):
        
        with open("lista_de_objetos", "wb") as fichero_binario:
            pickle.dump(self.lista_de_objetos, fichero_binario)

    
        print(f"Los supermercados guardados son los siguientes: {self.lista_de_objetos_Supermercado}")
        print(f"Los productos guardados son los siguientes: {self.lista_de_objetos_Producto}")
        print(f"Los descuentos guardados son los siguientes: {self.lista_de_objetos_Descuento}")
        print(f"Las personas guardadas son los siguientes: {self.lista_de_objetos_Persona}")

    @staticmethod
    def deserializar():
        
        with open("lista_de_objetos", "rb") as lo_guardado:
            lista = pickle.load(lo_guardado)
        return lista


serializable = Serializable()
serializable.serializar()


lista_deserializada = Serializable.deserializar()
print("Lista deserializada:", lista_deserializada)
