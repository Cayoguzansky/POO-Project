from passageiro_aviao import PassageiroAviao

class PassageiroExecutiva(PassageiroAviao):
    def __init__(self):
        self.nome,  self.numero_poltrona = super().cadastro()

    def fazer_check_in(self):
        print("\nClasse EXECUTIVA:")
        print (f"\nSeja bem-vind@ {self.nome}, direcione-se para área 2 (Executiva) de embarque")

    def passar_pela_seguranca(self):
        print ("Passageiro da EXECUTIVA liberado pela segurança para o embarque!")

    def embarcar(self):
        print (f"Passageiro da EXECUTIVA, direcione-se para a poltrona {self.numero_poltrona}")