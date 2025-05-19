from musico import Musico

class Pianista(Musico):
  def tocar(self):
    quando_tocar = f"{self.nome}: Estou tocando a nona sinfonia"
    return quando_tocar