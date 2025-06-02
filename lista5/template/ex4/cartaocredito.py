from metodopagamento import MetodoPagamento
from datetime import datetime

class CartaoCredito(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor:.2f} processado com Cartão de Crédito.")
        self.salvar_pagamento(valor)

    def salvar_pagamento(self, valor):
        with open("pagamentos.txt", "a") as f:
            f.write(f"{datetime.now()},Cartão de Crédito,{valor:.2f}\n")