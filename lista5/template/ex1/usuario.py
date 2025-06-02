from abc import ABC, abstractmethod

class Usuario(ABC):

    @abstractmethod
    def cadastrar(self, banco_dados):
        pass