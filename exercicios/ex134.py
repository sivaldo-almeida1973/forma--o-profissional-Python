#Crie uma função que receba uma matriz e retorne os indices #dos numeros que são divisiveis por 3.

import numpy
def divisiveis_por_3(arr):
  return numpy.where(arr % 3 == 0)

array = numpy.array([4,5,6,7,8,9])
print(divisiveis_por_3(array))