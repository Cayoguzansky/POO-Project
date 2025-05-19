from jogadores import Jogadores

class Mago(Jogadores):
  def __init__(self, nome):
    super().__init__(nome)
    self.modo_ataque = "lançando bola de fogo"
    self.xp = 2000

  def fortificar_membros(self, xp: int):
    if xp >= 2000:
      print("Fortificando membros")
      return True
    else:
      print("XP insuficiente para fortalecer membros")
      return False

  def zona_cura(self):
    print("Criando zona de cura")
  