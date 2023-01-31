#produção de Objetos Preenchidos

import numpy

array1 = numpy.zeros(9)
array2 = numpy.ones(3)
array3 = numpy.empty(6)
array4 = numpy.identity(4)

print(array1, end='\n\n')
print(array2, end='\n\n')
print(array3, end='\n\n')
print(array4, end='\n\n')


print('-'*30)

import numpy

array1 = numpy.zeros((3,3))
array2 = numpy.ones((4,4))

print(array1, end='\n\n')
print(array2, end='\n\n')



print('-'*30)
#por intervalo
import numpy

array1 = numpy.arange(9)# de 0 até  8
array2 = numpy.arange(4,16)#de 4 até 15
print(array1)
print(array2)


print('-'*30)
#posso usar  arange passar parametro por intervalo especifico
import numpy

array1 = numpy.arange(2,16+1,2)# de 0 até  8

print(array1)


print('-'*30)
#Função fuul preenche com valor especifico

import numpy
array = numpy.full((4,4), 10)
print(array)


print('-'*30)
#Numeros aleatorios
import numpy
array_float = numpy.random.rand(4,4)
array_int =  numpy.random.randint(5,11 ,(5,5))
print(array_float)
print(array_int)


print('-'*30)
# list Comprehension(como criar uma lista)
import numpy
array = numpy.array([[i for i in range(0,3)],
                    [i for i in range(3,6)],
                    [i for i in range(6,9)]]
)
print(array)