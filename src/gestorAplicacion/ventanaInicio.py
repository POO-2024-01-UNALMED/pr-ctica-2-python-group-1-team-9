import os
import tkinter as tk
from PIL import Image, ImageTk

class VentanaInicio:
    def __init__(self, root, root2):
        # Configuración basica de la ventana
        self.root = root
        self.root2 = root2
        self.root.title("Plataforma Super Usable Para Supermercados (PSUPS)")
        self.root.geometry("500x500")
        self.crearMenu()
        self.root.protocol("WM_DELETE_WINDOW", self.regresarVentanaPrincipal) #Si se cierra la ventana se muestra la primera y se oculta la segunda.

    def crearMenu(self): # Función para crear el menú
        menuBar = tk.Menu(self.root)
        self.root.config(menu=menuBar)

        menuArchivo = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Archivo", menu=menuArchivo) 
        menuArchivo.add_command(label="Aplicación (sin implementar)")
        menuArchivo.add_command(label="Salir", command= self.regresarVentanaPrincipal)

        menuProcesosYConsultas = tk.Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesosYConsultas)
        menuProcesosYConsultas.add_command(label="Administar inventario (sin implementar)")
        menuProcesosYConsultas.add_command(label="Generar Orden (sin implementar)")
        menuProcesosYConsultas.add_command(label="Intercambio de Productos (sin implementar)")

        menuAyuda = tk.Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label="Ayuda", menu=menuAyuda)
        menuAyuda.add_command(label="Acerda de: (sin implementar)")

    def regresarVentanaPrincipal(self): # Oculta la segunda ventana ("Plataforma Super Usable Para Supermercados (PSUPS)") y muestra la primera ("Ventana principal de inicio")
        self.root2.root.deiconify()
        self.root.withdraw()


'''Menú superior (Zona 1 de la interfaz) Su estructura ser ́a la siguiente:
    • Archivo
        - Aplicacion: Se despliega una ventana de di ́alogo con la informaci ́on b ́asica de lo que hace la aplicaci ́on.
        - Salir: retorna a la Ventana de Inicio del programa.
    • Procesos y Consultas
        - Listar ́a todos los procesos y consultas que permite la aplicaci ́on (incluida las 5 funcionalidades solicitadas) acorde a la primera práctica.
    • Ayuda
        - Acerca de: muestra una ventana de di ́alogo con los nombres de los autores de la aplicaci ́on. Formato libre.
'''        
