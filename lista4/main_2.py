from retangulo import Retangulo
from quadrado import Quadrado
from triangulo import Triangulo

def main():
    #instanciando
    figura1 = Retangulo(10, 5)
    figura2 = Quadrado(8)
    figura3 = Triangulo(8, 12, 9)

    #teste retangulo
    print("\n#teste retangulo: Base = 10, Altura = 5")
    figura1.calcular_area()
    figura1.calcular_perimetro()
    figura1.le_lados()
    figura1.mostra_lados()

    #teste quadrado
    print("\n#teste quadrado: Tamanho dos lados = 8")
    figura2.calcular_area()
    figura2.calcular_perimetro()
    figura2.le_lados()
    figura2.mostra_lados()

    #teste triangulo
    print("\n#teste triangulo: Base = 8, Lado A = 12, Lado B = 9cinco")
    figura3.calcular_area()
    figura3.calcular_perimetro()
    figura3.le_lados()
    figura3.mostra_lados()
    # verificando se triangulo é triangulo retangulo
    figura3.verif_triang_retangulo()

if __name__ == "__main__":
    main()