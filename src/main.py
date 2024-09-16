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

import re

import tkinter as tk
from tkinter import ttk, messagebox


def primerFuncion():
    mostrarFucionalidades("Orden de compra", "Creación de nueva orden de compra. Seleccione el supermercado donde se realizará la compra, seguido del empleado y del cliente.")
    segundaventana.limpiarFrame(segundaventana.frameProceso)

    def supSelect(event):
        supsel = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup.get()), None)
        if supsel:
            listaemp = [persona.getNombre() for persona in Persona.getPersonas()
                        if persona.getCargo() != "Cliente" and persona.getSupermercado().getNombre() == supsel.getNombre()]

            def empSelect(event):
                empsel = next((persona for persona in Persona.getPersonas() if persona.getNombre() == comboemp.get()), None)

                def onSelect():
                    if seleccion.get() == 1:  
                        def cliSelect(event):
                            clisel = next((clie for clie in Persona.getPersonas() if clie.getNombre() == combocli.get()), None)

                        def crearOrden():
                            if supsel and empsel and clisel:
                                orden = Orden(supsel, empsel, clisel)
                                print("Orden Creada")
                            else:
                                print("Error, faltan datos")  

                        listacli = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() == "Cliente"]
                        tk.Label(frame2, text="Cliente", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
                        combocli = ttk.Combobox(frame2, values=listacli, state="readonly")
                        combocli.bind("<<ComboboxSelected>>", cliSelect)
                        combocli.grid(row=1, column=1, pady=5, padx=5, sticky="w")
                        tk.Button(frame2, text="Crear Orden", command=crearOrden).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                    
                    elif seleccion.get() == 2:  # Cliente Nuevo
                        def crearCliente():
                            nombre = entryNombre.get()
                            cedula = entryCedula.get()

                            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑüÜ ]+$", nombre):
                                messagebox.showwarning("Advertencia", "El nombre solo puede contener letras y espacios.")
                                return

                            if nombre and cedula:
                                nuevo_cliente = Cliente(nombre, cedula, supsel)  
                                Persona.agregarPersona(nuevo_cliente)  
                                messagebox.showinfo("Éxito", "Cliente creado y agregado a la base de datos.")
                                combocli.set(nombre)  
                            else:
                                messagebox.showwarning("Advertencia", "Todos los campos deben ser llenados.")

                        frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#f4f4f4")
                        frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

                        tk.Label(frame2, text="Nombre", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5, sticky="e")
                        entryNombre = tk.Entry(frame2)
                        entryNombre.grid(row=0, column=1, pady=5, padx=5, sticky="w")

                        tk.Label(frame2, text="Cédula", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
                        entryCedula = tk.Entry(frame2)
                        entryCedula.grid(row=1, column=1, pady=5, padx=5, sticky="w")

                        tk.Button(frame2, text="Crear Cliente", command=crearCliente).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                        tk.Button(frame2, text="Crear Orden", command=lambda: crearOrden()).grid(row=3, column=0, pady=10, padx=10, columnspan=2)
                    
                    else:
                        pass

                frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#f4f4f4")
                frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
                seleccion = tk.IntVar()
                tk.Radiobutton(frame2, text="Cliente Existente", variable=seleccion, value=1, command=onSelect).grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
                tk.Radiobutton(frame2, text="Cliente Nuevo", variable=seleccion, value=2, command=onSelect).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
                seleccion.set(0)

            tk.Label(frame1, text="Empleado", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5, sticky="e")
            comboemp = ttk.Combobox(frame1, values=listaemp, state="readonly")
            comboemp.bind("<<ComboboxSelected>>", empSelect)
            comboemp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

    frame1 = tk.Frame(segundaventana.frameProceso, bg="#ffffff")
    frame1.pack(expand=True, fill="both", padx=10, pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)

    lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
    tk.Label(frame1, text="Supermercado", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5, sticky="e")
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>", supSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")


def segundaFuncion():
    mostrarFucionalidades("Administrar inventario", "Administración de inventario. Seleccione el supermercado donde se realizarán las modificaciones")
    segundaventana.limpiarFrame(segundaventana.frameProceso)
    
    def supSelect(event):
        for sup in Supermercado.getSupermercados():
            if sup.getNombre() == combosup.get():
                supsel = sup
        
        if supsel != "":
            listaemp = []
            for persona in Persona.getPersonas():
                if persona.getCargo() != "Cliente":
                    if persona.getSupermercado().getNombre() == supsel.getNombre():
                        listaemp.append(persona.getNombre())

            #Lista Empleados
            def empSelect(event):
                for persona in Persona.getPersonas():
                        if persona.getNombre() == comboemp.get():
                                empsel = persona

                if empsel != "":
                        primerFieldFrame = FieldFrame(segundaventana.frameProceso, tituloCriterios="Parametro de busqueda", criterios=["Dias"], 
                                                tituloValores="Cantidad", valores=None, habilitado=None)
                        primerFieldFrame.pack()
                        def aceptar():
                            diasIngresados = primerFieldFrame.entradas[0].get()
                            falta = False
                            for entrada in primerFieldFrame.entradas:
                                if entrada.get() is None or entrada.get() == "":
                                    falta = True
                                    break
                            if falta:
                                messagebox.showwarning("Advertencia","Faltan campos por llenar") #Esto tiene que ser con una excepcion!!!!!!!!
                            else:
                                return int(diasIngresados)
                        primerFieldFrame.botonAceptar.config(command=aceptar)
                        bodegas = supsel.getBodegas()
                        unidades = []
                        avencer = []

                        for bodega in bodegas:
                            unidades.extend(bodega.getProductos())

                        for unidad in unidades:
                            dias = unidad.diasParaVencimiento()
                            if dias <= diasIngresados:
                                avencer.append(unidad)

                        avencer.sort(key=lambda u: u.diasParaVencimiento())

            labelemp = tk.Label(frame1, text="Empleado", font=("Arial"))
            labelemp.grid(row=1, column=0, pady=5, padx=5, sticky="e")
            comboemp = ttk.Combobox(frame1, values=listaemp, state="readonly")
            comboemp.bind("<<ComboboxSelected>>",empSelect)
            comboemp.grid(row=1, column=1, pady=5, padx=5,sticky="w")

    
    diasIngresados = 0
    supsel = ""
    empsel = ""
    frame1 = tk.Frame(segundaventana.frameProceso)
    frame1.pack(expand=True,fill="both",padx=10,pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)

    # Lista Supermercados
    labelsup = tk.Label(frame1, text="Supermercado", font=("Arial"))
    labelsup.grid(row=0, column=0, pady=5, padx=5, sticky="e")
    lista = []
    for supermercado in Supermercado.getSupermercados():
        lista.append(supermercado.getNombre())
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>",supSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5,sticky="w")


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

    def onComboboxSelect(event):
        for sup in Supermercado.getSupermercados():
            if sup.getNombre() == combosup.get():
                return sup
    
    frame1 = tk.Frame(segundaventana.frameProceso)
    frame1.pack(expand=True,fill="both",padx=10,pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)
    labelsup = tk.Label(frame1, text="Supermercado", font=("Arial"))
    labelsup.grid(row=0, column=0, pady=5, padx=5, sticky="e")
    lista = []
    for supermercado in Supermercado.getSupermercados():
        lista.append(supermercado.getNombre())
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>",onComboboxSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5,sticky="w")
    
def preguntarEmpleado():
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