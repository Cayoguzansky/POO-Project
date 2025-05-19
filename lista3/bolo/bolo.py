class Bolo():
  def __init__(self, cliente: str, data: str):
    self.cliente = cliente
    self.data = data

  def valor(self, peso: float, cobertura: str):  
    if cobertura == "chocolate":
      preco = peso * 10
    else:
      preco = peso * 15

    print(f"O preço do bolo para o cliente {self.cliente} é de R$ {preco}")
