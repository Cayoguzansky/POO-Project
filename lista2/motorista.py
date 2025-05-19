import carro

class Motorista():
    def __init__(self, nome:str):
        self.nome = nome

    def dirigir(self, carro:carro.Carro, velocidade:int):
        
        usuario = input("Deseja ligar o carro? (s/n): ").strip().lower()

        if usuario == 's':
            carro.ligado = True
            print("{} seu carro ({} {}) está ligado!\n".format(self.nome, carro.modelo, carro.cor))

            carro.acelerar(velocidade)

            while carro.ligado == True:

                while True:
                    entrada = input("velocidade desejada: ")
                    try:
                        numero = int(entrada)
                        carro.acelerar(numero)
                        break  # Sai do loop se der certo
                    except ValueError:
                        print("Valor inválido. Tente novamente.")
                
                usuario = input("Deseja deligar o carro? (s/n): ").strip().lower()

                while True:
                    if usuario == 's':
                        carro.ligado = False
                        print("Carro desligado!")
                        break
                    elif usuario == 'n':
                        carro.ligado = True
                        break
                    else:
                        print("Resposta inválida! Digite apenas 's' para sim ou 'n' para não.")
        elif usuario == 'n':
            carro.ligado == False
            print("Carro desligado!")
        else:
            print("Resposta inválida, carro permanece desligado.")