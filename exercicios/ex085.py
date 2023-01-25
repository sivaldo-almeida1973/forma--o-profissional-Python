#crie uma função iteravel que receba uma lista de numeros
#e que retorne a cada iteração um item dessa lista #multiplicado por dois.
def duplicada(lista):
  for i in lista:
    yield i*2

lista = [1,2,3,4,5,6,7]

for i in duplicada(lista):
  print(i)