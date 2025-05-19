import guerreiro
import mago

#instanciando
jogador1 = guerreiro.Guerreiro("João")
jogador2 = mago.Mago("Maria")

#teste ataque
print("\nTeste ataque:")
jogador1.atacar(jogador1.modo_ataque)
jogador2.atacar(jogador2.modo_ataque)

#teste ataque especial
print("\nTeste ataque especial:")
jogador1.ataque_especial()
jogador2.zona_cura()

#teste chamar apoio e fortificar membros
print("\nTeste chamar apoio e fortificar membros:")
jogador1.chamar_apoio()
jogador2.fortificar_membros(jogador1.xp)