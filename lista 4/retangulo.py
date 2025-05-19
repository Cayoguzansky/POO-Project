from formageometrica import FormaGeometrica

class Retangulo (FormaGeometrica):
    def __init__(self, base: int, altura: int):
          super().__init__("RETANGULO")
          self.base = base
          self.altura = altura

    def calcular_area(self):
        value = self.base * self.altura
        print(f"Área do {self.tipo} = {value}")
        return value


    def calcular_perimetro(self):
        value = 2*self.base + 2*self.altura
        print(f"Perímetro do {self.tipo} = {value}")
        return value

        
    def le_lados (self):
        while True:
            try:
                self.base = int(input("__ => valor da base:"))
                self.altura = int(input("| => valor da altura:"))
                break
            except ValueError:
                print("Error: valor inválido! Tente novamente...")

    def mostra_lados(self):
        print(f"\n{self.tipo}:")
        print("valor da base: __ =", self.base)
        print("valor da altura: | = ", self.altura)