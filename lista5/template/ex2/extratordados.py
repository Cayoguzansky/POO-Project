from abc import ABC, abstractmethod

class ExtratorDados(ABC):
    @abstractmethod
    def extrair_dados(self):
        pass