#Da mesma forma que o ex. anterior ,gere a soma
#de 100 numeros alatorios e mostre o result final.

from random import randrange
soma = 0

for i in range(0,100):
  soma += randrange(1,100)

  print(soma)
