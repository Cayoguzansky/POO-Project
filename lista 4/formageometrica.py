from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, tipo: str):
        self.tipo = tipo


    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def le_lados (self):
        pass

    def mostra_lados (self):
        pass