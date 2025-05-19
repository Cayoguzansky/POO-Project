class Carro():
    def __init__(self, modelo:str, cor:str):
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        self.velocidade = 0

    def ligar (self):
        self.ligado = True

    def desligar (self):
        self.ligado = False

    def acelerar (self, velocidade: int):
        if velocidade < self.velocidade:
            while self.velocidade > velocidade:
                self.velocidade -= 1
        else:
            while self.velocidade < velocidade:
                self.velocidade += 1

        print ("Velocidade atual: ", self.velocidade)
        