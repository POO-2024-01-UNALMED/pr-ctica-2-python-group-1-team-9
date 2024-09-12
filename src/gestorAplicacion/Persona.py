from abc import ABC, abstractmethod

class Persona(ABC):
    personas = []

    def __init__(self, nombre, cedula, cargo):
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo
        Persona.personas.append(self)

    @abstractmethod
    def informacion(self):
        pass

 
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setCedula(self, cedula):
        self.cedula = cedula

    def getCedula(self):
        return self.cedula

    def setCargo(self, cargo):
        self.cargo = cargo
    
    def getCargo(self):
        return self.cargo
    
    @classmethod
    def getPersonas():
        return Persona.getPersonas

    @classmethod
    def getPersonas(cls):
        return cls.personas

    @classmethod
    def setPersonas(cls, personas):
        cls.personas = personas

    @classmethod
    def agregarPersona(cls, persona):
        cls.personas.append(persona)

    def __str__(self):
        return f"Persona con nombre {self.nombre} y cédula {self.cedula}"