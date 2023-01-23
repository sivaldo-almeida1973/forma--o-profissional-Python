#criear uma classe com uma função que diga se um objeto
#é primitivo do Python , informando que é sempre passado 
#valor Ex: [int, float, str, bool], ou se é um objeto passado
#por referencia.

def testa_objeto(obj):
    if isinstance(obj,(int, float, str, bool)):
      print('Objeto por valor')
    else:
        print('Objeto por referencia')


class Objeto:
    def __init__(self):
        pass

obj = Objeto()
valor = 3

testa_objeto(obj)
testa_objeto(valor)