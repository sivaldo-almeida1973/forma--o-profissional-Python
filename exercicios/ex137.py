#Crie uma função que receba um numero inicial e final, e #uma array.A função deve retornar uma nova array somente #com os numeros dentro deste intervalo.
import numpy
def remove_valores(arr,inicial ,final):
  filter = (arr >= inicial) & (arr<= final)
  return arr[filter]

array = numpy.array([i for i in range(-10,11)])
print(array)
print(remove_valores(array,0,7))




