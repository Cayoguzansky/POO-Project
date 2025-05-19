from hotel import Hotel
from cliente import Cliente

cliente1 = Cliente("Antônio", 3, 6)
hotel1 = Hotel("Copacabana Palace")

print ("O cliente {} que ficou {} dias no hotel {} teve a conta de {} reais, considerando {} dias de hospedagem e {} refeições.".format(cliente1.nome, cliente1.dias_estadia, hotel1.nome_hotel, Hotel.determineContaCliente(cliente1), cliente1.dias_estadia, cliente1.consumo_restaurante))