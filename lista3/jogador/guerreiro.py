from jogadores import Jogadores
import random

class Guerreiro(Jogadores):
  def __init__(self, nome: str):
    super().__init__(nome)
    self.modo_ataque = "Atacando com a espada"
    self.xp = 1000

  def chamar_apoio(self):
    print("Chamando apoio de outros guerreiros")

  def ataque_especial(self):
    self.ataque_value = random.randint(1, 100)
    print(f"Guerreiro atacando com um valor de {self.ataque_value}")