from passageiro_aviao import PassageiroAviao

class PassageiroEconomica(PassageiroAviao):
    def __init__(self, ):
        self.nome,  self.numero_poltrona = super().cadastro()

    def fazer_check_in(self):
        print("\nClasse ECONOMICA:")
        print (f"\nSeja bem-vind@ {self.nome}, direcione-se para área 2 (Economica) de embarque")

    def passar_pela_seguranca(self):
        print ("Passageiro da ECONOMICA liberado pela segurança para o embarque!")

    def embarcar(self):
        print (f"Passageiro da ECONOMICA, direcione-se para a poltrona {self.numero_poltrona}")
        