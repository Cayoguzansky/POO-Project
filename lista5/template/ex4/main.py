from cartaocredito import CartaoCredito
from paypal import PayPal
from transferenciabancaria import TransferenciaBancaria

def main_ex4():
    pagamentos = [
        CartaoCredito(),
        PayPal(),
        TransferenciaBancaria()
    ]

    valores = [150.00, 230.50, 99.90]

    for metodo, valor in zip(pagamentos, valores):
        metodo.processar_pagamento(valor)

if __name__ == "__main__":
    print("\nExecutando Exercício 4")
    main_ex4()