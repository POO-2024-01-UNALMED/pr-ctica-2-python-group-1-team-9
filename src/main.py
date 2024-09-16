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

import re
import tkinter as tk
from tkinter import ttk, messagebox

class Aplicacion():

    def __init__(self):
        self.supsel = None
        self.empsel = None
        self.clisel = None

        self.orden = None

        self.listasup = []
        self.listacli = []

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

        def crearOrden():
            if self.supsel and self.empsel and self.clisel:
                self.orden = Orden(self.supsel, self.empsel, self.clisel)
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

                            #frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#ffffff")
                            #frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

                self.limpiarFrame(frame3)
                tk.Label(frame3, text="Nombre").grid(row=0, column=0, pady=5, padx=5, sticky="e")
                entryNombre = tk.Entry(frame3)
                entryNombre.grid(row=0, column=1, pady=5, padx=5, sticky="w")

                tk.Label(frame3, text="Cédula").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                entryCedula = tk.Entry(frame3)
                entryCedula.grid(row=1, column=1, pady=5, padx=5, sticky="w")

                tk.Button(frame3, text="Crear Cliente", command=crearCliente).grid(row=2, column=0, pady=10, padx=10, columnspan=2)
                #tk.Button(frame3, text="Crear Orden", command=crearOrden).grid(row=3, column=0, pady=10, padx=10, columnspan=2)


        frame1 = tk.Frame(self.segundaventana.frameProceso, bg="#ffffff")
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

        frame2 = tk.Frame(frame1, bd=2, relief="groove", bg="#ffffff")
        frame2.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        seleccion = tk.IntVar()
        tk.Radiobutton(frame2, text="Cliente Existente", variable=seleccion, value=1, command=onSelect).grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        tk.Radiobutton(frame2, text="Cliente Nuevo", variable=seleccion, value=2, command=onSelect).grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        seleccion.set(1)
        frame3 = tk.Frame(frame2, bg="#ffffff")
        frame3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        onSelect()

    def segundaFuncion(self):
        self.mostrarFucionalidades("Administrar inventario", "Administración de inventario. Seleccione el supermercado donde se realizarán las modificaciones")
        self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)

        def supSelect(event):
            supsel = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == combosup.get()), None)

            if supsel:
                listaemp = [persona.getNombre() for persona in Persona.getPersonas()
                            if persona.getCargo() != "Cliente" and persona.getSupermercado().getNombre() == supsel.getNombre()]

                def empSelect(event):
                    empsel = next((persona for persona in Persona.getPersonas() if persona.getNombre() == comboemp.get()), None)

                    if empsel:
                        primerFieldFrame = FieldFrame(self.segundaventana.frameProceso, tituloCriterios="Parametro de busqueda", criterios=["Días"], 
                                                    tituloValores="Cantidad", valores=None, habilitado=None)
                        primerFieldFrame.pack()

                        def aceptar():
                            diasIngresados = primerFieldFrame.entradas[0].get()
                            if not diasIngresados:
                                messagebox.showwarning("Advertencia", ExceptionSugerida2())
                            elif not diasIngresados.isdigit():
                                messagebox.showwarning("Advertencia", ExceptionSugerida1())
                            else:
                                diasIngresados = int(diasIngresados)
                                bodegas = supsel.getBodegas()
                                unidades = [producto for bodega in bodegas for producto in bodega.getProductos()]
                                avencer = [unidad for unidad in unidades if unidad.diasParaVencimiento() <= diasIngresados]
                                avencer.sort(key=lambda u: u.diasParaVencimiento())
                            
                            

                        primerFieldFrame.botonAceptar.config(command=aceptar)

                tk.Label(frame1, text="Empleado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
                comboemp = ttk.Combobox(frame1, values=listaemp, state="readonly")
                comboemp.bind("<<ComboboxSelected>>", empSelect)
                comboemp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        frame1 = tk.Frame(self.segundaventana.frameProceso, bg="#ffffff")
        frame1.pack(expand=True, fill="both", padx=10, pady=10)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)

        lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
        tk.Label(frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        combosup = ttk.Combobox(frame1, values=lista, state="readonly")
        combosup.bind("<<ComboboxSelected>>", supSelect)
        combosup.grid(row=0, column=1, pady=5, padx=5, sticky="w")


    def terceraFuncion(self):
        self.mostrarFucionalidades("Intercambio de Productos", "Seleccione dos supermercados para realizar un intercambio de productos entre estos.")
        self.segundaventana.limpiarFrame(self.segundaventana.frameProceso)

        def supSelect(event):
            selected_sup = self.combosup1.get()  # Primer supermercado seleccionado
            lista_filtrada = [sup.getNombre() for sup in Supermercado.getSupermercados() if sup.getNombre() != selected_sup]
        
            # Actualizar el segundo Combobox con la lista filtrada
            self.combosup2.config(values=lista_filtrada)
            self.combosup2.set('')  

        def mostrar_productos():
            # Limpiar el frame de productos anterior
            for widget in self.frame_productos.winfo_children():
                widget.destroy()

            nombre_sup1 = self.combosup1.get()
            nombre_sup2 = self.combosup2.get()
            
            supermercado1 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == nombre_sup1), None)
            supermercado2 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == nombre_sup2), None)

            try:
                if not supermercado1 or not supermercado2:
                    raise ExceptionInventada3() 
                
                frame_supermercado1 = tk.Frame(self.frame_productos)
                frame_supermercado1.pack(side="left", fill="y", padx=10, pady=10)

                listbox1 = tk.Listbox(frame_supermercado1, width=40, height=15)
                scrollbar1 = tk.Scrollbar(frame_supermercado1, orient="vertical")
                scrollbar1.config(command=listbox1.yview)
                listbox1.config(yscrollcommand=scrollbar1.set)
                scrollbar1.pack(side="right", fill="y")
                listbox1.pack(side="left", fill="both", expand=True)

                # Agregar productos del supermercado 1 a la lista
                for prod in Producto.getListaProductos():
                    i = sum(1 for bodega in supermercado1.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo().getNombre() == prod.getNombre())
                    listbox1.insert("end", f"{prod.getNombre()} // {i} unidades")
                
                # Agregar el frame para el botón de flecha
                frame_flechas = tk.Frame(self.frame_productos)
                frame_flechas.pack(side="left", padx=10, pady=10)

                # Botón de flecha hacia la derecha
                boton_derecha = tk.Button(frame_flechas, text="-->", command=lambda: mover_producto(listbox1, listbox2))
                boton_derecha.pack(pady=5)

                # Botón de flecha hacia la izquierda
                boton_izquierda = tk.Button(frame_flechas, text="<--", command=lambda: mover_producto(listbox2, listbox1))
                boton_izquierda.pack(pady=5)

                frame_supermercado2 = tk.Frame(self.frame_productos)
                frame_supermercado2.pack(side="right", fill="y", padx=10, pady=10)

                listbox2 = tk.Listbox(frame_supermercado2, width=40, height=15)
                scrollbar2 = tk.Scrollbar(frame_supermercado2, orient="vertical")
                scrollbar2.config(command=listbox2.yview)
                listbox2.config(yscrollcommand=scrollbar2.set)
                scrollbar2.pack(side="right", fill="y")
                listbox2.pack(side="left", fill="both", expand=True)

                # Agregar productos del supermercado 2 a la lista
                for prod in Producto.getListaProductos():
                    i = sum(1 for bodega in supermercado2.getBodegas() for unidad in bodega.getProductos() if unidad.getTipo().getNombre() == prod.getNombre())
                    listbox2.insert("end", f"{prod.getNombre()} // {i} unidades")

            except ExceptionInventada3 as e:
                messagebox.showwarning("Advertencia", str(e))


        def confirmar_intercambio():
            supermercado1 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == self.combosup1.get()), None)
            supermercado2 = next((sup for sup in Supermercado.getSupermercados() if sup.getNombre() == self.combosup2.get()), None)

            try:
                if not supermercado1 or not supermercado2:
                    raise ExceptionInventada3() 

                confirmacion = messagebox.askyesno("Confirmar", "¿Desea intercambiar productos entre los supermercados?")
                if confirmacion:
                    envia = supermercado1
                    recibe = supermercado2
                    messagebox.showinfo("Intercambio", f"Intercambio confirmado entre {envia.getNombre()} y {recibe.getNombre()}")
            
            except ExceptionInventada3 as e:
                messagebox.showwarning("Advertencia", str(e))
                

        def mover_producto(source_listbox, target_listbox):
            selected_item = source_listbox.curselection()
            
            try:
                if not selected_item:
                    raise ExceptionInventada3("No se ha seleccionado ningún producto para mover.")
            except ExceptionInventada3 as e:
                messagebox.showwarning("Advertencia", str(e))
                return

            producto = source_listbox.get(selected_item)
            target_listbox.insert("end", producto)
            source_listbox.delete(selected_item)

        # Frame principal
        self.frame1 = tk.Frame(self.segundaventana.frameProceso, bg="#ffffff")
        self.frame1.pack(expand=True, fill="both", padx=10, pady=10)
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)

        # Combobox 1: Seleccionar primer supermercado
        tk.Label(self.frame1, text="Supermercado").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        lista = [supermercado.getNombre() for supermercado in Supermercado.getSupermercados()]
        self.combosup1 = ttk.Combobox(self.frame1, values=lista, state="readonly")
        self.combosup1.bind("<<ComboboxSelected>>", supSelect)
        self.combosup1.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        # Combobox 2: Seleccionar otro supermercado (excluye el seleccionado en el primero)
        tk.Label(self.frame1, text="Otro Supermercado").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.combosup2 = ttk.Combobox(self.frame1, values=[], state="readonly")
        self.combosup2.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        # Botones para mostrar productos y confirmar intercambio
        tk.Button(self.frame1, text="Mostrar Productos", command=mostrar_productos).grid(row=2, column=0, pady=10, padx=5, sticky="e")
        tk.Button(self.frame1, text="Confirmar Intercambio", command=confirmar_intercambio).grid(row=2, column=1, pady=10, padx=5, sticky="w")

        # Frame para mostrar productos
        self.frame_productos = tk.Frame(self.frame1)
        self.frame_productos.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")






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
