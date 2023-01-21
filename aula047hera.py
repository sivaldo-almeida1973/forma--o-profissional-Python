class formaGeometrica:
    def __init__(self, altura,largura):
        self.altura = altura
        self.largura = largura

class quadrado(formaGeometrica):
    pass

class triangulo(formaGeometrica):
    pass

quadrado = quadrado(100, 50)
triangulo = triangulo(10,30)

print(quadrado.altura)
print(triangulo.largura)

print('-'*30)
class formaGeometrica:
    def __init__(self, altura,largura):
        self.altura = altura
        self.largura = largura

class quadrado(formaGeometrica):
    lado = 10

class triangulo(formaGeometrica):
    angulo = 30

quadrado = quadrado(100, 50)
triangulo = triangulo(10,30)

print(quadrado.altura)
print(quadrado.largura)
print(quadrado.lado)


print(triangulo.angulo)


print('-'*30)
class formaGeometrica:
    def __init__(self, altura,largura):
        self.altura = altura
        self.largura = largura
    def funcao_herdada(self):
        print('sou herdado')

class quadrado(formaGeometrica):
    pass

class triangulo(formaGeometrica):
    pass

quadrado = quadrado(100, 50)
triangulo = triangulo(10,30)

print(quadrado.altura)
print(triangulo.largura)

quadrado.funcao_herdada()
triangulo.funcao_herdada()


