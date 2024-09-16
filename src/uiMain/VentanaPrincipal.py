import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, primerventana):
        super().__init__(primerventana)
        # Configuración basica de la ventana
        self.primerventana = primerventana
        self.title("Plataforma Super Usable Para Supermercados (PSUPS)")
        self.geometry("800x600")
        self.protocol("WM_DELETE_WINDOW", self.regresarVentanaInicio) #Si se cierra la ventana se muestra la primera y se oculta la segunda.

        self.config(background="black")

        self.frameDeInteraccion = tk.Frame(self, bg="gray90")
        self.frameDeInteraccion.pack(expand=True,fill="both",padx=10,pady=10)
        self.labelInformativo = tk.Label(self.frameDeInteraccion, bg= "gray50", text="Esta será la info que va al iniciar", font=("Arial"))
        self.labelInformativo.pack(expand=True, fill = "both")

        self.frameNombreProceso = tk.Frame(self.frameDeInteraccion, bg="black")
        self.labelNombreProceso = tk.Label(self.frameNombreProceso, text="Nombre del Proceso", font=("Arial"), bg="white")

        self.frameDescripcionProceso = tk.Frame(self.frameDeInteraccion, bg="black")
        self.labelDescripcionProceso = tk.Label(self.frameDescripcionProceso, text="Descripcion del Proceso" ,wraplength=760 ,font=("Arial"), bg="white")

        self.frameProceso = tk.Frame(self.frameDeInteraccion, bg="green")

        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        self.menuArchivo = tk.Menu(self.menuBar, tearoff=0)
        self.menuProcesosYConsultas = tk.Menu(self.menuBar,tearoff=0)
        self.menuAyuda = tk.Menu(self.menuBar,tearoff=0)
        
    #frame = FieldFrame(frameDeInteraccion,tituloCriterios = "",criterios = ["nombre","apellido"], tituloValores = "",valores = None, habilitado = None)

    

    def regresarVentanaInicio(self): # Oculta la segunda ventana ("Plataforma Super Usable Para Supermercados (PSUPS)") y muestra la primera ("Ventana de inicio")
        self.primerventana.deiconify()
        self.withdraw()
        self.frameNombreProceso.grid_forget()
        self.frameDescripcionProceso.grid_forget()
        self.frameProceso.grid_forget()
        self.labelInformativo.pack(expand=True, fill = "both")
    
    def ventanaDeDialogoInfoBasica(self):
        messagebox.showinfo("Aplicación", "Con esta aplicación podrá hacer ordenes de venta, administar inventarios y relizar movimientos de mercancia entre supermercados.")

    def ventanaDeDialogoAcercaDe(self):
        messagebox.showinfo("Acerca de:", "PSUPS fue desarrollado por:\n - Jose Manuel Areiza @areizaaz\n - Oscar Daniel Ruiz @OscarDanielRuiz\n - Julián David Martinez @JulianMart2706\n - Simón Steban Posada @Sayposada")

    def mostrarInfoInicio(self):
        self.labelInformativo.pack(expand=True, fill = "both")





'''Menú superior (Zona 1 de la interfaz) Su estructura ser ́a la siguiente:
    • Archivo
        - Aplicacion: Se despliega una ventana de dialogo con la informaci ́on b ́asica de lo que hace la aplicaci ́on.
        - Salir: retorna a la Ventana de Inicio del programa.
    • Procesos y Consultas
        - Listar ́a todos los procesos y consultas que permite la aplicaci ́on (incluida las 5 funcionalidades solicitadas) acorde a la primera práctica.
    • Ayuda
        - Acerca de: muestra una ventana de di ́alogo con los nombres de los autores de la aplicaci ́on. Formato libre.
'''        
