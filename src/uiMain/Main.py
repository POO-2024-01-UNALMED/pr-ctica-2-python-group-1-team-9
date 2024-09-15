from uiMain.VentanaPrincipal import VentanaPrincipal as VentanaPrincipal
from uiMain.VentanaInicio import VentanaInicio as VentanaInicio
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Bodega import Bodega
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Unidad import Unidad
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Descuento import Descuento
import tkinter as tk
import pickle


if __name__ == "__main__":

    root = tk.Tk()
    ventana = VentanaPrincipal(root)
    root.mainloop()