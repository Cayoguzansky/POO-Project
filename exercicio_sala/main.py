from passageiroeconomica import PassageiroEconomica
from passageiroexecutiva import PassageiroExecutiva

def main():
    #passageiro eco
    passageiro1 = PassageiroEconomica()

    #passageiro exe 
    passageiro2 = PassageiroExecutiva()

    #teste do processo economica
    passageiro1.fazer_check_in()
    passageiro1.passar_pela_seguranca()
    passageiro1.embarcar()

    #teste de processo executiva
    passageiro2.fazer_check_in()
    passageiro2.passar_pela_seguranca()
    passageiro2.embarcar()
    
if __name__ == "__main__":
    main()