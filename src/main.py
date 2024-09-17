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
from gestorAplicacion.ErrorAplicacion import *
import random

import re
import tkinter as tk
from tkinter import ttk, messagebox

class Aplicacion():

    def __init__(self):
        self.supsel = None
        self.empsel = None
        self.clisel = None
        self.tipsel = None
        self.prodsel = None

        self.corredor = 0

        self.orden = None

        self.listasup = []
        self.listacli = []
        self.lista_unidades = []
        self.lista1 = []
        self.lista2 = []
        self.listaAvencer = []

        self.primerventana = VentanaInicio()
        self.segundaventana = VentanaPrincipal(self.primerventana)

    # Función para aplicar estilos a los widgets
    def aplicar_estilos(widget):
        widget.config(font=("Arial", 12), background="#f4f4f4", foreground="#000000")
        if isinstance(widget, tk.Label):
            widget.config(bg="#f4f4f4")
        elif isinstance(widget, ttk.Combobox):
            widget.config(style="TCombobox")
        elif isinstance(widget, tk.Button):
            widget.config(bg="#cccccc", activebackground="#aaaaaa")

    def limpiarFrame(self, frame): # Recorremos todos los widgets dentro del frame y los destruimos
        for widget in frame.winfo_children():
            widget.destroy()

    def primerFuncion(self):
        self.mostrarFucionalidades("Orden de compra", "Creación de nueva orden de compra. Seleccione el supermercado donde se realizará la compra, seguido del empleado y del cliente.")
        self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)

        def supSelect(event):
            self.supsel = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup.get()), None)
            listaemp = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() != "Cliente" if persona.getSupermercado().getNombre() == self.supsel.getNombre()]
            comboemp.config(values=listaemp)
            comboemp.set("")

        def empSelect(event):
            self.empsel = next((persona for persona in Persona.getPersonas() if persona.getNombre() == comboemp.get()), None)

        def menuOrden(orden):
            def agregarProducto():
                self.tipsel == None

                def tipSelect(event):
                    if combotip.get() == "Alimentos":
                        self.tipsel = TipoProducto.ALIMENTO
                    elif combotip.get() == "Aseo":
                        self.tipsel = TipoProducto.ASEO
                    elif combotip.get() == "Bebidas":
                        self.tipsel = TipoProducto.BEBIDA
                    elif combotip.get() == "Cuidado personal":
                        self.tipsel = TipoProducto.CUIDADOPERSONAL
                    elif combotip.get() == "Productos para mascotas":
                        self.tipsel = TipoProducto.MASCOTA
                    elif combotip.get() == "Otro":
                        self.tipsel = TipoProducto.OTRO

                    listaprod = [producto.getNombre() for producto in self.orden.getSupermercado().productosPorTipo(self.tipsel)]
                    comboprod.config(values=listaprod)
                    comboprod.set("")

                def prodSelect(event):
                    self.lista_unidades = []
                    listbox1.delete(0, tk.END)
                    self.prodsel = next((prod for prod in Producto.getListaProductos() if prod.getNombre() == comboprod.get()), None)
                    for uni in self.prodsel.getUnidades():
                        if uni.getUbicacion().getSupermercado().getNombre() == self.orden.getSupermercado().getNombre():
                            self.lista_unidades.append(uni)
                            if uni.isOferta():
                                listbox1.insert("end", f"{uni.getTipo().getNombre()} {uni.calcularOferta().getNombre()}({uni.calcularOferta().getPorcentajeDescuento()}%) ${uni.calcularPrecio()}")         
                            else:
                                listbox1.insert("end", f"{uni.getTipo().getNombre()} ${uni.calcularPrecio()}")

                def regresar():
                    menuOrden(self.orden)

                def agregar():
                    selected_item = listbox1.curselection()
                    try:
                        self.orden.agregarUnidad(self.lista_unidades[selected_item[0]])
                        del self.lista_unidades[selected_item[0]]
                        listbox1.delete(0, tk.END)
                        for uni in self.prodsel.getUnidades():
                            if uni.getUbicacion().getSupermercado().getNombre() == self.orden.getSupermercado().getNombre():
                                self.lista_unidades.append(uni)
                                if uni.isOferta():
                                    listbox1.insert("end", f"{uni.getTipo().getNombre()} {uni.calcularOferta().getNombre()}({uni.calcularOferta().getPorcentajeDescuento()}%) ${uni.calcularPrecio()}")         
                                else:
                                    listbox1.insert("end", f"{uni.getTipo().getNombre()} ${uni.calcularPrecio()}")
                    except IndexError:
                        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna unidad de la lista.")
                        

                self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)
                self.segundaventana.labelDescripcionProceso.config(text="Seleccione los valores correspondientes en cada una de las listas desplegables, luego seleccione una unidad de la lista de la derecha y presione el botón Agregar Producto para agregarlo a la orden.")
                self.segundaventana.frameProceso.grid_forget()
                self.segundaventana.frameProceso.grid(row=2, column=0, sticky="new", pady=(2.5, 5), padx=5)

                frame_lista = tk.Frame(self.segundaventana.frameProceso, bd=3, relief="raised")
                frame_combos = tk.Frame(self.segundaventana.frameProceso, bd=3, relief="raised")
                frame_lista.pack(side="right", fill="both", expand=True)
                frame_combos.pack(side="left", fill="y")

                listbox1 = tk.Listbox(frame_lista, height=20)
                scrollbar1 = tk.Scrollbar(frame_lista, orient="vertical")
                scrollbar1.config(command=listbox1.yview)
                listbox1.config(yscrollcommand=scrollbar1.set)
                scrollbar1.pack(side="right", fill="y")
                listbox1.pack(side="left", fill="both", expand=True)

                tk.Label(frame_combos, text="Tipo de Producto").grid(row=0, column=0, pady=5, padx=5, sticky="e")
                combotip = ttk.Combobox(frame_combos, values=["Alimentos", "Aseo", "Bebidas", "Cuidado personal", "Productos para mascotas", "Otro"], state="readonly")
                combotip.bind("<<ComboboxSelected>>", tipSelect)
                combotip.grid(row=0, column=1, pady=5, padx=5, sticky="w")

                tk.Label(frame_combos, text="Producto").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                prodvariable = tk.StringVar()
                comboprod = ttk.Combobox(frame_combos,textvariable=prodvariable, state="readonly")
                comboprod.bind("<<ComboboxSelected>>", prodSelect)
                comboprod.grid(row=1, column=1, pady=5, padx=5, sticky="w")

                tk.Button(frame_combos, text="Agregar Producto", command=agregar).grid(row=2, column=0, pady=5, padx=5, sticky="e")
                tk.Button(frame_combos, text="Regresar al menú anterior", command=regresar).grid(row=2, column=1, pady=5, padx=5, sticky="e")

            def completarOrden():
                try:
                    if len(self.orden.getProductos()) != 0:
                        self.orden.completarOrden()
                        messagebox.showinfo("Orden Completada", "La orden se completó con éxito.")
                        self.segundaventana.limpiarFrame(self.segundaventana.frameDeInteraccion)
                        self.segundaventana.crearLabelInformativo()
                        self.segundaventana.crearFrames()

                    else:
                        raise ExceptionInventada5()
                except ExceptionInventada5 as e:
                    messagebox.showwarning("Advertencia", str(e))

            def cancelarOrden():
                if len(self.orden.getProductos())==0:
                    self.orden.cancelarOrden()
                    messagebox.showinfo("Orden Cancelada", "La orden se canceló.")
                    self.segundaventana.limpiarFrame(self.segundaventana.frameDeInteraccion)
                    self.segundaventana.crearLabelInformativo()
                    self.segundaventana.crearFrames()
                else:
                    if messagebox.askyesno("Advertencia", "¿Desea cancelar la orden y regresar todos los productos?."):
                        self.orden.cancelarOrden()
                        messagebox.showinfo("Orden Cancelada", "La orden se canceló.")
                        self.segundaventana.limpiarFrame(self.segundaventana.frameDeInteraccion)
                        self.segundaventana.crearLabelInformativo()
                        self.segundaventana.crearFrames()

            def menu():
                def quitarProducto():
                    selected_item = listbox1.curselection()
                    try:
                        self.orden.quitarUnidad(self.orden.getProductos()[selected_item[0]])
                        listbox1.delete(0, tk.END)
                        for unidad in self.orden.getProductos():
                            if not unidad.isOferta():
                                listbox1.insert("end", f"{unidad.getTipo().getNombre()} ${unidad.calcularPrecio()}")
                            else:
                                listbox1.insert("end", f"{unidad.getTipo().getNombre()} {unidad.calcularOferta().getNombre()}({unidad.calcularOferta().getPorcentajeDescuento()}%) ${unidad.calcularPrecio()}")

                    except IndexError:
                        messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna unidad de la lista.")

                self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)
                self.segundaventana.labelDescripcionProceso.config(text=f"Orden id: {orden.getId()}\nSupermercado: {orden.getSupermercado().getNombre()}\nEmpleado: {orden.getEmpleado().getNombre()}\nCliente: {orden.getCliente().getNombre()}")
                self.segundaventana.frameProceso.grid_forget()
                self.segundaventana.frameProceso.grid(row=2, column=0, sticky="new", pady=(2.5, 5), padx=5)

                frame_orden = tk.Frame(self.segundaventana.frameProceso, bd=3, relief="raised")
                frame_botones = tk.Frame(self.segundaventana.frameProceso, bd=3, relief="raised")
                frame_inferior = tk.Frame(self.segundaventana.frameProceso)
                frame_inferior.pack(side="bottom", expand=True)
                frame_orden.pack(side="right", fill="both", expand=True)
                frame_botones.pack(side="left", fill="y")
                

                tk.Label(frame_orden, text=f"Precio total: ${orden.calcularPrecioTotal()}").pack(side="bottom", fill="x", expand=True)
                listbox1 = tk.Listbox(frame_orden, height=20)
                scrollbar1 = tk.Scrollbar(frame_orden, orient="vertical")
                scrollbar1.config(command=listbox1.yview)
                listbox1.config(yscrollcommand=scrollbar1.set)
                scrollbar1.pack(side="right", fill="y")
                listbox1.pack(side="left", fill="both", expand=True)

                # Botones
                tk.Button(frame_botones, text="Agregar Productos", command=agregarProducto).grid(row=0, column=0, pady=10, padx=10)
                tk.Button(frame_botones, text="Quitar Producto", command=quitarProducto).grid(row=1, column=0, pady=10, padx=10)
                tk.Button(frame_inferior, text="Completar Orden", command=completarOrden).grid(row=0, column=0, sticky="e", pady=10, padx=10)
                tk.Button(frame_inferior, text="Cancelar Orden", command=cancelarOrden).grid(row=0, column=1, sticky="w", pady=10, padx=10)

                for i, unidad in enumerate(self.orden.getProductos(), start=1):
                    if not unidad.isOferta():
                        listbox1.insert("end", f"{unidad.getTipo().getNombre()} ${unidad.calcularPrecio()}")
                    else:
                        listbox1.insert("end", f"{unidad.getTipo().getNombre()} {unidad.calcularOferta().getNombre()}({unidad.calcularOferta().getPorcentajeDescuento()}%) ${unidad.calcularPrecio()}")

            menu()

        def crearOrden():
            if self.supsel and self.empsel and self.clisel:
                self.orden = Orden(self.supsel, self.empsel, self.clisel)
                menuOrden(self.orden)
            else:
                messagebox.showwarning("Advertencia", "Seleccione al menos un valor en cada campo.")

        def onSelect():
            self.clisel = None
            if seleccion.get() == 1:  # Cliente Existente
                def cliSelect(event):
                    self.clisel = next((clie for clie in Persona.getPersonas() if clie.getNombre() == combocli.get()), None)
                
                self.limpiarFrame(frame3)
                tk.Label(frame3, text="Cliente").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                combocli = ttk.Combobox(frame3, values=self.listacli, state="readonly")
                combocli.bind("<<ComboboxSelected>>", cliSelect)
                combocli.grid(row=1, column=1, pady=5, padx=5, sticky="w")
                tk.Button(frame3, text="Crear Orden", command=crearOrden).grid(row=2, column=0, pady=10, padx=10, columnspan=2)

            elif seleccion.get() == 2:  # Cliente Nuevo
                def validar_entrada(nombre, cedula):
                    if not nombre or not cedula:
                        raise ValueError(ExceptionSugerida2())
                    if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑüÜ ]+$", nombre):
                        raise ValueError(ExceptionSugerida1())
                    if not re.match("^\d+$", cedula):
                        raise ValueError(ExceptionSugerida1())
                    if len(cedula) > 15:
                        raise ValueError(ExceptionInventada1())
                    return True

                def crearCliente():
                    nombre = entryNombre.get()
                    cedula = entryCedula.get()

                    try:
                        if validar_entrada(nombre, cedula):
                            nuevo_cliente = Cliente(nombre, cedula)
                            self.listacli = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() == "Cliente"]
                            messagebox.showinfo("Éxito", "Cliente creado y agregado a la base de datos.")
                            self.clisel = nuevo_cliente
                            seleccion.set(1)
                            onSelect()

                    except ValueError as e:
                        messagebox.showwarning("Advertencia", f"Error al crear el cliente: {e}")

                self.limpiarFrame(frame3)
                tk.Label(frame3, text="Nombre").grid(row=0, column=0, pady=5, padx=5, sticky="e")
                entryNombre = tk.Entry(frame3)
                entryNombre.grid(row=0, column=1, pady=5, padx=5, sticky="w")

                tk.Label(frame3, text="Cédula").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                entryCedula = tk.Entry(frame3)
                entryCedula.grid(row=1, column=1, pady=5, padx=5, sticky="w")

                tk.Button(frame3, text="Crear Cliente", command=crearCliente).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                #tk.Button(frame3, text="Crear Orden", command=crearOrden).grid(row=3, column=0, pady=10, padx=10, columnspan=2)


        frame1 = tk.Frame(self.segundaventana.frameProceso)
        frame1.pack(expand=True, fill="both", padx=10, pady=10)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)

        self.listasup = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
        self.listacli = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() == "Cliente"]

        tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        combosup = ttk.Combobox(frame1, values=self.listasup, state="readonly")
        combosup.bind("<<ComboboxSelected>>", supSelect)
        combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        tk.Label(frame1, text="Empleado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        empvariable = tk.StringVar()
        comboemp = ttk.Combobox(frame1,textvariable=empvariable, state="readonly")
        comboemp.bind("<<ComboboxSelected>>", empSelect)
        comboemp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        frame2 = tk.Frame(frame1, bd=2, relief="groove")
        frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        seleccion = tk.IntVar()
        tk.Radiobutton(frame2, text="Cliente Existente", variable=seleccion, value=1, command=onSelect).grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        tk.Radiobutton(frame2, text="Cliente Nuevo", variable=seleccion, value=2, command=onSelect).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        seleccion.set(1)
        frame3 = tk.Frame(frame2)
        frame3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        onSelect()

    def segundaFuncion(self):
        self.mostrarFucionalidades("Administrar inventario", "Administración de inventario. Seleccione el supermercado donde se realizarán las modificaciones")
        self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)
        self.corredor = 0
        self.supsel = None
        self.clisel = None
        rangodias = None
        listaDefieldsFrames = []
        self.listaAvencer = []

        def supSelect(event):
            self.supsel = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup.get()), None)
            listaemp = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() != "Cliente" if persona.getSupermercado().getNombre() == self.supsel.getNombre()]
            comboemp.config(values=listaemp)
            comboemp.set("")
            if self.empsel is not None:
                self.empsel = None

        def empSelect(event):
            self.empsel = next((persona for persona in Persona.getPersonas() if persona.getNombre() == comboemp.get()), None)
        
        def validarDescuento():
            for widget in self.segundaventana.frameProceso.winfo_children():
                widget.pack_forget()
            listaDefieldsFrames[self.corredor].pack(expand = True, fill = "both")
            listaDefieldsFrames[self.corredor].botonAceptar.config(command= lambda: aceptar2(listaDefieldsFrames[self.corredor]))
        
        def aceptar1(primmerFieldFrame):
            try:

                if frameProductosVencidos.winfo_manager() == "grid":
                    frameProductosVencidos.grid_forget()
                if frameProductosPorVencer.winfo_manager() == "grid":
                    frameProductosPorVencer.grid_forget()
                if labelVencidos.winfo_manager() == "grid":
                    labelVencidos.grid_forget()
                if labelPorVencer.winfo_manager() == "grid":
                    labelPorVencer.grid_forget()

                for entrada in primmerFieldFrame.entradas:
                    if entrada.get() is None or entrada.get() == "":
                        raise ExceptionSugerida2()

                if not re.match("^\d+$", primmerFieldFrame.entradas[0].get()):
                    raise ExceptionSugerida1()
                
                rangodias = int(primmerFieldFrame.entradas[0].get())

                mostrarProductos(rangodias)

            except ExceptionSugerida2 as e2:
                messagebox.showwarning("Advertencia",str(e2))

            except ExceptionSugerida1 as e1:
                messagebox.showwarning("Advertencia",str(e1))
            
        def aceptar2(frame):
            try:
                if self.corredor+1 < len(listaDefieldsFrames):
                    self.corredor = self.corredor + 1

                    if frame.entradas[3].get() is None or frame.entradas[3].get() == "":
                        raise ExceptionSugerida2()

                    if not re.match("^\d+$", frame.entradas[3].get()):
                        raise ExceptionSugerida1()
                    
                    if int(frame.entradas[3].get()) > 0:
                        nuevoDescuento = Descuento("Descuento por vencimiento",(self.listaAvencer[self.corredor]),int(frame.entradas[3].get()))

                    validarDescuento()
                
                else:
                    messagebox.showinfo("Información", "Cambios realizados exitosamente")
                    self.segundaventana.limpiarFrame(self.segundaventana.frameDeInteraccion)
                    self.segundaventana.crearLabelInformativo()
                    self.segundaventana.crearFrames()

            except ExceptionSugerida2 as e2:
                messagebox.showwarning("Advertencia",str(e2))

            except ExceptionSugerida1 as e1:
                messagebox.showwarning("Advertencia",str(e1))
            

        def mostrarProductos(rangodias):
            try:
                if self.supsel and self.empsel and (rangodias or (rangodias == 0)):

                    if listbox3.size() > 0:
                        listbox3.delete(0, tk.END)

                    if listbox4.size() > 0:
                        listbox4.delete(0, tk.END)

                    bodegas = self.supsel.getBodegas()
                    unidades = []
                    avencer = []
                    vencidos = []

                    for bodega in bodegas:
                        unidades.extend(bodega.getProductos())
                    
                    for unidad in unidades:
                        dias = unidad.diasParaVencimiento()
                        if dias <= rangodias:
                            if dias > 0:
                                avencer.append(unidad)
                            else:
                                vencidos.append(unidad)
                        else:
                            pass
                    
                    avencer.sort(key=lambda u: u.diasParaVencimiento())

                    if rangodias == 0 and len(vencidos) > 0:

                        frame1.grid(columnspan=1)

                        labelVencidos.grid(row=1, column=0, pady=5, padx=5, sticky="we", columnspan=2)
                        frameProductosVencidos.grid(row=2, column=0, pady=5, padx=5, sticky="we", columnspan=2)

                        items1 = []

                        for unidad in vencidos:

                            item1 = f"{unidad.getTipo().getNombre()}, codigo: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}"
                            items1.append(item1)

                        for elemento in items1:
                            listbox3.insert("end", elemento)

                        anchoMax1 = max(len(item1) for item1 in items1)
                        numItems1 = listbox3.size()
                        listbox3.config(width=anchoMax1 + 1, height=min(numItems1, 10))

                        bontonParaContinuar.config(text="Eliminar Vencidos",command= lambda: ElimiarVencidos(self.supsel,rangodias))
                        bontonParaContinuar.grid(row=3, column= 0, padx=5, pady=5, columnspan=2)
                    
                    elif len(avencer) > 0 and len(vencidos) > 0:

                        frame1.grid(columnspan=2)

                        labelVencidos.grid(row=1, column=0, pady=5, padx=5, sticky="we")
                        frameProductosVencidos.grid(row=2, column=0, pady=5, padx=5, sticky="we")

                        items2 = []

                        for unidad in vencidos:
                            item2 = f"{unidad.getTipo().getNombre()}, codigo: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}"
                            items2.append(item2)

                        for elemento in items2:
                            listbox3.insert("end", elemento)

                        anchoMax2 = max(len(item2) for item2 in items2)
                        numItems2 = listbox3.size()
                        listbox3.config(width=anchoMax2 + 1, height=min(numItems2, 10))

                        botonParaEliminar.config(text="Eliminar vencidos",command= lambda: ElimiarVencidos(self.supsel,rangodias))
                        botonParaEliminar.grid(row=3, column= 0, padx=5, pady=5)

                        labelPorVencer.grid(row=1, column=1, pady=5, padx=5, sticky="we")
                        frameProductosPorVencer.grid(row=2, column=1, pady=5, padx=5, sticky="we")

                        items3 = []

                        for unidad in avencer:

                            item3 = f"{unidad.getTipo().getNombre()}, codigo: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}, Días para vencer: {unidad.diasParaVencimiento()}"
                            items3.append(item3)

                        for elemento in items3:
                            listbox4.insert("end", elemento)

                        anchoMax3 = max(len(item3) for item3 in items3)
                        numItems3 = listbox4.size()
                        listbox4.config(width=anchoMax3 + 1, height=min(numItems3, 10))

                        botonParaDescuentos.config(text="Continuar",command= lambda: continuarDescuentos(self.supsel,rangodias))
                        botonParaDescuentos.grid(row=3, column= 1, padx=5, pady=5)

                    elif len(avencer) > 0 and len(vencidos) == 0:

                        frame1.grid(columnspan=1)

                        labelPorVencer.grid(row=1, column=0, pady=5, padx=5, sticky="we", columnspan=2)
                        frameProductosPorVencer.grid(row=2, column=0, pady=5, padx=5, sticky="we", columnspan=2)

                        items4 = []

                        for unidad in avencer:
                            item4 = f"{unidad.getTipo().getNombre()}, codigo: {unidad.getCodigo()}, Ubicación: {unidad.getUbicacion().getNombre()}, Días para vencer: {unidad.diasParaVencimiento()}"
                            items4.append(item4)
                        
                        for elemento in items4:
                            listbox4.insert("end", elemento)

                        anchoMax4 = max(len(item4) for item4 in items4)
                        numItems4 = listbox4.size()
                        listbox4.config(width=anchoMax4 + 1, height=min(numItems4, 10))

                        bontonParaContinuar.config(text="Continuar",command= lambda: continuarDescuentos(self.supsel,rangodias))
                        bontonParaContinuar.grid(row=3, column= 0, padx=5, pady=5, columnspan=2)

                    else:
                        messagebox.showinfo("Información",f"No hay productos vencidos, o proximos a vencer en {rangodias} dias")

                else:
                    raise ExceptionSugerida2()
            except ExceptionSugerida2 as e2:
                messagebox.showwarning("Advertencia",str(e2))

        def ElimiarVencidos(supermercado,rangodias):

            listbox3.delete(0, tk.END)
            
            labelVencidos.grid_forget()
            frameProductosVencidos.grid_forget()
            bontonParaContinuar.grid_forget()
            botonParaEliminar.destroy()

            bodegas = supermercado.getBodegas()
            unidades2 = []

            for bodega in bodegas:
                unidades2.append(bodega.getProductos())
            
            for unidades in unidades2:
                for unidadd in unidades:
                    dias2 = unidadd.diasParaVencimiento()
                    if dias2 <= rangodias and dias2 <= 0:
                        unidadd.getUbicacion().quitarProducto(unidadd)
                        unidadd.getTipo().getUnidades().remove(unidadd)

        def continuarDescuentos(supermercado,rangodias):
            self.mostrarFucionalidades("Administrar inventario", "Administración de inventario. Ingrese el descuento de cada producto proximo a vencer.")
            self.corredor = 0
            bodegas = supermercado.getBodegas()
            unidades = []
            avencer = []

            for bodega in bodegas:
                unidades.extend(bodega.getProductos())
            
            for unidad in unidades:
                dias = unidad.diasParaVencimiento()
                if dias <= rangodias and dias > 0:
                    avencer.append(unidad)
                    self.listaAvencer.append(unidad)

            avencer.sort(key=lambda u: u.diasParaVencimiento())
            self.limpiarFrame(self.segundaventana.frameProceso)

            for unidad in avencer:
                
                if unidad.calcularOferta() is None:
                    descuento = 0
                else:
                    descuento = unidad.calcularOferta().getPorcentajeDescuento()
                    
                fieldFrameDescuento = FieldFrame(self.segundaventana.frameProceso, tituloCriterios="Info", criterios=["Producto", "Codigo","Vence en (dias)","Descuento actual (%)"], 
                            tituloValores="Valores", valores=[f"{unidad.getTipo().getNombre()}", f"{unidad.getCodigo()}",f"{unidad.diasParaVencimiento()}",f"{descuento}"], 
                            habilitado=["Noedit","Noedit","Noedit",None])

                listaDefieldsFrames.append(fieldFrameDescuento)

            validarDescuento()
            

        frame1 = tk.Frame(self.segundaventana.frameProceso)
        frame1.grid(row=0, column=0)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)

        self.listasup = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
        self.listacli = [persona.getNombre() for persona in Persona.getPersonas() if persona.getCargo() == "Cliente"]

        tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        combosup = ttk.Combobox(frame1, values=self.listasup, state="readonly")
        combosup.bind("<<ComboboxSelected>>", supSelect)
        combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        tk.Label(frame1, text="Empleado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        empvariable = tk.StringVar()
        comboemp = ttk.Combobox(frame1,textvariable=empvariable, state="readonly")
        comboemp.bind("<<ComboboxSelected>>", empSelect)
        comboemp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        primmerFieldFrame = FieldFrame(frame1, tituloCriterios="Rango de dias", criterios=["Dias"], tituloValores="Cantidad", valores=None, habilitado=None)
        primmerFieldFrame.grid(row=2, column=0, pady=5, padx=5, sticky="we", columnspan=2)
        primmerFieldFrame.botonAceptar.config(command= lambda: aceptar1(primmerFieldFrame))

        frameProductosVencidos = tk.Frame(self.segundaventana.frameProceso, padx= 5, pady=5)
        frameProductosPorVencer = tk.Frame(self.segundaventana.frameProceso, padx= 5, pady=5)

        labelVencidos = tk.Label(self.segundaventana.frameProceso, text="Productos vencidos", font=("Arial"))
        labelPorVencer = tk.Label(self.segundaventana.frameProceso, text="Productos a vencer", font=("Arial"))

        listbox3 = tk.Listbox(frameProductosVencidos)
        scrollbar3 = tk.Scrollbar(frameProductosVencidos, orient="vertical")
        scrollbar3.config(command=listbox3.yview)
        listbox3.config(yscrollcommand=scrollbar3.set)
        scrollbar3.pack(side="right", fill="y")
        listbox3.pack(side="left", fill="both", expand=True)

        listbox4 = tk.Listbox(frameProductosPorVencer)
        scrollbar4 = tk.Scrollbar(frameProductosPorVencer, orient="vertical")
        scrollbar4.config(command=listbox4.yview)
        listbox4.config(yscrollcommand=scrollbar4.set)
        scrollbar4.pack(side="right", fill="y")
        listbox4.pack(side="left", fill="both", expand=True)

        bontonParaContinuar = tk.Button(self.segundaventana.frameProceso)

        botonParaEliminar = tk.Button(self.segundaventana.frameProceso)
        botonParaDescuentos = tk.Button(self.segundaventana.frameProceso)

    def terceraFuncion(self):
        self.lista1 = []
        self.lista2 = []
        supermercado1 = None
        supermercado2 = None
        self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)
        self.mostrarFucionalidades("Intercambio de Productos", "Seleccione dos supermercados para realizar un intercambio de productos entre estos.")
        
        def supSelect(event):
            selected_sup = combosup1.get()  # Primer supermercado seleccionado
            for supermercado in Supermercado.getSupermercados():
                if supermercado.getNombre() == selected_sup:
                    supermercado1 = supermercado
            lista_filtrada = [sup.getNombre() for sup in Supermercado.getSupermercados() if sup.getNombre() != selected_sup]
            combosup2.config(values=lista_filtrada)
            combosup2.set('')

        def mostrar_productos(evento):
            self.limpiarFrame(frame_productos)
            # Limpiar el frame de productos antes de agregar nuevos elementos
            self.limpiarFrame(frame_productos)

            nombre_sup1 = combosup1.get()
            nombre_sup2 = combosup2.get()
            
            supermercado1 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == nombre_sup1), None)
            supermercado2 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == nombre_sup2), None)

            def mover_producto(ind):
                if ind == 1:
                    selected_item = listbox1.curselection()
                    lista_source = self.lista1
                    listbox_source = listbox1
                    lista_dest = self.lista2
                    listbox_dest = listbox2
                else:
                    selected_item = listbox2.curselection()
                    lista_source = self.lista2
                    listbox_source = listbox2
                    lista_dest = self.lista1
                    listbox_dest = listbox1
                    
                try:
                    lista_dest.append(lista_source[selected_item[0]])
                    listbox_dest.insert("end", f"{lista_source[selected_item[0]].getTipo().getNombre()} // Días para vencimiento: {lista_source[selected_item[0]].diasParaVencimiento()}")
                    del lista_source[selected_item[0]]

                    listbox_source.delete(selected_item[0])
                    
                except IndexError:
                    messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna unidad de la lista.")

            try:
                if not supermercado1 or not supermercado2:
                    raise ExceptionInventada3() 
                
                frame_supermercado1 = tk.Frame(frame_productos)
                frame_supermercado1.pack(side="left", fill="y", padx=10, pady=10)

                listbox1 = tk.Listbox(frame_supermercado1, width=40, height=15)
                scrollbar1 = tk.Scrollbar(frame_supermercado1, orient="vertical")
                scrollbar1.config(command=listbox1.yview)
                listbox1.config(yscrollcommand=scrollbar1.set)
                scrollbar1.pack(side="right", fill="y")
                listbox1.pack(side="left", fill="both", expand=True)

                # Agregar productos del supermercado 1 a la lista
                for bodega in supermercado1.getBodegas():
                    for unidad in bodega.getProductos():
                        self.lista1.append(unidad)
                        dias_vencimiento = unidad.diasParaVencimiento()
                        listbox1.insert("end", f"{unidad.getTipo().getNombre()} // Días para vencimiento: {dias_vencimiento}")

                frame_flechas = tk.Frame(frame_productos)
                frame_flechas.pack(side="left", padx=10, pady=10)

                boton_derecha = tk.Button(frame_flechas, text="-->", command=lambda: mover_producto(1))
                boton_derecha.pack(pady=5)


                boton_izquierda = tk.Button(frame_flechas, text="<--", command=lambda: mover_producto(2))
                boton_izquierda.pack(pady=5)


                frame_supermercado2 = tk.Frame(frame_productos)
                frame_supermercado2.pack(side="right", fill="y", padx=10, pady=10)

                listbox2 = tk.Listbox(frame_supermercado2, width=40, height=15)
                scrollbar2 = tk.Scrollbar(frame_supermercado2, orient="vertical")
                scrollbar2.config(command=listbox2.yview)
                listbox2.config(yscrollcommand=scrollbar2.set)
                scrollbar2.pack(side="right", fill="y")
                listbox2.pack(side="left", fill="both", expand=True)

                # Agregar productos del supermercado 2 a la lista
                for bodega in supermercado2.getBodegas():
                    for unidad in bodega.getProductos():
                        self.lista2.append(unidad)
                        dias_vencimiento = unidad.diasParaVencimiento()
                        listbox2.insert("end", f"{unidad.getTipo().getNombre()} // Días para vencimiento: {dias_vencimiento}")

            except ExceptionInventada3 as e:
                messagebox.showwarning("Advertencia", str(e))

        def confirmar_intercambio():
            supermercado1 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup1.get()), None)
            supermercado2 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup2.get()), None)

            try:
                if not supermercado1 or not supermercado2:
                    raise ExceptionInventada3()

                confirmacion = messagebox.askyesno("Confirmar", "¿Desea intercambiar productos entre los supermercados?")
                if confirmacion:
                    for unidad in self.lista1:
                        rand = random.randint(0, len(supermercado1.getBodegas())-1)
                        supermercado1.getBodegas()[rand].agregarProducto(unidad)
                        unidad.getUbicacion().quitarProducto(unidad)
                        unidad.setUbicacion(supermercado1.getBodegas()[rand])

                    for unidad in self.lista2:
                        rand = random.randint(0, len(supermercado2.getBodegas())-1)
                        supermercado2.getBodegas()[rand].agregarProducto(unidad)
                        unidad.getUbicacion().quitarProducto(unidad)
                        unidad.setUbicacion(supermercado2.getBodegas()[rand])

                    self.lista1 = []
                    self.lista2 = []
                    messagebox.showinfo("Intercambio", f"Intercambio confirmado entre {supermercado1.getNombre()} y {supermercado2.getNombre()}")

            except ExceptionInventada3 as e:
                messagebox.showwarning("Advertencia", str(e))

        def cancelar_intercambio():
            self.lista1 = []
            self.lista2 = []

            if messagebox.askyesno("Confirmar", "¿Dejar de realizar intercambios y regresar al menú principal?"):
                self.segundaventana.limpiarFrame(self.segundaventana.frameDeInteraccion)
                self.segundaventana.crearLabelInformativo()
                self.segundaventana.crearFrames()


        frame1 = tk.Frame(self.segundaventana.frameProceso)
        frame1.pack(expand=True, fill="both", padx=10, pady=10)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)

        tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
        combosup1 = ttk.Combobox(frame1, values=lista, state="readonly")
        combosup1.bind("<<ComboboxSelected>>", supSelect)
        combosup1.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        tk.Label(frame1, text="Otro Supermercado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        combosup2 = ttk.Combobox(frame1, values=[], state="readonly")
        combosup2.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        combosup2.bind("<<ComboboxSelected>>", mostrar_productos)

        tk.Button(frame1, text="Cancelar", command=cancelar_intercambio).grid(row=2, column=1, pady=10, padx=5, sticky="w")
        tk.Button(frame1, text="Confirmar Intercambio", command=confirmar_intercambio).grid(row=2, column=0, pady=10, padx=5, sticky="e")

        frame_productos = tk.Frame(frame1)
        frame_productos.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")


    def MostrarVentanaPrincipal(self, primerventana, segundaventana):
        primerventana.withdraw()
        segundaventana.deiconify()

    def mostrarFucionalidades(self, NombreProceso, DescripcionProceso):
        self.segundaventana.labelInformativo.pack_forget()
        self.segundaventana.frameDeInteraccion.grid_rowconfigure(2, weight=1)
        self.segundaventana.frameDeInteraccion.grid_columnconfigure(0, weight=1)

        self.segundaventana.frameNombreProceso.grid(row=0, column=0, pady=(5, 2.5), padx=5, ipady=2)
        self.segundaventana.labelNombreProceso.config(text=NombreProceso)
        self.segundaventana.labelNombreProceso.pack(padx=5, pady=5)

        self.segundaventana.frameDescripcionProceso.grid(row=1, column=0, sticky="ew", pady=(2.5, 2.5), padx=5, ipady=4)
        self.segundaventana.labelDescripcionProceso.config(text=DescripcionProceso)
        self.segundaventana.labelDescripcionProceso.pack(padx=5, pady=5, expand=True, fill="x")

        self.segundaventana.frameProceso.grid(row=2, column=0, sticky="n", pady=(2.5, 5), padx=5)

    def configurarBoton(self, ventana, ventana2):
        ventana.botonP4.config(command=lambda: self.MostrarVentanaPrincipal(ventana, ventana2))

    


class main():
    if __name__ == "__main__":
        Serializacion.deserializar()
        aplicacion = Aplicacion()
        aplicacion.segundaventana.withdraw()

        aplicacion.segundaventana.menuBar.add_cascade(label="Archivo", menu=aplicacion.segundaventana.menuArchivo)
        aplicacion.segundaventana.menuArchivo.add_command(label="Aplicación", command=aplicacion.segundaventana.ventanaDeDialogoInfoBasica)
        aplicacion.segundaventana.menuArchivo.add_command(label="Salir", command=aplicacion.segundaventana.regresarVentanaInicio)

        aplicacion.segundaventana.menuBar.add_cascade(label="Procesos y Consultas", menu=aplicacion.segundaventana.menuProcesosYConsultas)
        aplicacion.segundaventana.menuProcesosYConsultas.add_command(label="Administrar inventario", command=aplicacion.segundaFuncion)
        aplicacion.segundaventana.menuProcesosYConsultas.add_command(label="Generar Orden", command=aplicacion.primerFuncion)
        aplicacion.segundaventana.menuProcesosYConsultas.add_command(label="Intercambio de Productos", command=aplicacion.terceraFuncion)

        aplicacion.segundaventana.menuBar.add_cascade(label="Ayuda", menu=aplicacion.segundaventana.menuAyuda)
        aplicacion.segundaventana.menuAyuda.add_command(label="Acerca de:", command=aplicacion.segundaventana.ventanaDeDialogoAcercaDe)
        aplicacion.configurarBoton(aplicacion.primerventana, aplicacion.segundaventana)
        aplicacion.primerventana.mainloop()