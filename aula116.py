#Divisão de Arrays

import numpy as np
array = np.array([1,2,3,4,5,6])
print(np.split(array,1))
print(np.split(array,2))
print(np.split(array,3))

print('-'*30)
import numpy 
array = numpy.array([[1,2,3,4],[4,5,6,7]])
print(np.split(array,2))

#metodo de divisão aproximado
print('-'*30)
import numpy 
array = numpy.array([1,2,3,4,5,6])
array1 = numpy.array_split(array, 2)
array2 = numpy.array_split(array, 3)
array3 = numpy.array_split(array, 4)
print(array1)
print(array2)
print(array3)


print('-'*30)
import numpy 
array = numpy.array([[1,2,3,],[4,5,6,]])
array1 = numpy.array_split(array, 2)
array2 = numpy.array_split(array, 3)
array3 = numpy.array_split(array, 4)
print(array1)
print(array2)
print(array3)


#divide por coluna
print('-'*30)
import numpy
array = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = numpy.hsplit(array,3 )
print(array1)