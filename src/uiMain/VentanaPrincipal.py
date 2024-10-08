import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, primerventana):
        super().__init__(primerventana)
        # Configuración basica de la ventana
        self.primerventana = primerventana
        self.title("Plataforma Super Usable Para Supermercados (PSUPS)")
        self.geometry("1000x750+50+0")
        self.protocol("WM_DELETE_WINDOW", self.regresarVentanaInicio) #Si se cierra la ventana se muestra la primera y se oculta la segunda.
        self.iconbitmap("src\psups.ico")

        self.config(background="black", border=6, relief= "groove")

        self.frameDeInteraccion = tk.Frame(self, bg="#ffffff")
        self.frameDeInteraccion.pack(expand=True,fill="both",padx=10,pady=10)

        self.crearLabelInformativo()
        self.crearFrames()

        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        self.menuArchivo = tk.Menu(self.menuBar, tearoff=0)
        self.menuProcesosYConsultas = tk.Menu(self.menuBar,tearoff=0)
        self.menuAyuda = tk.Menu(self.menuBar,tearoff=0)

    def crearLabelInformativo(self):
        self.labelInformativo = tk.Label(self.frameDeInteraccion, wraplength=900, text="-Para empezar, acceda al menú superior a la opcion, 'Procesos y Consultas'.\n\nEncontrará tres opciones:\n\nPrimera opción: 'Administrar inventario', con esta podrá verificar que productos están vencidos y cuales proximos a vencer, eliminar de su inventario los productos vencidos y además hacer descuento sobre los que están proximos a vencer en el lapso de dias establecio en la busqueda.\n\nSegunda opción: 'Generar Orden', con esta función realizará las ordenes de venta, podrá crear clientes, eligiendo que tipo de producto se va a agregar a la orden, con la posibilidad de agregarlos uno a uno.\n\nTercera opción: Intercambio de productos, por medio de esta función, podra darle mejor manejo al inventario en su bodega, trasladando los productos que seleccione de un supermercado a otro.", font=("Arial"))
        self.labelInformativo.pack(expand=True, fill = "both")

    def crearFrames(self):
        self.frameNombreProceso = tk.Frame(self.frameDeInteraccion, bd=3, relief="raised")
        self.labelNombreProceso = tk.Label(self.frameNombreProceso, text="Nombre del Proceso", font=("Arial"))

        self.frameDescripcionProceso = tk.Frame(self.frameDeInteraccion, bd=3, relief="raised")
        self.labelDescripcionProceso = tk.Label(self.frameDescripcionProceso, text="Descripcion del Proceso" ,wraplength=760 ,font=("Arial"))

        self.frameProceso = tk.Frame(self.frameDeInteraccion, bd=3, relief="groove")

    def regresarVentanaInicio(self): # Oculta la segunda ventana ("Plataforma Super Usable Para Supermercados (PSUPS)") y muestra la primera ("Ventana de inicio")
        self.primerventana.deiconify()
        self.withdraw()
        self.ReiniciarFrameDeInteraccion()
        self.labelInformativo.pack(expand=True, fill = "both")
    
    def ventanaDeDialogoInfoBasica(self):
        messagebox.showinfo("Aplicación", "Con esta aplicación podrá hacer ordenes de venta, administar inventarios y relizar movimientos de mercancia entre supermercados.")

    def ventanaDeDialogoAcercaDe(self):
        messagebox.showinfo("Acerca de:", "PSUPS fue desarrollado por:\n - Jose Manuel Areiza @areizaaz\n - Oscar Daniel Ruiz @OscarDanielRuiz\n - Julián David Martinez @JulianMart2706\n - Simón Steban Posada @Sayposada")

    def mostrarInfoInicio(self):
        self.labelInformativo.pack(expand=True, fill = "both")

    def ReiniciarFrameDeInteraccion(self):
        self.limpiarFrame(self.frameDeInteraccion)
        self.crearFrames()
        self.labelInformativo = tk.Label(self.frameDeInteraccion, wraplength=900, text="-Para empezar, acceda al menú superior a la opcion, 'Procesos y Consultas'.\n\nEncontrará tres opciones:\n\nPrimera opción: 'Administrar inventario', con esta podrá verificar que productos están vencidos y cuales proximos a vencer, eliminar de su inventario los productos vencidos y además hacer descuento sobre los que están proximos a vencer en el lapso de dias establecio en la busqueda.\n\nSegunda opción: 'Generar Orden', con esta función realizará las ordenes de venta, podrá crear clientes, eligiendo que tipo de producto se va a agregar a la orden, con la posibilidad de agregarlos uno a uno.\n\nTercera opción: Intercambio de productos, por medio de esta función, podra darle mejor manejo al inventario en su bodega, trasladando los productos que seleccione de un supermercado a otro.", font=("Arial"))

    def limpiarFrame(self, frame): # Recorremos todos los widgets dentro del frame y los destruimos
        for widget in frame.winfo_children():
            widget.destroy()





'''Menú superior (Zona 1 de la interfaz) Su estructura ser ́a la siguiente:
    • Archivo
        - Aplicacion: Se despliega una ventana de dialogo con la informaci ́on b ́asica de lo que hace la aplicaci ́on.
        - Salir: retorna a la Ventana de Inicio del programa.
    • Procesos y Consultas
        - Listar ́a todos los procesos y consultas que permite la aplicaci ́on (incluida las 5 funcionalidades solicitadas) acorde a la primera práctica.
    • Ayuda
        - Acerca de: muestra una ventana de di ́alogo con los nombres de los autores de la aplicaci ́on. Formato libre.
'''        
