#Este será el main
#voy a ver si si sirve lo de tk


import tkinter as tk 
from tkinter import ttk 

class Ventana_prueba(ttk.Frame):
  
  def __init__(self, ventana):
    super().__init__(ventana)
    #configuramos el  nombre y el tamaño de la ventana 
    ventana.title("Supermercado los programers")

    #creamos la configuración de la página
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight= 1)


    self.Label1 = tk.Label(self, text="INICIO", bg= "#FFA500")
    self.Label1.grid(row=0, column=0, sticky="nsew", columnspan=2)


    self.Label2 = tk.Label(self, text="INICIO", bg= "#FFA500")
    self.Label2.grid(row=1, column=0, sticky="nsew", columnspan=2)

    self.grid(sticky="n")
    self.rowconfigure(0, weight=3)

ventana = tk.Tk()
Practica = Ventana_prueba(ventana)
Practica.mainloop()

from gestorAplicacion.VentanaPrincipal import VentanaPrincipal
from gestorAplicacion.ventanaInicio import VentanaInicio
import tkinter as tk
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Bodega import Bodega
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Unidad import Unidad
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Descuento import Descuento
import pickle


if __name__ == "__main__":

    #root = tk.Tk()
    #ventana = VentanaPrincipal(root)
    #root.mainloop()
    """
# Crear instancias
    sup1 = Supermercado("MercaChicles", 1000000)
    sup2 = Supermercado("El Gangazo", 12000000)
    sup3 = Supermercado("Mercatodo", 900000)
    emp1 = Empleado("Pepe Pineda", 12345, sup1, "Ventas", 2000000)
    emp2 = Empleado("Pancho Alzate", 65485, sup1, "Asesor", 2500000)
    emp3 = Empleado("Juanito Alimana", 666999, sup1, "Ventas", 2100000)
    emp4 = Empleado("Pedro Navaja", 963258, sup2, "Ventas", 2000000)
    emp5 = Empleado("Betty Lafea", 467852, sup2, "Secretaria", 2400000)
    emp6 = Empleado("Jose Rodriguez", 643816, sup2, "Asesor", 2450000)
    emp7 = Empleado("Lucho Diaz", 4736512, sup3, "Ventas", 2010000)
    emp8 = Empleado("Betty Lafea", 467852, sup3, "Ventas", 1950000)
    emp9 = Empleado("Willie Colon", 864325, sup3, "Caja", 2005000)
    cli1 = Cliente("Jaimito Maravilla", 23456)
    cli2 = Cliente("Pedro Escamoso", 411359)
    cli3 = Cliente("Lucas Tadeo", 435864)
    cli4 = Cliente("Alfredo Mercurio", 943567)
    cli5 = Cliente("Axel Rosas", 73465)
    bod1 = Bodega("Bodega Principal", "Cordoba", sup1)
    bod2 = Bodega("Bodega Secundaria", "La Piedra", sup1)
    bod3 = Bodega("Bodega Terciaria", "El Monte", sup1)
    bod4 = Bodega("Bodega La Esquinita", "La Esquina", sup2)
    bod5 = Bodega("Bodega Medieval", "El pasado", sup2)
    bod6 = Bodega("Bodega El colchon", "La cama", sup3)
    bod7 = Bodega("Bodega Pollito", "Kokoriko", sup3)
    sup1.agregarEmpleado(emp1)
    sup1.agregarEmpleado(emp2)
    sup1.agregarEmpleado(emp3)
    sup1.agregarBodega(bod1)
    sup1.agregarBodega(bod2)
    sup1.agregarBodega(bod3)
    sup2.agregarEmpleado(emp4)
    sup2.agregarEmpleado(emp5)
    sup2.agregarEmpleado(emp6)
    sup2.agregarBodega(bod4)
    sup2.agregarBodega(bod5)
    sup3.agregarEmpleado(emp7)
    sup3.agregarEmpleado(emp8)
    sup3.agregarEmpleado(emp9)
    sup3.agregarBodega(bod6)
    sup3.agregarBodega(bod7)

    prod1 = Producto("leche Colanta", TipoProducto.BEBIDA, 3000, 2000)
    prod2 = Producto("vodka Absoluti", TipoProducto.BEBIDA, 90000, 50000)
    prod3 = Producto("leche Alqueria", TipoProducto.ALIMENTO, 3100, 2100)
    prod4 = Producto("detergente Fav", TipoProducto.ASEO, 6500, 5000)
    prod5 = Producto("jabón Dove", TipoProducto.CUIDADOPERSONAL, 18900, 13450)
    prod6 = Producto("cuido Dog Chow", TipoProducto.MASCOTA, 125000, 98000)
    prod7 = Producto("spray Raid", TipoProducto.OTRO, 17000, 15100)
    prod8 = Producto("cepillo Pro 425", TipoProducto.CUIDADOPERSONAL, 4700, 3000)

    uni100 = Unidad("2024-09-20", prod1, bod1)
    uni102 = Unidad("2024-08-01", prod1, bod1)
    uni103 = Unidad("2024-10-05", prod1, bod2)
    uni101 = Unidad("2024-09-20", prod1, bod1)
    uni102 = Unidad("2024-08-01", prod1, bod1)
    uni103 = Unidad("2024-10-05", prod1, bod2)
    uni101 = Unidad("2024-09-20", prod1, bod1)
    uni102 = Unidad("2024-08-01", prod1, bod1)
    uni103 = Unidad("2024-10-05", prod1, bod2)

    uni4 = Unidad("2024-09-30", prod2, bod2)
    uni5 = Unidad("2024-07-08", prod2, bod1)
    uni6 = Unidad("2024-11-27", prod2, bod1)
    uni7 = Unidad("2024-12-08", prod3, bod2)
    uni8 = Unidad("2024-10-20", prod3, bod1)
    uni9 = Unidad("2024-09-27", prod3, bod2)
    uni10 = Unidad("2025-01-30", prod3, bod1)

    descuento_uno = Descuento("Refrescantes y baratas", TipoProducto.BEBIDA, 10)
    descuento_dos = Descuento("Borrachera económica", prod2, 15)
    """