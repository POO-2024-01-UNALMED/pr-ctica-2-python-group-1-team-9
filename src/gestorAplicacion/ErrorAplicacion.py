import re
import tkinter as tk
from tkinter import ttk, messagebox

class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje) 
        self.mensaje = f"\n--Manejo de errores de la Aplicación--\n{mensaje}"
    def __str__(self):
        return self.mensaje 
    


class ExceptionC1(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(f"Error de categoria 1: {mensaje}\n")

class ExceptionC2(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(f"Error de categoria 2: {mensaje}\n")






class ExceptionInventada1(ExceptionC1):
    def __init__(self):
        super().__init__("El ingreso excede los caracteres permitidos, intente otra vez")

class ExceptionInventada2(ExceptionC1):
    def __init__(self):
        super().__init__("EI2C1")

class ExceptionSugerida1(ExceptionC1):
    def __init__(self):
        super().__init__("Ingreso invalido, intente otra vez.")






class ExceptionInventada3(ExceptionC2):
    def __init__(self):
        super().__init__("EI1C2")

class ExceptionInventada4(ExceptionC2):
    def __init__(self):
        super().__init__("EI2C2")
class ExceptionSugerida2(ExceptionC2):
    def __init__(self):
        super().__init__("Por favor rellene todos los campos.")