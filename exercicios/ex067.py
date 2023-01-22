#crie uma classe para representar um carro
#que mostre sua potencia ecavalos
#outro atributo vai dizer quanto de #gasolina por km.
#crie 2 instancias e mostre os valores.
print('-'*30)
class Carro:
 def __init__(self, potencia , cavalos):
    self.potencia = potencia
    self.alcanse = cavalos

carro1 = Carro(100,200)
carro2 = Carro(200,350.5)

print('Potencia de carro 1:', carro1.potencia, 'cavalos')
print('Alcance  do carro 1:', carro1.alcanse, '  Km/1')

print('Potencia de carro 2:', carro2.potencia, 'cavalos')
print('Alcance  do carro 2:', carro2.alcanse, ' Km/1')

print('-'*30)
