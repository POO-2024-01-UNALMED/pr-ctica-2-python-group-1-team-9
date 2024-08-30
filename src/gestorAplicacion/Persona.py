from abc import ABC, abstractmethod

class Persona(ABC):
    _personas = []

    def __init__(self, nombre, cedula, cargo="Cliente"):
        self._nombre = nombre
        self._cedula = cedula
        self._cargo = cargo
        Persona._personas.append(self)

    @abstractmethod
    def informacion(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @classmethod
    def get_personas(cls):
        return cls._personas

    @classmethod
    def set_personas(cls, personas):
        cls._personas = personas

    @classmethod
    def agregar_persona(cls, persona):
        cls._personas.append(persona)

    def __str__(self):
        return f"Persona con nombre {self.nombre} y cédula {self.cedula}"