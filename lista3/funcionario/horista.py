from funcionario import Funcionario

class Horista(Funcionario):
  def horas_trabalhadas(self, horas: int, min: int):
    return float(horas + min/60)