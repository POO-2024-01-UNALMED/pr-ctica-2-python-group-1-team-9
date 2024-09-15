from uiMain.VentanaInicio import VentanaInicio
from uiMain.VentanaPrincipal import VentanaPrincipal
from uiMain.FieldFrame import FieldFrame
import tkinter as tk

def primerFuncion():
    frame = tk.Frame(segundaventana, background="blue")
    frame.pack(expand=True, fill="both")

def MostrarVentanaPrincipal(primerventana):
    primerventana.withdraw()
    segundaventana.deiconify()

def crearMenu(): # Función para crear el menú
    menuBar = tk.Menu(segundaventana)
    segundaventana.config(menu=menuBar)

    menuArchivo = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Archivo", menu=menuArchivo) 
    menuArchivo.add_command(label="Aplicación", command= segundaventana.ventanaDeDialogoInfoBasica)
    menuArchivo.add_command(label="Salir", command= segundaventana.regresarVentanaInicio)

    menuProcesosYConsultas = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label="Procesos y Consultas", menu=menuProcesosYConsultas)
    menuProcesosYConsultas.add_command(label="Administar inventario (sin implementar)", command=primerFuncion)
    menuProcesosYConsultas.add_command(label="Generar Orden (sin implementar)")
    menuProcesosYConsultas.add_command(label="Intercambio de Productos (sin implementar)")

    menuAyuda = tk.Menu(menuBar,tearoff=0)
    menuBar.add_cascade(label="Ayuda", menu=menuAyuda)
    menuAyuda.add_command(label="Acerda de:", command=segundaventana.ventanaDeDialogoAcercaDe)
        
if __name__ == "__main__":


    primerventana = VentanaInicio()
    segundaventana = VentanaPrincipal(primerventana)
    segundaventana.withdraw()

    primerventana.botonP4.config(command=lambda: MostrarVentanaPrincipal(primerventana))

    crearMenu()

    #frameDePrueba = FieldFrame(tituloCriterios="",criterios=["Nombre", "Edad"],tituloValores= "", valores=None, habilitado=None)
    primerventana.mainloop()