#Crie uma função que remova os numeros negativos de um array.
import numpy
def remove_negativos(arr):
  filter = arr >= 0
  return arr[filter]

array = numpy.array([1,-5,4,-6,-7,8])
print(remove_negativos(array))

