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

    def supSelect(event):
        empsel = ""
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
                    def onSelect():
                        if seleccion.get() == 1:
                            def cliSelect(event):
                                for clie in Persona.getPersonas():
                                    if clie.getNombre() == combocli.get():
                                        clisel = clie

                            def crearOrden():
                                print(str(type(supsel))+" "+str(type(empsel))+" "+str(type(clisel)))
                                if supsel != "" and empsel != "" and clisel != "":
                                    orden = Orden(supsel, empsel, clisel)
                                    print("Orden Creada")
                                else:
                                    print("Error, faltan datos") # Mensaje de error
                            listacli = []
                            for persona in Persona.getPersonas():
                                if persona.getCargo() == "Cliente":
                                    listacli.append(persona.getNombre())
                            labelcli = tk.Label(frame2, text="Cliente", font=("Arial"))
                            labelcli.grid(row=1, column=0, pady=5, padx=5, sticky="e")
                            combocli = ttk.Combobox(frame2, values=listacli, state="readonly")
                            combocli.bind("<<ComboboxSelected>>",cliSelect)
                            combocli.grid(row=1, column=1, pady=5, padx=5,sticky="w")
                            botoncrearorden = tk.Button(frame2, text="Crear Orden", command=crearOrden)
                            botoncrearorden.grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                        else:
                            pass
                    frame2 = tk.Frame(frame1, bd=2, relief="groove")
                    frame2.grid(row=2, column=0, columnspan=2)
                    seleccion = tk.IntVar()
                    clienteexistente = tk.Radiobutton(frame2, text="Cliente Existente", variable=seleccion, value=1, command=onSelect)
                    clienteexistente.grid(row=0, column=0, sticky="nsew")
                    clientenuevo = tk.Radiobutton(frame2, text="Cliente Nuevo", variable=seleccion, value=2, command=onSelect)
                    clientenuevo.grid(row=0, column=1, sticky="nsew")
                    seleccion.set(0)


            labelemp = tk.Label(frame1, text="Empleado", font=("Arial"))
            labelemp.grid(row=1, column=0, pady=5, padx=5, sticky="e")
            comboemp = ttk.Combobox(frame1, values=listaemp, state="readonly")
            comboemp.bind("<<ComboboxSelected>>",empSelect)
            comboemp.grid(row=1, column=1, pady=5, padx=5,sticky="w")


    supsel = ""
    empsel = ""
    clisel = ""
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