from metodopagamento import MetodoPagamento
from datetime import datetime


class TransferenciaBancaria(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor:.2f} processado por Transferência Bancária.")
        self.salvar_pagamento(valor)

    def salvar_pagamento(self, valor):
        with open("pagamentos.txt", "a") as f:
            f.write(f"{datetime.now()},Transferência Bancária,{valor:.2f}\n")