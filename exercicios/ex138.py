#Crie uma função  que ordena uma matriz e remova todos os impares.
import numpy 
def remove_impares(arr):
  filter = arr % 2 == 1
  return arr[filter]

array = numpy.array([i for i in range(0,100)])
print(array)
print(remove_impares(array))

