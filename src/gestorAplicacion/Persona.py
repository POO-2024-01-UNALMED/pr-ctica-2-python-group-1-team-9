from abc import ABC, abstractmethod

class Persona(ABC):
    personas = []

    def __init__(self, nombre, cedula, cargo="Cliente"):
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = cargo
        Persona.personas.append(self)

    @abstractmethod
    def informacion(self):
        pass

 
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_cedula(self):
        return self.cedula

    def set_cargo(self, cargo):
        self.cargo = cargo
    
    def get_cargo(self):
        return self.cargo
    
    @classmethod
    def get_personas():
        return Persona.get_personas

    @classmethod
    def get_personas(cls):
        return cls.personas

    @classmethod
    def set_personas(cls, personas):
        cls.personas = personas

    @classmethod
    def agregar_persona(cls, persona):
        cls.personas.append(persona)

    def __str__(self):
        return f"Persona con nombre {self.nombre} y cédula {self.cedula}"