from bolo import Bolo

class BoloChocolate(Bolo):
  def def_peso(self):
    peso = input("Digite o peso do bolo: ")
    return float(peso)

  def def_cobertura(self):
    return "chocolate"
    