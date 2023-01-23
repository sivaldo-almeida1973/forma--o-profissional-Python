#crie uma classe base que represente um veiculo.
#os atributos devem ser peso do veiculo, numero de rodas
#e potencia,Em seguida crie tres classes que herdam esse #veiculo: onoibus, carro e moto.Crie uma instancia de cada
#e imprima.

class Veiculo:
    def __init__(self,peso,potencia,rodas ):
        self.peso = peso
        self.potencia = potencia
        self.rodas = rodas

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
onibus = Onibus(5000,100,8)
carro = Carro(2000,200,4)

print('Moto: Peso:',moto.peso,'Potencia:',moto.potencia,'Rodas:',moto.rodas )
print('Onibus:Peso',onibus.peso,'Potencia',onibus.potencia,'Rodas',onibus.rodas )
print('Carro:Peso:',carro.peso,'Potencia',carro.potencia,'Rodas:',carro.rodas )


    