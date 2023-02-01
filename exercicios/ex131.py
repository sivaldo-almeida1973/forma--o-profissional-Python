#Crie uma função que receba tres arrays de mesmo formato , #então retorne elas conactenadas em uma só.Se as matrizes #recebidas não forem do mesmo formato gere uma exceção.
import numpy
array = numpy

def combina(arr1,arr2,arr3):
  if arr1.shape != arr2.shape or arr1.shape != arr3.shape:
    raise Exception('Formatos sao diferentes')

  return numpy.concatenate((arr1,arr2,arr3))

array1 = numpy.array([1,2,9,8])
array2 = numpy.array([4,5,6])
array3 = numpy.array([7,8,9])
print(combina(array1,array2,array3))