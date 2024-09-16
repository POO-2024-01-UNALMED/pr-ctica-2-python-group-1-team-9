barraDeSeparacion = "______________________________________________________________________________________________________"

class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje) 
        self.mensaje = f"{barraDeSeparacion}\n--Manejo de errores de la Aplicación--\n{mensaje}"
    def __str__(self):
        return self.mensaje 
    


class ExceptionC1(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__(f"Error tipo C1: {mensaje}\n{barraDeSeparacion}")

class ExceptionC2(ErrorAplicacion):
        def __init__(self, mensaje):
            super().__init__(f"Error tipo C2: {mensaje}")






class ExceptionInventada1(ExceptionC1):
    def __init__(self):
        super().__init__("Ingreso invalido, pruebe otra vez")

class ExceptionInventada2(ExceptionC1):
    def __init__(self, mensaje="Error inventado 2"):
        super().__init__(f"{super().__str__()}: {mensaje}")

class ExceptionSugerida1(ExceptionC1):
    def __init__(self, mensaje="Excepción sugerida 1"):
        super().__init__(f"{super().__str__()}: {mensaje}")






class ExceptionInventada3(ExceptionC2):
    def __init__(self, mensaje="Error: Fallo en la seleccion"):
        super().__init__(f"{super().__str__()}: {mensaje}")

class ExceptionInventada4(ExceptionC2):
    def __init__(self, mensaje="Error inventado 4"):
        super().__init__(f"{super().__str__()}: {mensaje}")

class ExceptionSugerida2(ExceptionC2):
    def __init__(self, mensaje="Excepción sugerida 2"):
        super().__init__(f"{super().__str__()}: {mensaje}")