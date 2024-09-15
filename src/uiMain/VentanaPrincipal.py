import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, primerventana):
        super().__init__(primerventana)
        # Configuración basica de la ventana
        self.primerventana = primerventana
        self.title("Plataforma Super Usable Para Supermercados (PSUPS)")
        self.geometry("500x500")
        self.protocol("WM_DELETE_WINDOW", self.regresarVentanaInicio) #Si se cierra la ventana se muestra la primera y se oculta la segunda.

    def regresarVentanaInicio(self): # Oculta la segunda ventana ("Plataforma Super Usable Para Supermercados (PSUPS)") y muestra la primera ("Ventana de inicio")
        self.primerventana.deiconify()
        self.withdraw()
    
    def ventanaDeDialogoInfoBasica(self):
        messagebox.showinfo("Aplicación", "Con esta aplicación podrá hacer ordenes de venta, administar inventarios y relizar movimientos de mercancia entre supermercados.")

    def ventanaDeDialogoAcercaDe(self):
        messagebox.showinfo("Acerca de:", "PSUPS fue desarrollado por:\n - Jose Manuel Areiza @areizaaz\n - Oscar Daniel Ruiz @OscarDanielRuiz\n - Julián David Martinez @JulianMart2706\n - Simón Steban Posada @Sayposada")






'''Menú superior (Zona 1 de la interfaz) Su estructura ser ́a la siguiente:
    • Archivo
        - Aplicacion: Se despliega una ventana de dialogo con la informaci ́on b ́asica de lo que hace la aplicaci ́on.
        - Salir: retorna a la Ventana de Inicio del programa.
    • Procesos y Consultas
        - Listar ́a todos los procesos y consultas que permite la aplicaci ́on (incluida las 5 funcionalidades solicitadas) acorde a la primera práctica.
    • Ayuda
        - Acerca de: muestra una ventana de di ́alogo con los nombres de los autores de la aplicaci ́on. Formato libre.
'''        
