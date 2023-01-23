#Baseado no ex anterior, crie uma func na classe base
#que diga a distancia percorrida.Vamos supor que esse valor 
#é dado pelo peso do veiculo dividido pela potencia do veiculo vezes mil ,crie 1 moto ,1 carro e 1 onibus.Mostre os 
#valores

class Veiculo:
    def __init__(self,peso,potencia,rodas ):
        self.peso = peso
        self.potencia = potencia
        self.rodas = rodas
    def distancia_percorrida(self):
        return(self.potencia / self.peso)* 1000

class Moto(Veiculo):
    def __init__(self, peso, potencia, rodas):
      Veiculo.__init__(self,peso,potencia,rodas)

class Onibus(Veiculo):

    def __init__(self,peso,potencia,rodas):
     Veiculo.__init__(self,peso,potencia,rodas)

class Carro(Veiculo):
    def __init__(self,peso,potencia,rodas):
      Veiculo.__init__(self,peso,potencia,rodas)

moto = Moto(200,150,2)
onibus = Onibus(1000,400,8)
carro = Carro(2000,200,4)

print('Distancia Percorrida da moto:', moto.distancia_percorrida() )
print('Distancia Percorrida do onibus:',onibus 
.distancia_percorrida() )
print('Distancia Percorrida do carro:', carro.distancia_percorrida()  )
