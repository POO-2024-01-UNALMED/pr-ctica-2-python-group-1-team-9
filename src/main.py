from gestorAplicacion.Persona import Persona
from gestorAplicacion.Empleado import Empleado
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado
from gestorAplicacion.Orden import Orden
from gestorAplicacion.TipoProducto import TipoProducto
from gestorAplicacion.Producto import Producto
from gestorAplicacion.Unidad import Unidad
from gestorAplicacion.Descuento import Descuento
from gestorAplicacion.Bodega import Bodega
from baseDatos.Serializacion import Serializacion
from uiMain.VentanaInicio import VentanaInicio
from uiMain.VentanaPrincipal import VentanaPrincipal
from uiMain.FieldFrame import FieldFrame
import tkinter as tk

def primerFuncion():
    mostrarFucionalidades("Creación de orden de compra", "Seleccione el supermercado que hará la venta")
    preguntarSupermercado()

def MostrarVentanaPrincipal(primerventana):
    primerventana.withdraw()
    segundaventana.deiconify()

def crearMenu(): # Función para crear el menú
    menuBar = tk.Menu(segundaventana)
    segundaventana.config(menu=menuBar)

    menuArchivo = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Archivo", menu=menuArchivo) 
    menuArchivo.add_command(label="Aplicación", command= segundaventana.ventanaDeDialogoInfoBasica)
    menuArchivo.add_command(label="Salir", command= segundaventana.regresarVentanaInicio)

    menuProcesosYConsultas = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesosYConsultas)
    menuProcesosYConsultas.add_command(label="Administar inventario")
    menuProcesosYConsultas.add_command(label="Generar Orden", command=primerFuncion)
    menuProcesosYConsultas.add_command(label="Intercambio de Productos (sin implementar)")

    menuAyuda = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label="Ayuda", menu=menuAyuda)
    menuAyuda.add_command(label="Acerda de:", command=segundaventana.ventanaDeDialogoAcercaDe)

def mostrarFucionalidades(NombreProceso, DescripcionProceso):
    
    segundaventana.labelInformativo.pack_forget()
    segundaventana.frameDeInteraccion.grid_rowconfigure(2, weight=1)
    segundaventana.frameDeInteraccion.grid_columnconfigure(0, weight=1)

    frameNombreProceso = tk.Frame(segundaventana.frameDeInteraccion, bg="black")
    frameNombreProceso.grid(row=0, column=0, pady=(5,2.5), padx=5, ipady=2)
    labelNombreProceso = tk.Label(frameNombreProceso, text=NombreProceso, font=("Arial"), bg="white")
    labelNombreProceso.pack(padx=5, pady=5, expand= True)

    frameDescripcionProceso = tk.Frame(segundaventana.frameDeInteraccion, bg="black")
    frameDescripcionProceso.grid(row=1, column=0, sticky="ew", pady=(2.5,2.5), padx=5, ipady=4)
    labelDescripcionProceso = tk.Label(frameDescripcionProceso, text=DescripcionProceso ,font=("Arial"), bg="white")
    labelDescripcionProceso.pack(padx=5, pady=5, expand= True, fill="x")

    frameProceso = tk.Frame(segundaventana.frameDeInteraccion, bg="green")
    frameProceso.grid(row=2, column=0, sticky="snew", pady=(2.5,5), padx=5)

def preguntarSupermercado():
    #frameDescripcionProceso.config
    pass

if __name__ == "__main__":

    primerventana = VentanaInicio()
    primerventana.botonP4.config(command=lambda: MostrarVentanaPrincipal(primerventana))
    
    segundaventana = VentanaPrincipal(primerventana)
    segundaventana.withdraw()
    crearMenu()
    primerventana.mainloop()