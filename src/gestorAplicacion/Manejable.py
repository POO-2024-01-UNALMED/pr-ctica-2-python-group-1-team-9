from abc import ABC, abstractmethod

class Manejable(ABC):
    
    @abstractmethod
    def agregar_producto(self, unidad):
        pass
    
    @abstractmethod
    def quitar_producto(self, unidad):
        pass