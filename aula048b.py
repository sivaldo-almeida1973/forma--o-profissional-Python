class formaGeometrica:
    def __init__(self, altura, largura):
        self.altura =altura
        self.largura = largura
    def calcula_area(self):
        pass

class quadrado(formaGeometrica):
    def calcula_area(self):
        return self.altura * self.largura


class triangulo(formaGeometrica):
    def calcula_area(self):
        return (self.altura * self.largura)/2

quadrado = quadrado(200,200)
triangulo = triangulo(200,200)

print(quadrado.calcula_area())
print(triangulo.calcula_area())
    

print('-'*30)

class veiculo:
    def __init__(self , marcha):
        self.marcha = marcha
    def aumenta_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha, 5) 
    def diminui_marcha(self):
        self.marcha -= 1
        self.marcha = min(self.marcha, 1)

class palio(veiculo):
    def __init__(self, marcha):
        veiculo.__init__(self,marcha)


class ecoSport(veiculo):
    def __init__(self, marcha):
        veiculo.__init__(self,marcha)
    def aumenta_marcha(self):
        self.marcha += 1
        self.marcha = min(self.marcha, 6) 

carro = palio(5)
carro.aumenta_marcha()
print(carro.marcha)

carro = ecoSport(3)
carro.aumenta_marcha()
print(carro.marcha)