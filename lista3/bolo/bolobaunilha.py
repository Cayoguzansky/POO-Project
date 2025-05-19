from bolo import Bolo

class BoloBaunilha(Bolo):
  def def_peso(self):
    peso = input("Digite o peso do bolo: ")
    return float(peso)

  def def_cobertura(self):
    return "baunilha"