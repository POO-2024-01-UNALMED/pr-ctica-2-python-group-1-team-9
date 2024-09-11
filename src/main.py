from gestorAplicacion.VentanaPrincipal import VentanaPrincipal
from gestorAplicacion.ventanaInicio import VentanaInicio
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    ventana = VentanaPrincipal(root)
    root.mainloop()