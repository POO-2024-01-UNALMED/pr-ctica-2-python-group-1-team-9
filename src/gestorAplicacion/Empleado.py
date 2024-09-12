from gestorAplicacion.Persona import Persona

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
        supermercado.agregarEmpleado(self)
        Empleado.empleados.append(self)

    def informacion(self):
        return f"{self.getCargo()} {self.getNombre()} con cédula {self.getCedula()}"
    

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getActivo(self):
        return self._activo

    def setActivo(self, activo):
        self._activo = activo

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario

    def getSupermercado(self):
        return self._supermercado

    def setSupermercado(self, supermercado):
        self._supermercado = supermercado

    def __str__(self):
        return f"Empleado con nombre {self.nombre}, cédula {self.cedula} y cargo {self.cargo}"