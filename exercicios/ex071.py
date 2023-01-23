#baseado no ex anterior , crie os operadores '>'e'<' para
#dizer qual  veiculo é mais potente.Compare um de cada tipo.
#obs, sobrescreva os metodos __1t__ e __gt__.

class Veiculo:
    def __init__(self,peso,potencia,rodas ):
        self.peso = peso
        self.potencia = potencia
        self.rodas = rodas
    def __lt__(self,outro):
        return self.potencia < outro.potencia
    def __gt__(self, outro):
        return self.potencia > outro.potencia
    
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

print(onibus > carro)
print(onibus < moto)
print(moto > carro  )
