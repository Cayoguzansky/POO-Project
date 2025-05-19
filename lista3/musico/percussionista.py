from musico import Musico

class Percussionista(Musico):
  def tocar (self):
    quando_tocar = f"{self.nome}: Tocando percussão sempre no ritmo sincronizado"
    return quando_tocar