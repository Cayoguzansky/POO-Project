from extratordados import ExtratorDados

class ExtratorTXT(ExtratorDados):
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def extrair_dados(self):
        try:
            with open(self.arquivo, 'r') as f:
                linhas = f.readlines()
                for linha in linhas:
                    partes = linha.strip().split(',')
                    print("Nome:", partes[0])
                    print("Email:", partes[1])
                    print("Tipo:", partes[2])
                    if len(partes) > 3:
                        print("Nível de Acesso:", partes[3])
                    print("-" * 20)
        except FileNotFoundError:
            print("Arquivo não encontrado.")