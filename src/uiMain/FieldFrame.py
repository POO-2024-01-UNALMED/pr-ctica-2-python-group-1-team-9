from tkinter import Frame,Label,Entry
from .VentanaInicio import VentanaInicio
import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.ErrorAplicacion import *

class FieldFrame(Frame):

    def getValue(self, criterio):
        return self.diccionario[criterio]

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(root)
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado

        self.diccionario = {}
        self.entradas = []
        tituloCriterios = Label(self, text=tituloCriterios, font=("Arial"))
        tituloCriterios.grid(row=0, column=0, padx=5, pady=5)
        tituloValores = Label(self, text=tituloValores, font=("Arial"))
        tituloValores.grid(row=0, column=1, padx=5, pady=5)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)

        def aceptar():
            falta = False
            for entrada in self.entradas:
                if entrada.get() is None or entrada.get() == "":
                    falta = True
                    break
            if falta:
               messagebox.showwarning("Advertencia",ExceptionSugerida2()) #Esto tiene que ser con una excepcion!!!!!!!!
            return not falta 

        def borrar():
            for entrada in self.entradas:
                entrada.delete(0, tk.END)
            
        self.botonAceptar = tk.Button(self, text="Aceptar", font=("Arial"), command=aceptar)
        self.botonAceptar.grid(row=(len(criterios)+1), column=1, padx=5, pady=5)

        self.bontonBorrar = tk.Button(self, text="Borrar", font=("Arial"), command=borrar)
        self.bontonBorrar.grid(row=(len(criterios)+1), column=0, padx=5, pady=5)

        for i, criterio in enumerate(criterios):
            etiqueta = Label(self, text=criterio, font=("Arial"))
            if self.valores is not None:
                valorinicial = tk.StringVar(value=valores[i])
                entrada = Entry(self, font=("Arial"), textvariable=valorinicial, border=2)
                if (self.habilitado[i] is not None) and (self.habilitado[i] != ""):
                    entrada.config(state="disabled")
            else:
                entrada = Entry(self, font=("Arial"))
            
            self.entradas.append(entrada)

            # Colocamos la etiqueta y el cuadro de texto en la cuadrícula
            etiqueta.grid(row=i+1, column=0, padx=5, pady=5, sticky="e")
            entrada.grid(row=i+1, column=1, padx=5, pady=5, sticky="w")
            
            # Guardamos las entradas en el diccionario
            self.diccionario[criterio] = entrada