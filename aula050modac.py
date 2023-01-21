class Segredo:
    def __init__(self):
        self.__segredo = 'senha123'
    
    def __printa_segredo(self):
        print(self.__segredo)

    def printa_segredo(self):
        self.__printa_segredo()


seg = Segredo()
seg.printa_segredo()




print('-'*30)

class Base:
    def __base__privada(self):
        print('Pertenço somente a base')
    def _baseprotegida(self):
      print('pertenço a base e a quem me herdar')

class filha(Base):
    def acessa_protegida(self):
        self._baseprotegida()

filha = filha()
filha.acessa_protegida()
filha._baseprotegida()

print('-'*30)
#acessar veiculo

class Veiculo:
    def __init__(self):
        self.__marcha = 1
    def aumenta_marcha(self):
        self.__marcha += 1
        self.__marcha = min(self.__marcha, 5)

    def diminui_marcha(self):
        self.__marcha -= 1
        self.__marcha = max(self.__marcha, 1)
    def marcha_atual(self):
        return self.__marcha

carro = Veiculo()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
carro.aumenta_marcha()
print(carro.marcha_atual())

carro.diminui_marcha()
carro.diminui_marcha()
carro.diminui_marcha()
carro.diminui_marcha()
carro.diminui_marcha()
print(carro.marcha_atual())
    
