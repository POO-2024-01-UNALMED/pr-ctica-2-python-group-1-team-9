import os
import tkinter as tk
from PIL import Image, ImageTk

class VentanaInicio:
    def __init__(self, root):
        # Configuración basica de la ventana
        self.root = root
        self.root.title("Ventana de Inicio")
        self.root.geometry("500x500")
        self.root.grid_propagate(False)

        