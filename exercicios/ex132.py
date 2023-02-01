#Crie um função que divida um array em N pedaços, mas so #mantenha os valores absolutos dos valores deste array. 
import numpy
def divide_abs(arr, n):
  arr = numpy.array_split(arr,n)#função da divisão
  arr = numpy.abs(arr)#valor absoluto(remove negativo)
  return arr
array1 = numpy.array([1,2,3,-4,5,-7])
print(divide_abs(array1,3))