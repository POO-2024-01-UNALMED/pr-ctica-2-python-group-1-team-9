import pickle
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Descuento import Descuento
from gestorAplicacion.Persona import Persona


lista_de_objetos = []

class Serializable:
  def __init__():
    self.lista_de_objetos = lista_de_objetos

    lista_de_objetos_Supermercado = lista_de_objetos_Supermercado.append(Supermercado.get_supermercados())
    lista_de_objetos_Producto = lista_de_objetos_Producto.append(Producto.get_lista_productos())
    lista_de_objetos_Descuento = lista_de_objetos_Descuento.append(Descuento.get_descuentos())  
    lista_de_objetos_Persona = lista_de_objetos_Persona.append(Persona.get_personas()) 

    lista_de_objetos = lista_de_objetos.append(lista_de_objetos_Supermercado)     
    lista_de_objetos = lista_de_objetos.append(lista_de_objetos_Producto)   
    lista_de_objetos = lista_de_objetos.append(lista_de_objetos_Descuento) 
    lista_de_objetos = lista_de_objetos.append(lista_de_objetos_Persona)                                                                                                                                                                                                                                                                   

  
  fichero_binario=open("lista_de_objetos", "wb")

  pickle.dump(lista_de_objetos, fichero_binario)

  fichero_binario.close()

lo_guardado = open("lista_de_objetos", "rb")
lista = pickle.load(lo_guardado)
print(lista)




  







    

    