#Outras formas de declarar tipos

import numpy

array = numpy.array([1,2,3,4,5,6,7,8,9,0])
print(array)
print(type(array))#tipo obj para o python
print(array.dtype)#tipo do obj para o numpy


import numpy

array = numpy.array([1,2,3,4,5,6,7,8,9,0], dtype= numpy.int8)
print(array)
print(type(array))#tipo obj para o python
print(array.dtype)#tipo do obj para o numpy

print('-'*30)
import numpy

array = numpy.array(['1','234','1'], dtype= numpy.string_)
print(array)
print(type(array))#tipo obj para o python
print(array.dtype)#tipo do obj para o numpy


print('-'*30)
"""i = inteiro b = booleano u = inteiro sem sinal f = ponto flutuante S = String(bytes) U = String Unicode
"""
import numpy
array = numpy.array(['abc','def','ghi'] , dtype= 'S3')
print(array)
print(array.dtype)#tipo do obj para o numpy
print(array.itemsize)#tamanho de cada item
print(array.nbytes)#tamanho total

print('-'*30)
#com numeros
import numpy
array = numpy.array([1,2,3] , dtype= 'i2')
print(array)
print(array.dtype)#tipo do obj para o numpy
print(array.itemsize)#tamanho de cada item
print(array.nbytes)#tamanho total
