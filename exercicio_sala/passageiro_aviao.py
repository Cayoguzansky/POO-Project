from abc import ABC, abstractmethod
import random

class PassageiroAviao(ABC):
    @abstractmethod
    def fazer_check_in():
        pass

    @abstractmethod
    def passar_pela_seguranca():
        pass

    @abstractmethod
    def embarcar():
        pass

    def cadastro(self):
                
      

        while True:
            try:

                while True:
                    self.nome = input("Digite seu nome:")
                    if self.nome.strip().isalpha():
                        break
                    else:
                        print("Não é permitido caracteres especiais! Tente novamente...")

                self.poltrona = int(input("Digite sua poltrona:"))

                #self.poltrona = random.randint(1, 22)
                if self.poltrona > 0 and self.poltrona < 22: 
                    return self.nome, self.poltrona
                    break
                else:
                    print("Poltrona indisponivel! selecione outra...")
            except ValueError:
                print("Error: valor inválido! Tente novamente...")
