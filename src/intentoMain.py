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
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from gestorAplicacion.Persona import Persona
from gestorAplicacion.Cliente import Cliente

from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from gestorAplicacion.Persona import Persona
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Supermercado import Supermercado

def aplicar_estilos(widget):
    widget.config(font=("Arial", 12), background="#f4f4f4", foreground="#000000")
    if isinstance(widget, tk.Label):
        widget.config(bg="#f4f4f4")
    elif isinstance(widget, ttk.Combobox):
        widget.config(style="TCombobox")
    elif isinstance(widget, tk.Button):
        widget.config(bg="#cccccc", activebackground="#aaaaaa")

def actualizar_lista_clientes():
    lista_clientes.delete(0, tk.END)
    clientes = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() == "Cliente"]
    for cliente in clientes:
        lista_clientes.insert(tk.END, cliente)

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

                def verificarClienteExistente():
                    nombre_cliente = lista_clientes.get(tk.ACTIVE)
                    cliente_existente = next((clie for clie in Persona.getPersonas() if clie.getNombre() == nombre_cliente and clie.getCargo() == "Cliente"), None)
                    if cliente_existente:
                        messagebox.showinfo("Cliente Encontrado", f"Cliente {nombre_cliente} encontrado.")
                        combocli.set(cliente_existente.getNombre())
                    else:
                        messagebox.showwarning("Error", "Cliente no encontrado. Verifique el nombre e intente nuevamente.")

                def crearCliente():
                    nombre = entryNombre.get()
                    cedula = entryCedula.get()

                    try:
                        if validar_entrada(nombre, cedula):
                            nuevo_cliente = Cliente(nombre, cedula, supsel)
                            Persona.agregarPersona(nuevo_cliente)
                            messagebox.showinfo("Éxito", "Cliente creado y agregado a la base de datos.")
                            entryNombre.delete(0, tk.END)
                            entryCedula.delete(0, tk.END)
                            actualizar_lista_clientes()
                            combocli.set(nombre)

                    except ValueError as e:
                        messagebox.showwarning("Advertencia", f"Error al crear el cliente: {e}")

                def crearOrden():
                    # Implementa la lógica para crear una orden de compra aquí
                    messagebox.showinfo("Crear Orden", "Orden de compra creada.")

                def onSelect():
                    frame2.pack_forget()  # Ocultar el frame2 actual
                    if seleccion.get() == 1:  # Cliente Existente
                        frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#ffffff")
                        frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
                        tk.Label(frame2, text="Seleccionar Cliente").grid(row=0, column=0, pady=5, padx=5, sticky="e")

                        global lista_clientes
                        lista_clientes = tk.Listbox(frame2, height=5)
                        lista_clientes.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="ew")
                        actualizar_lista_clientes()

                        tk.Button(frame2, text="Aceptar", command=verificarClienteExistente).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                        
                        # Configura la selección del Listbox
                        lista_clientes.bind("<<ListboxSelect>>", lambda e: combocli.set(lista_clientes.get(tk.ACTIVE)))

                    elif seleccion.get() == 2:  # Cliente Nuevo
                        frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#ffffff")
                        frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
                        tk.Label(frame2, text="Nombre").grid(row=0, column=0, pady=5, padx=5, sticky="e")
                        entryNombre = tk.Entry(frame2)
                        entryNombre.grid(row=0, column=1, pady=5, padx=5, sticky="w")

                        tk.Label(frame2, text="Cédula").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                        entryCedula = tk.Entry(frame2)
                        entryCedula.grid(row=1, column=1, pady=5, padx=5, sticky="w")

                        tk.Button(frame2, text="Crear Cliente", command=crearCliente).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                        tk.Button(frame2, text="Crear Orden", command=crearOrden).grid(row=3, column=0, pady=10, padx=10, columnspan=2)

                # Se asegura de ocultar el frame2 antes de crear uno nuevo
                if 'frame2' in globals():
                    frame2.pack_forget()

                frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#ffffff")
                frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
                seleccion = tk.IntVar()
                tk.Radiobutton(frame2, text="Cliente Existente", variable=seleccion, value=1, command=onSelect).grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
                tk.Radiobutton(frame2, text="Cliente Nuevo", variable=seleccion, value=2, command=onSelect).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
                seleccion.set(0)

    frame1 = tk.Frame(segundaventana.frameProceso, bg="#ffffff")
    frame1.pack(expand=True, fill="both", padx=10, pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)

    lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
    tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>", supSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")

