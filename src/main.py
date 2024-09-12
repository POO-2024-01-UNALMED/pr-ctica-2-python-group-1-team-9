from gestorAplicacion.VentanaPrincipal import VentanaPrincipal
from gestorAplicacion.ventanaInicio import VentanaInicio
import tkinter as tk
from gestorAplicacion import Supermercado
from gestorAplicacion import Empleado
from gestorAplicacion import Cliente
from gestorAplicacion import Bodega
from gestorAplicacion import Producto
from gestorAplicacion import Unidad
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion import Descuento


if __name__ == "__main__":

    #root = tk.Tk()
    #ventana = VentanaPrincipal(root)
    #root.mainloop()

# Crear instancias
    sup1 = Supermercado("MercaChicles", 1000000)
    emp1 = Empleado("Pepe", 12345, sup1, 2000000)
    cli1 = Cliente("Jaimito", 23456)
    bod1 = Bodega("Bodega Principal", "Cordoba", sup1)
    bod2 = Bodega("Bodega Secundaria", "La Piedra", sup1)
    sup1.agregarEmpleado(emp1)
    sup1.agregarBodega(bod1)
    sup1.agregarBodega(bod2)

    prod1 = Producto("leche Colanta", TipoProducto.BEBIDA, 3000, 2000)
    prod2 = Producto("vodka Absoluti", TipoProducto.BEBIDA, 90000, 50000)
    prod3 = Producto("leche Alqueria", TipoProducto.ALIMENTO, 3100, 2100)
    prod4 = Producto("detergente Fav", TipoProducto.ASEO, 6500, 5000)
    prod5 = Producto("jabón Dove", TipoProducto.CUIDADOPERSONAL, 18900, 13450)
    prod6 = Producto("cuido Dog Chow", TipoProducto.MASCOTA, 125000, 98000)
    prod7 = Producto("spray Raid", TipoProducto.OTRO, 17000, 15100)
    prod8 = Producto("cepillo Pro 425", TipoProducto.CUIDADOPERSONAL, 4700, 3000)

    uni1 = Unidad("2024-09-20", prod1, bod1)
    uni2 = Unidad("2024-08-01", prod1, bod1)
    uni3 = Unidad("2024-10-05", prod1, bod2)
    # No se imprime el número de unidades por ahora

    uni4 = Unidad("2024-09-30", prod2, bod2)
    uni5 = Unidad("2024-07-08", prod2, bod1)
    uni6 = Unidad("2024-11-27", prod2, bod1)
    uni7 = Unidad("2024-12-08", prod3, bod2)
    uni8 = Unidad("2024-10-20", prod3, bod1)
    uni9 = Unidad("2024-09-27", prod3, bod2)
    uni10 = Unidad("2025-01-30", prod3, bod1)

    # Continuar con el resto de unidades...

    # Crear descuentos
    descuento_uno = Descuento("Refrescantes y baratas", TipoProducto.BEBIDA, 10)
    descuento_dos = Descuento("Borrachera económica", prod2, 15)
