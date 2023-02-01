#Operações Aritimeticas com metodos especificos do numpy

import numpy
arr1 = numpy.array([1,2,3,4,5,6,18])
arr2 = numpy.array([1,2,3,4,5,6,3])

array1 = numpy.add(arr1, arr2)
array2 = numpy.subtract(arr1 , arr2 )
array3 = numpy.multiply(arr1 , arr2 )
array4 = numpy.divide(arr1 , arr2 )

print(array1)
print(array2)
print(array3)
print(array4)

print('-'*30)
import numpy
arr1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
array = numpy.add(arr1, arr2)
print(array)



print('-'*30)
import numpy
arr1 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
array1 = numpy.divide(arr1, arr2)
array2 = numpy.floor_divide(arr1, arr2)#divisão de inteiros
print(array1)
print(array2)

#power(potencia)
print('-'*30)
import numpy
arr1 = numpy.array([1,2])
arr2 = numpy.array([2,4])
array1 = numpy.power(arr1, arr2)
print(array1)


print('-'*30)
#Resto da divisão por inteiro(vai gerar 2 arrays)
#divisão por inteiro e o resto da divisão
import numpy
arr1 = numpy.array([2,2,100])
arr2 = numpy.array([2,3,31])

array1 = numpy.divmod(arr1, arr2)
print(array1)



print('-'*30)
#Resto da divisão por inteiro(vai gerar 2 arrays)
#divisão por inteiro e o resto da divisão
import numpy
arr1 = numpy.array([2,2,100])
arr2 = numpy.array([2,3,31])

array1 = numpy.divmod(arr1, arr2)#faz 2 calculos simultaneos
print(array1)


print('-'*30)
#Raiz quadrada
import numpy
arr1 = numpy.array([2,2,100])
array1 = numpy.sqrt(arr1)#raiz quadrada
print(array1)


#Arredondamento de valores.
print('-'*30)
import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.around(arr1,2)#arredonda pra 2 casas
print(array)

#Truncar valores pra baixo
print('-'*30)
import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.floor(arr1)#arredonda pra  baixo
print(array)


#Truncar valores pra cima
print('-'*30)
import numpy
arr1 = numpy.array([3.14159, 2.71])
array = numpy.ceil(arr1)#arredonda pra  cima
print(array)