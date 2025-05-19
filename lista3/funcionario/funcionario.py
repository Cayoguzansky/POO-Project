class Funcionario():
  def __init__(self, nome: str, cpf: str, salario: float):
    if not isinstance(nome, str) or nome.strip() == "":
      raise ValueError("Nome deve ser uma string valída")
    if any(char.isalpha() for char in cpf) or cpf.strip() == "":
      raise ValueError("CPF deve conter apenas números")
    if not isinstance(salario, (int, float)) or salario <= 0: 
      raise ValueError("Salário deve ser um número positivo válido")
      
    self.nome = nome
    self.cpf = cpf
    self.salario = salario

  def calc_pagamentos(self, horas: float):
    valor =  horas * self.salario
    print(f"O funcionário {self.nome} inscrito no CPF: {self.cpf}, recebera o valor de R$ {valor}")