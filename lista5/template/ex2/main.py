from extratortxt import ExtratorTXT

def main_ex2():
    extrator = ExtratorTXT("/home/cayo/Python study/POO/lista5/ex1/banco_usuarios.txt")
    extrator.extrair_dados()

if __name__ == "__main__":
    print("\nExecutando Exercício 2")
    main_ex2()