import bolobaunilha
import bolochocolate

#instanciando
bolo1 = bolochocolate.BoloChocolate("João", "10/10/2023")
bolo2 = bolobaunilha.BoloBaunilha("Maria", "10/10/2023")

#precificando
bolo1.valor(bolo1.def_peso(), bolo1.def_cobertura())
bolo2.valor(bolo2.def_peso(), bolo2.def_cobertura())