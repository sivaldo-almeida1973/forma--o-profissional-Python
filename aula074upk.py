#Unpacking de Iteredores
produtos = [
  ['carro', '200.000'],
  ['cadeira', '2.000'],
  ['moto', '20.000'],
  ['geladeira', '2.000'],
  ['armario', '1.500']
]
for produto , valor in produtos:
  print(produto, valor)

print('-'*30)
def produtos():
  yield ['carro', '200.000'  ]
  yield ['cadeira', '2.000']
  yield ['moto', '20.000']
  yield ['geladeira', '2.000']
  yield ['armario', '1.500']
for produto, valor in produtos():
    print(produto, valor)


print('-'*30)
def gen1():
    yield [1,2]
    yield[3,4]
    yield [5,6]

for x,  y in gen1():
    print(x,y)


print('-'*30)
#funções geradoras aninhadas



def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    for i in gen1():
      yield i, 'a'
      yield i, 'b'
      yield i ,'c'

for x, y in  gen2():
  print(x,y)