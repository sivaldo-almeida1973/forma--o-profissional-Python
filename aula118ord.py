#Ordenação no array

import numpy
array = numpy.array([4,1,3,2])
print(numpy.sort(array))#imprime ordenado

print('-'*30)
import numpy
array = numpy.array([4,1,3,2])
print(numpy.sort(array, kind='quicksort'))#(quicksort) oredençao rapida


#mas de uma dimenssão
print('-'*30)
import numpy
array = numpy.array([[38,2,1],[5,5,4]])
print(numpy.sort(array, axis=0))# eixo 0 por linha
print(numpy.sort(array, axis=1))#eixo 1 por coluna