from pianista import Pianista
from percussionista import Percussionista

#instanciando
musico1 = Pianista("João")
musico2 = Percussionista("Maria")
musico3 = Pianista("Pedro")
musico4 = Percussionista("Ana")

#Teste1
print("\nTeste 1:")

musico1.tocar_instrumento(musico1.tocar())
musico2.tocar_instrumento(musico2.tocar())
musico3.tocar_instrumento(musico3.tocar())
musico4.tocar_instrumento(musico4.tocar())

#instanciando2
#musico1 = Pianista(123)
#musico2 = Percussionista(True)
#musico3 = Pianista()
musico4 = Percussionista("  ")

#Teste2
print("\nTeste 2:")

#musico1.tocar_instrumento(musico1.tocar())
#musico2.tocar_instrumento(musico2.tocar())
#musico3.tocar_instrumento(musico3.tocar())
musico4.tocar_instrumento(musico4.tocar())