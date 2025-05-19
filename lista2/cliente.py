class Cliente():
    def __init__(self, nome:str, dias_estadia:int, consumo_restaurante:int):
        self.nome = nome
        self.dias_estadia = dias_estadia
        self.consumo_restaurante = consumo_restaurante

    def fornecaValorConta(self):
        self.total_estadia = self.dias_estadia * 100
        self.total_restaurante = self.consumo_restaurante * 50
        return self.total_estadia + self.total_restaurante