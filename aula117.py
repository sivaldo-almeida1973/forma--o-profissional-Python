#Filtrando elementos com (where)= onde

import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.where(array >= 4)#vai retornar o indice
array_find2 = numpy.where((array == 3) |( array == 2))#indice
print(array_find)
print(array_find2)

print('-'*30)
import numpy
array = numpy.array([1,-1,-3,0,6,3,-78])
array_find = numpy.where(array >= 4)#vai retornar o indice
array_find2 = numpy.where((array > 0) & ( array < 10))#indice
print(array_find)
print(array_find2)



#verdadeiro ou falso(any)= nenhum
print('-'*30)
import numpy
array = numpy.array([1,3,4,2,7,4])
array_find2 = numpy.any(array == 3) 
print(array_find2)



print('-'*30)
import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.any((array > 0)& (array < 10)) 
print(array_find)



#verdadeiro o falso (all)= todos
print('-'*30)
import numpy
array = numpy.array([1,3,4,2,7,4])
array_find = numpy.all(array > 0) 
print(array_find)


#usando o filter
print('-'*30)
import numpy
array = numpy.array([1,0,1,1,1,0,0,])
filter = array == 1
filter_array = array[filter]#elementos igual a 1
print(filter_array)



print('-'*30)
import numpy
array = numpy.array([1,0,1,1,1,0,0,2])
filter = (array == 1) | (array == 2)
filter_array = array[filter]#elementos igual a 1
print(filter_array)


#interation
print('-'*30)
import numpy
array = numpy.array([1,0,1,1,1,0,0,2])
filtered_array = numpy.array([i for i in array if i == 0])
print(filtered_array)
