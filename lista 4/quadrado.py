from formageometrica import FormaGeometrica

class Quadrado (FormaGeometrica):
    def __init__(self, tamanho_lado: int):
          super().__init__("QUADRADO")
          self.tamanho = tamanho_lado

    def calcular_area(self):
        value = self.tamanho ** 2
        print(f"Área do {self.tipo} = {value}")
        return value


    def calcular_perimetro(self):
        value = 4 * self.tamanho
        print(f"Perímetro do {self.tipo} = {value}")
        return value

        
    def le_lados (self):
        while True:
            try:
                self.tamanho = int(input("| => tamanho do lado:"))
                break
            except ValueError:
                print("Error: valor inválido! Tente novamente...")
        
    
    def mostra_lados(self):
        print(f"\n{self.tipo}:")
        print("Ambos os lados [ 2 x __ & 2 x | ] possuem:", self.tamanho)