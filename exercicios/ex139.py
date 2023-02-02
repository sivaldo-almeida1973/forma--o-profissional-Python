#Realize o mesmo exercicio anterio, mas remova valore duplicados.
import numpy
def remove_duplica(arr):
  arr = numpy.sort(arr)
  filter = arr % 2 == 1
  return numpy.unique(arr[filter])


array = numpy.random.randint(0,20,(100))
print(remove_duplica(array))