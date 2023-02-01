#Crie uma função que receba um array e retorne quantos #numeros positivos ela contêm.

import numpy
def conta_positivos(arr):
  return len(numpy.where(arr > 0)[0])

array = numpy.array([1,2,3,-4,5,-7])
print(conta_positivos(array))

