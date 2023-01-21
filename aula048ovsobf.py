#Overrides: sobreposição de funções.

class classePai:
    def __init__(self):
        print('sou a classe pai')

class classefilho1(classePai):
    def __init__(self):
        print('sou a classe filha 1')

class classefilho2(classePai):
    def __init__(self):
        print('sou a classe filha 2')


pai = classePai()
filha1 = classefilho1()
filha2 = classefilho2()

        
print('-'*30)

class formaGeometrica:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura


class quadrado(formaGeometrica):
    def __init__(self, altura, largura, atributo_quadrado):
        formaGeometrica.__init__(self, altura,largura)
        self.atributo_quadrado = atributo_quadrado


class triangulo(formaGeometrica):
    def __init__(self, altura, largura, atributo_triangulo):
        formaGeometrica.__init__(self, altura,largura)
        self.atributo_triangulo = atributo_triangulo

quadrado = quadrado(1000,200,'quadrado' )
triangulo = triangulo(1000,200,'triangulo' )

print(quadrado.altura)
print(quadrado.atributo_quadrado)


print(triangulo.altura)
print(triangulo.atributo_triangulo)

