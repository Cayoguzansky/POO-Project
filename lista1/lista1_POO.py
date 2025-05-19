## Crie um exemplo de uma classe hipotética, crie os atributos dessa classe, os métodos dessa classe e pelo menos dois objetos preenchendo os atributos (apenas teórico).
#
#class Padaria():
#    def __init__(self, nome, vendas):
#        self.nome = nome 
#        self.vendas = vendas
#        self.temPao = bool
#
#    def verificaTemPao (self):
#        if self.temPao == True:
#            print("Há pão disponível!")
#        else:
#            print("Precisa fabricar mais pão!")
#
#    def bateuMeta (self, meta: int):
#        if self.vendas > meta:
#            print("bateu a meta!")
#        else:
#            print("A meta não foi atingida!")
#
#padaria1 = Padaria("São jose", 1200)
##init_teste
#print(padaria1.nome)
#padaria1.temPao = True
#padaria1.verificaTemPao()
#padaria1.bateuMeta(600)
##end_teste
#
#padaria2 = Padaria("Panicéu", 500)
##init_teste
#print(padaria2.nome)
#padaria2.temPao = False
#padaria2.verificaTemPao()
#padaria2.bateuMeta(1000)
##end_teste
#
#class Bolo():
#
#    def __init__ (self, nome: str, recheio: str, massa: str, cobertura: bool):
#        self.nome = nome
#        self.recheio = recheio
#        self.massa = massa
#        self.cobertura = cobertura
#
#    def temCobertura (self):
#        if self.cobertura == True:
#            print(self.nome, "Tem cobertura!")
#        else:
#            print(self.nome, "Não tem cobertura!")
#
#
#bolo1 = Bolo("Prestigio", "Brigadeiro Branco", "Chocolate", True)
#bolo2 = Bolo("Abacaxi Cake", "Creme de Abacaxi", "Baunilha", False)
#bolo3 = Bolo(bolo1.nome, bolo1.recheio, bolo1.massa, False)
#
#print("Teste 1")
#bolo1.temCobertura()
#bolo2.temCobertura()
#bolo3.temCobertura()
#
#bolo1.cobertura = False
#
#print("Teste 2")
#bolo1.temCobertura()
#bolo2.temCobertura()
#bolo3.temCobertura()

class FazBolo ():
    def __init__(self, massa:str, recheio:str, cobertura:bool, temperatura:str):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura
        self.tempoNoForno = 0
        self.temperatura = temperatura

    def assar(self, tempoNoForno, temperatura):
        self.tempoNoForno = tempoNoForno
        self.temperatura = temperatura

        if self.tempoNoForno > 180 and self.tempoNoForno < 0:
            print("Tempo fora do escopo permitido!")
            return
        elif self.temperatura not in ["baixo", "médio", "alto"]:
            print(self.temperatura, "Temperatura inválida!")
            return

        print("Você está querendo assar o bolo no fogo {} por {} minutos".format(self.temperatura, self.tempoNoForno))
        
        # Para o fogo alto, o bolo assa em 10 minutos. Antes fica cru e depois ele queima.
        # Para o fogo médio, o bolo assa em 30 minutos. Antes fica cru e depois ele queima.
        # Para o fogo baixo, o bolo assa em 45 minutos. Antes fica cru e depois ele queima.
        pontos_ideais = {
            "alto": 10,
            "médio": 30,
            "baixo": 45
        }

        ideal = pontos_ideais[self.temperatura]

        if self.tempoNoForno < ideal:
            print("Ponto: cru!")
        elif self.tempoNoForno > ideal:
            print("Ponto: Queimado!")
        else:
            print("Ponto: Ideal!")

print("teste1")
bolo1 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo1.assar(0, "alto")
bolo1 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo1.assar(10, "alto")
bolo1 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo1.assar(11, "alto")

print("teste2")
bolo2 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo2.assar(10, "médio")
bolo2 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo2.assar(30, "médio")
bolo2 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo2.assar(31, "médio")

print("teste3")
bolo3 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo3.assar(30, "baixo")
bolo3 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo3.assar(45, "baixo")
bolo3 = FazBolo("chocolate", "brigadeiro", False, "baixo")
bolo3.assar(46, "baixo")