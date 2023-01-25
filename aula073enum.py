#Enumerate
#nesse acessa o indice e valor em uma tupla juntos
lista = ['a','b','c']

for item in enumerate(lista):#produz uma tupla
  print(item)


#acessa separadamente o indice e o valor
lista = ['a','b','c']

for indice, valor in enumerate(lista):#produz uma
  print(indice, valor)




def anos():
    yield '2000'
    yield '2001'
    yield '2002'
    yield '2003'
    yield '2004'
    yield '2005'

for indice , valor in enumerate(anos()):
  print(indice, valor)



for valor in range(0,20,5):
  print( valor)


for valor, indice in enumerate(range(0,20,5)):
  print( valor, indice)

