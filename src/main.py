#Este será el main
#voy a ver si si sirve lo de tk


import tkinter as tk 
from tkinter import ttk 

class Ventana_prueba(ttk.Frame):
  
  def __init__(self, ventana):
    super().__init__(ventana)
    #configuramos el  nombre y el tamaño de la ventana 
    ventana.title("Supermercado los programers")

    #creamos la configuración de la página
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight= 1)


    self.Label1 = tk.Label(self, text="INICIO", bg= "#FFA500")
    self.Label1.grid(row=0, column=0, sticky="nsew", columnspan=2)


    self.Label2 = tk.Label(self, text="INICIO", bg= "#FFA500")
    self.Label2.grid(row=1, column=0, sticky="nsew", columnspan=2)

    self.grid(sticky="n")
    self.rowconfigure(0, weight=3)

ventana = tk.Tk()
Practica = Ventana_prueba(ventana)
Practica.mainloop()
