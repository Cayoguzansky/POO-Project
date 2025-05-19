class Jogadores():
  def __init__(self, nome: str):
    self.nome = nome 

  def atacar(self, modo_ataque):
    print(f"{self.nome}: {modo_ataque}")