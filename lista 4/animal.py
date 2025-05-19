from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, raca: str, nome: str):
        self.raca = raca
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass

