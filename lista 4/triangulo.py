from formageometrica import FormaGeometrica

class Triangulo (FormaGeometrica):
    def __init__(self, base: int, lado_a: int, lado_b: int):
          super().__init__("TRIANGULO")
          self.base = base
          self.lado_a = lado_a
          self.lado_b = lado_b

    def calcular_area(self):
        if self.base == self.lado_a == self.lado_b:
            value = ((self.base**2)*(3**(1/3)))/4
            print(f"Área do {self.tipo} = {value}")
            return value
        else:
            #fórmula de Heron
            s = (self.base + self.lado_a + self.lado_b)/ 2
            value = (s*(s - self.base)*(s - self.lado_a)*(s - self.lado_b))**(1/2)
            print(f"Área do {self.tipo} = {value}")
            return value


    def calcular_perimetro(self):
        value = self.base + self.lado_a + self.lado_b
        print(f"Perímetro do {self.tipo} = {value}")
        return value
        
    def le_lados (self):
        while True:
            try:
                self.base = int(input("__ => valor da base:"))
                self.lado_a = int(input("A / => valor do lado A:"))
                self.lado_b = int(input("B \ => valor do lado B:"))
                break
            except ValueError:
                print("Error: valor inválido! Tente novamente...")
        

    def mostra_lados(self):
        print(f"\n{self.tipo}:")
        print("valor da base: __ =", self.base)
        print("valor do lado A / =", self.lado_a)
        print("valor do lado B \ =", self.lado_b)

    def verif_triang_retangulo(self):
        hipotenusa = (max(self.base, self.lado_a, self.lado_b)) ** 2

        achar_catetos = sorted([self.base, self.lado_a, self.lado_b])
        soma_catetos =  (achar_catetos[0] ** 2) + (achar_catetos[1] ** 2)

        if hipotenusa == soma_catetos:
            print(f"\nO triângulo é um triangulo retângulo")
            return True
        else:
            print(f"\nO triângulo não é um triângulo retângulo")
            return False