from carro import Carro 
from motorista import Motorista

#Carros
carro1 = Carro("Montana", "Prata")
carro2 = Carro("Civic", "Azul")

#Motoristas
Motorista1 = Motorista("Carlos")
Motorista2 = Motorista("André")

#chamando metódos

print("\nteste1")
Motorista1.dirigir(carro1, 80)
print("\nteste2")
Motorista2.dirigir(carro2, 120)
print("\nteste3")
Motorista1.dirigir(carro2, 110)
print("\nteste4")
Motorista2.dirigir(carro1, 50)