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
from tkinter import ttk

def primerFuncion():
    mostrarFucionalidades("Orden de compra", "Creación de nueva orden de compra. Seleccione el supermercado donde se realizará la compra, seguido del empleado y del cliente.")
    segundaventana.limpiarFrame(segundaventana.frameProceso)
    supermercado1 = preguntarSupermercado()
    print(supermercado1.getNombre())
    preguntarEmpleado()
    preguntarCliente()

def segundaFuncion():
    mostrarFucionalidades("Administrar inventario", "Ingrese el número de días que se usará como criterio para verificar la fecha de vencimiento de los productos disponibles.")
    segundaventana.limpiarFrame(segundaventana.frameProceso)
    preguntarSupermercado()
    preguntarEmpleado()

def terceraFuncion():
    mostrarFucionalidades("Intercambio de Productos", "Seleccione dos supermercados para realizar un intercambio de productos entre estos.")
    segundaventana.limpiarFrame(segundaventana.frameProceso)
    preguntarSupermercado()
    preguntarEmpleado()

def MostrarVentanaPrincipal(primerventana):
    primerventana.withdraw()
    segundaventana.deiconify()

def mostrarFucionalidades(NombreProceso, DescripcionProceso):
    
    segundaventana.labelInformativo.pack_forget()
    segundaventana.frameDeInteraccion.grid_rowconfigure(2, weight=1)
    segundaventana.frameDeInteraccion.grid_columnconfigure(0, weight=1)

    segundaventana.frameNombreProceso.grid(row=0, column=0, pady=(5,2.5), padx=5, ipady=2)
    segundaventana.labelNombreProceso.config(text=NombreProceso)
    segundaventana.labelNombreProceso.pack(padx=5, pady=5)
 
    segundaventana.frameDescripcionProceso.grid(row=1, column=0, sticky="ew", pady=(2.5,2.5), padx=5, ipady=4)
    segundaventana.labelDescripcionProceso.config(text=DescripcionProceso)
    segundaventana.labelDescripcionProceso.pack(padx=5, pady=5, expand= True, fill="x")
    
    segundaventana.frameProceso.grid(row=2, column=0, sticky="n", pady=(2.5,5), padx=5)

def preguntarSupermercado():
    supermercado = tk.StringVar()
    frame1 = tk.Frame(segundaventana.frameProceso)
    frame1.pack(expand=True,fill="both",padx=10,pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)
    labelsup = tk.Label(frame1, text="Supermercado", font=("Arial"))
    labelsup.grid(row=0, column=0, pady=5, padx=5, sticky="e")
    lista = []
    for supermercado in Supermercado.getSupermercados():
        lista.append(supermercado.getNombre())
    combosup = ttk.Combobox(frame1, values=lista, state="readonly", textvariable=supermercado)
    combosup.grid(row=0, column=1, pady=5, padx=5,sticky="w")
    

def preguntarEmpleado():
    #frameDescripcionProceso.config
    pass

def preguntarCliente():
    #frameDescripcionProceso.config
    pass

if __name__ == "__main__":

    Serializacion.deserializar()

    primerventana = VentanaInicio()
    primerventana.botonP4.config(command=lambda: MostrarVentanaPrincipal(primerventana))
    
    segundaventana = VentanaPrincipal(primerventana)
    segundaventana.withdraw()

    segundaventana.menuBar.add_cascade(label="Archivo", menu=segundaventana.menuArchivo) 
    segundaventana.menuArchivo.add_command(label="Aplicación", command= segundaventana.ventanaDeDialogoInfoBasica)
    segundaventana.menuArchivo.add_command(label="Salir", command= segundaventana.regresarVentanaInicio)

    segundaventana.menuBar.add_cascade(label="Procesos y Consultas", menu=segundaventana.menuProcesosYConsultas)
    segundaventana.menuProcesosYConsultas.add_command(label="Administar inventario", command=segundaFuncion)
    segundaventana.menuProcesosYConsultas.add_command(label="Generar Orden", command=primerFuncion)
    segundaventana.menuProcesosYConsultas.add_command(label="Intercambio de Productos", command=terceraFuncion)

    segundaventana.menuBar.add_cascade(label="Ayuda", menu=segundaventana.menuAyuda)
    segundaventana.menuAyuda.add_command(label="Acerda de:", command=segundaventana.ventanaDeDialogoAcercaDe)

    primerventana.mainloop()