class Teste:
    def __init__(self, gasolina):
        pass
    @classmethod
    def class_method(cls):
        print(cls)
    @staticmethod
    def static_method():
        print('static method')

Teste.class_method()
Teste.static_method()

testando = Teste('aditivada')
testando.class_method()



print('-'*30)

class Veiculo:
    def __init__(self,nome, gasolina, potencia):
        self.nome = nome
        self.gasolina = gasolina
        self.potencia = potencia
    @classmethod
    def cria_carro(cls):
        return cls('carro','comum',200)
    @classmethod
    def cria_trator(cls):
        return cls('trator','aditivada',500)

veicul1 = Veiculo.cria_carro()
veicul2 = Veiculo.cria_trator()

print(veicul1.nome)
print(veicul1.gasolina)
print(veicul1.potencia)
print(veicul2.nome)
    

print('-'*30)

class Veiculo:
    __numero_veiculos = 0#elemento estatico
    def __init__(self,nome, gasolina, potencia):
        self.nome = nome
        self.gasolina = gasolina
        self.potencia = potencia
        Veiculo.__numero_veiculos += 1
    @staticmethod
    def get_numero_carros():
       return Veiculo.__numero_veiculos

carro = Veiculo('carro','aditivada',200)
carro = Veiculo('caminhão','aditivada',1000)
print(Veiculo.get_numero_carros())
print(carro.get_numero_carros())
    