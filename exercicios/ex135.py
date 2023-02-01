#Crie uma função que diga se um array possui numeros negativos 
import numpy
def possui_negativo(arr):
  return numpy.any(arr < 0)

array = numpy.array([1,2,-3,-4,-5,6,7])
print(possui_negativo(array))
