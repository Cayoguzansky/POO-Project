class Musico():
  def __init__(self, nome: str):
    if not isinstance(nome, str) or nome.strip() == "":
      raise ValueError("Nome deve ser uma string valída")
      
    self.nome = nome

  def tocar_instrumento (self, a: str):
    print(f"{a}")