def segundaFuncion():
    mostrarFucionalidades("Administrar inventario", "Administración de inventario. Seleccione el supermercado donde se realizarán las modificaciones")
    segundaventana.limpiarFrame(segundaventana.frameProceso)

    def supSelect(event):
        supsel = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup.get()), None)

        if supsel:
            listaemp = [persona.getNombre() for persona in Persona.getPersonas()
                        if persona.getCargo() != "Cliente" and persona.getSupermercado().getNombre() == supsel.getNombre()]

            def empSelect(event):
                empsel = next((persona for persona in Persona.getPersonas() if persona.getNombre() == comboemp.get()), None)

                def primerFuncion():
                    mostrarFucionalidades("Administrar inventario", "Ingrese los detalles del producto a agregar al inventario.")
                    segundaventana.limpiarFrame(segundaventana.frameProceso)

                    def aceptar():
                        nombre_producto = primerFieldFrame.valorPorCampo("Nombre del producto:")
                        codigo_producto = primerFieldFrame.valorPorCampo("Código del producto:")
                        cantidad = primerFieldFrame.valorPorCampo("Cantidad a ingresar:")
                        fecha_vencimiento = primerFieldFrame.valorPorCampo("Fecha de vencimiento:")

                        if nombre_producto and codigo_producto and cantidad and fecha_vencimiento:
                            producto = Producto(nombre_producto, codigo_producto, int(cantidad), fecha_vencimiento, supsel)
                            supsel.agregarProducto(producto)
                            messagebox.showinfo("Éxito", "Producto agregado exitosamente.")
                        else:
                            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

                    primerFieldFrame = tk.Frame(segundaventana.frameProceso)
                    primerFieldFrame.pack(padx=10, pady=10, fill="both", expand=True)
                    tk.Label(primerFieldFrame, text="Detalles del Producto").pack(pady=5)

                    tk.Label(primerFieldFrame, text="Nombre del producto:").pack(pady=5)
                    entryNombre = tk.Entry(primerFieldFrame)
                    entryNombre.pack(pady=5)

                    tk.Label(primerFieldFrame, text="Código del producto:").pack(pady=5)
                    entryCodigo = tk.Entry(primerFieldFrame)
                    entryCodigo.pack(pady=5)

                    tk.Label(primerFieldFrame, text="Cantidad a ingresar:").pack(pady=5)
                    entryCantidad = tk.Entry(primerFieldFrame)
                    entryCantidad.pack(pady=5)

                    tk.Label(primerFieldFrame, text="Fecha de vencimiento:").pack(pady=5)
                    entryFecha = tk.Entry(primerFieldFrame)
                    entryFecha.pack(pady=5)

                    tk.Button(primerFieldFrame, text="Aceptar", command=aceptar).pack(pady=10)

            frame1 = tk.Frame(segundaventana.frameProceso, bg="#ffffff")
            frame1.pack(expand=True, fill="both", padx=10, pady=10)
            frame1.grid_columnconfigure(0, weight=1)
            frame1.grid_columnconfigure(1, weight=1)

            tk.Label(frame1, text="Empleado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
            comboemp = ttk.Combobox(frame1, values=listaemp, state="readonly")
            comboemp.bind("<<ComboboxSelected>>", empSelect)
            comboemp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

    frame1 = tk.Frame(segundaventana.frameProceso, bg="#ffffff")
    frame1.pack(expand=True, fill="both", padx=10, pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)

    lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
    tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>", supSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")

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

    segundaventana.frameNombreProceso.grid(row=0, column=0, pady=(5, 2.5), padx=5, ipady=2)
    segundaventana.labelNombreProceso.config(text=NombreProceso)
    segundaventana.labelNombreProceso.pack(padx=5, pady=5)

    segundaventana.frameDescripcionProceso.grid(row=1, column=0, sticky="ew", pady=(2.5, 2.5), padx=5, ipady=4)
    segundaventana.labelDescripcionProceso.config(text=DescripcionProceso)
    segundaventana.labelDescripcionProceso.pack(padx=5, pady=5, expand=True, fill="x")

    segundaventana.frameProceso.grid(row=2, column=0, sticky="n", pady=(2.5, 5), padx=5)

def preguntarSupermercado():
    def onComboboxSelect(event):
        for sup in Supermercado.getSupermercados():
            if sup.getNombre() == combosup.get():
                return sup

    frame1 = tk.Frame(segundaventana.frameProceso, bg="#ffffff")
    frame1.pack(expand=True, fill="both", padx=10, pady=10)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)

    tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
    lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
    combosup = ttk.Combobox(frame1, values=lista, state="readonly")
    combosup.bind("<<ComboboxSelected>>", onComboboxSelect)
    combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")

def preguntarEmpleado():
    pass

def preguntarCliente():
    pass

if __name__ == "__main__":
    Serializacion.deserializar()

    primerventana = VentanaInicio()
    primerventana.botonP4.config(command=lambda: MostrarVentanaPrincipal(primerventana))

    segundaventana = VentanaPrincipal(primerventana)
    segundaventana.withdraw()

    segundaventana.menuBar.add_cascade(label="Archivo", menu=segundaventana.menuArchivo)
    segundaventana.menuArchivo.add_command(label="Aplicación", command=segundaventana.ventanaDeDialogoInfoBasica)
    segundaventana.menuArchivo.add_command(label="Salir", command=segundaventana.regresarVentanaInicio)

    segundaventana.menuBar.add_cascade(label="Procesos y Consultas", menu=segundaventana.menuProcesosYConsultas)
    segundaventana.menuProcesosYConsultas.add_command(label="Administrar inventario", command=segundaFuncion)
    segundaventana.menuProcesosYConsultas.add_command(label="Generar Orden", command=primerFuncion)
    segundaventana.menuProcesosYConsultas.add_command(label="Intercambio de Productos", command=terceraFuncion)

    segundaventana.menuBar.add_cascade(label="Ayuda", menu=segundaventana.menuAyuda)
    segundaventana.menuAyuda.add_command(label="Acerca de:", command=segundaventana.ventanaDeDialogoAcercaDe)

    primerventana.mainloop()
