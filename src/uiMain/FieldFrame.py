from tkinter import Frame,Label,Entry
from VentanaInicio import VentanaInicio

class FieldFrame(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(VentanaInicio.segundaVentana)
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilidato = habilitado

        self.diccionario = {}

        for i, criterio in criterios():
            etiqueta = Label(self, text=criterio)
            entrada = Entry(self)
            
            # Colocamos la etiqueta y el cuadro de texto en la cuadrícula
            etiqueta.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            entrada.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            
            # Guardamos las entradas en el diccionario
            self.diccionario[criterio] = entrada

    
    def getValue(self, criterio):
        return self.valores[criterio]
        
"""crea un nuevo objeto de tipo FieldFrame
@arg tituloCriterios titulo para la columna "Criterio"
@arg criterios array con los nombres de los criterios
@arg tituloValores titulo para la columna "valor"
@arg valores array con los valores iniciales; Si ‘None’, no hay valores iniciales
@arg habilitado array con los campos no-editables por el usuario; Si ‘None’, todos son editables
*/
def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado):
...
/**
@arg criterio el criterio cuyo valor se quiere obtener
@return el valor del criterio cuyo nombre es ’criterio’
*/
def getValue(self, criterio):
..."""