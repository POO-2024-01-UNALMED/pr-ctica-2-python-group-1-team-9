from .Persona import Persona

class Empleado(Persona):
    _actual_id = 0
    empleados = []

    def __init__(self, nombre, cedula, supermercado, cargo, salario):
        super().__init__(nombre, cedula, cargo)
        self._salario = salario
        self._supermercado = supermercado
        self._activo = True
        Empleado._actual_id += 1
        self._id = Empleado._actual_id
        supermercado.agregar_empleado(self)
        Empleado.empleados.append(self)

    def informacion(self):
        return f"{self.get_cargo()} {self.get_nombre()} con cédula {self.get_cedula()}"
    

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_activo(self):
        return self._activo

    def set_activo(self, activo):
        self._activo = activo

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def get_supermercado(self):
        return self._supermercado

    def set_supermercado(self, supermercado):
        self._supermercado = supermercado

    def __str__(self):
        return f"Empleado con nombre {self.nombre}, cédula {self.cedula} y cargo {self.cargo}"