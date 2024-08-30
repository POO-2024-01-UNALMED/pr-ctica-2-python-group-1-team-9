import Persona

class Empleado(Persona):
    _actual_id = 0
    _empleados = []

    def __init__(self, nombre, cedula, supermercado, cargo, salario):
        super().__init__(nombre, cedula, cargo)
        self._salario = salario
        self._supermercado = supermercado
        self._activo = True
        Empleado._actual_id += 1
        self._id = Empleado._actual_id
        supermercado.agregar_empleado(self)
        Empleado._empleados.append(self)

    def informacion(self):
        return f"{self.cargo} {self.nombre} con cédula {self.cedula}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def supermercado(self):
        return self._supermercado

    @supermercado.setter
    def supermercado(self, supermercado):
        self._supermercado = supermercado

    def __str__(self):
        return f"Empleado con nombre {self.nombre}, cédula {self.cedula} y cargo {self.cargo}"