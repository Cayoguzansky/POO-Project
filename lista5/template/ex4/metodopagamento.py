from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

    @abstractmethod
    def salvar_pagamento(self, valor):
        pass