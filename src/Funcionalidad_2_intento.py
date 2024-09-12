import random
from datetime import datetime, timedelta
from gestorAplicacion import Supermercado, Empleado, Persona

class Empleado:
       def __init__(self, nombre, cedula, supermercado, cargo, salario):
        super().__init__(nombre, cedula, cargo)
        self.salario = salario
        self.supermercado = supermercado
        self.activo = True
        Empleado.actual_id += 1
        self.id = Empleado.actual_id
        supermercado.agregar_empleado(self)
        Empleado.empleados.append(self)
def crear_empleado():
    # Pedir los datos al usuario
    nombre = input("Ingrese el nombre del empleado: ")
    
    while True:
        try:
            cedula = int(input("Ingrese la cédula del empleado: "))
            break
        except ValueError:
            print("Error: Ingrese un número válido para la cédula.")
    
    cargo = input("Ingrese el cargo del empleado: ")
    
    while True:
        try:
            salario = float(input("Ingrese el salario del empleado: "))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico para el salario.")
    
    # Simulación de selección de supermercado
    supermercado = Supermercado("Supermercado XYZ")
    
    # Crear el empleado
    nuevo_empleado = Empleado(nombre, cedula, supermercado, cargo, salario)
    
    print(f"Empleado creado exitosamente:\nNombre: {nuevo_empleado.nombre}\nCédula: {nuevo_empleado.cedula}\nCargo: {nuevo_empleado.cargo}\nSalario: {nuevo_empleado.salario}\nSupermercado: {nuevo_empleado.supermercado.nombre}\nID: {nuevo_empleado.id}")


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
        self.empleados = []

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


def contar_tipos_diferentes(unidades):
    tipos_unicos = []
    for unidad in unidades:
        if unidad.tipo not in tipos_unicos:
            tipos_unicos.append(unidad.tipo)
    print(f"Retornando: {len(tipos_unicos)}")
    return len(tipos_unicos)

    


def administarrInventario(Supermercado):

  #primero que todo debemos tener la info de los supermercados, personas y empleados 
  lista_de_supermercados= Supermercado.get_supermertcados()
  lista_de_personas = Persona.get_personas()
  lista_de_empleados = Empleado.get_empleados()

  #nevcesito una función para verificar que si ingrwesen una palabra y no otra mondá 
  def pedirPalabra():
    while True:
        palabra = input("Ingresa una palabra: ")
        
        # Verifica si la palabra contiene solo letras
        if palabra.isalpha():
            return palabra
        else:
            print("Se permiten letras. Escribe otra cosa.")

  #verificamos que no estén vacías 

  print("Hola, estos son los supermercados que hay disponibles en nuestra app: \n" + {lista_de_supermercados})
  if (len(lista_de_supermercados) <= 0):
      print("La lista está vacía, debes agregar algún siupermercado: ")
      Añadir_supermercado = pedirPalabra()
      lista_de_supermercados.append(Añadir_supermercado)

      print("ya que creamos el supermercado, ahora debemos crear a los empleados")
      nuevo_empleado= crear_empleado()
      lista_de_empleados.append(nuevo_empleado)

      print(f"Ahora tenemos un supermercado llamado: {Añadir_supermercado} \n y un empleado llamado {nuevo_empleado} ")
      respuesta= input("¿Desea crear otro empleado?")
      while respuesta == "Si" or "SI" or "si" or "sí" or "Si" or "Sí":
        nuevo_empleado= crear_empleado()
        lista_de_empleados.append(nuevo_empleado)
        respuesta= input("¿Desea crear otro empleado?")

      print(f"luego de añadir el supermercado {Añadir_supermercado} y a los empleados" + ''.join(lista_de_empleados) + "\n debemos añadirte como -cliente-")

      



          

  else: 
    print("Estos son los supermercados que hay: ")
    for elemento in lista_de_supermercados:
      print(elemento)

  
  



    # Selección de días para la búsqueda de productos
    dias_busqueda = int(input("Ingrese los días para la búsqueda: "))
    
    # Obtener productos de todas las bodegas del supermercado
    unidades = []
    for bodega in supermercado.bodegas:
        unidades.extend(bodega.productos)
    
    # Buscar productos próximos a vencer
    avencer = [unidad for unidad in unidades if unidad.dias_para_vencimiento() <= dias_busqueda]
    
    # Ordenar por días para vencimiento
    avencer.sort(key=lambda u: u.dias_para_vencimiento())
    
    if len(avencer) == 0:
        print("No hay productos próximos a vencer en ese plazo")
        return
    
    print("Productos vencidos o próximos a vencer:\n")
    for unidad in avencer:
        if unidad.dias_para_vencimiento() <= 0:
            print(f"Nombre: {unidad.tipo.nombre}, Código: {unidad.codigo}, Ubicación: {unidad.ubicacion}, VENCIDO")
        else:
            print(f"Nombre: {unidad.tipo.nombre}, Código: {unidad.codigo}, Días para vencer: {unidad.dias_para_vencimiento()}")
    
    # Aplicar descuentos
    for unidad in avencer:
        if unidad.dias_para_vencimiento() > 0:
            print(f"\nProducto: {unidad.tipo.nombre}, Código: {unidad.codigo}, Días para vencer: {unidad.dias_para_vencimiento()}")
            if len(unidad.descuentos) == 0:
                eleccion = input("No tiene descuentos disponibles. ¿Desea crear uno? (s/n): ")
                if eleccion.lower() == 's':
                    porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
                    unidad.agregar_descuento(porcentaje_descuento)
            else:
                mejor_descuento = max(unidad.descuentos)
                print(f"Mejor descuento: {mejor_descuento}% (Precio: {unidad.calcular_precio()})")
                eleccion = input("¿Desea agregar un mejor descuento? (s/n): ")
                if eleccion.lower() == 's':
                    porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))
                    unidad.agregar_descuento(porcentaje_descuento)
    
    # Crear paquetes promocionales
    disponibles_para_paquetes = [unidad for unidad in avencer if unidad.dias_para_vencimiento() > 0]
    tipos = list(set(unidad.tipo for unidad in disponibles_para_paquetes))
    
    if len(tipos) > 1:
        eleccion = input("¿Desea crear paquetes de promociones? (s/n): ")
        if eleccion.lower() == 's':
            paquete = []
            for tipo in tipos:
                for unidad in disponibles_para_paquetes:
                    if unidad.tipo == tipo and not unidad.en_paquete:
                        paquete.append(unidad)
                        unidad.en_paquete = True
                        break
            supermercado.agregar_paquete_promocion(paquete)
            print("Paquete creado con los siguientes productos:")
            for unidad in paquete:
                print(f"- {unidad.tipo.nombre} (Código: {unidad.codigo})")

# Ejemplo de uso
if __name__ == "__main__":
    supermercado = Supermercado("Supermercado Central")
    bodega1 = Bodega("Bodega 1")
    
    tipo1 = TipoProducto("Leche", 1.50)
    tipo2 = TipoProducto("Pan", 0.50)
    
    bodega1.agregar_producto(Unidad(tipo1, "001", "Pasillo 1", datetime.now() + timedelta(days=random.randint(1, 10))))
    bodega1.agregar_producto(Unidad(tipo2, "002", "Pasillo 2", datetime.now() + timedelta(days=random.randint(1, 10))))
    
    supermercado.agregar_bodega(bodega1)
    
    administrar_inventario(supermercado)
