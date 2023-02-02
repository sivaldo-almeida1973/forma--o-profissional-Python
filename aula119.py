#Acumuladores
#somar todos os elementos de um array (sum)
import numpy
array = numpy.array([[1,2,3], [4,5,6]])
array_sum = numpy.sum(array)#somar tudo
print(array_sum)
#somar liha por linha(sum)+ axis=0
print('-'*30)
import numpy
array = numpy.array([[1,2,3], [4,5,6]])
array_sum = numpy.sum(array, axis= 1)#somar linha por linha
print(array_sum)

#soma aculmulativa(cumsum)
print('-'*30)
import numpy
array = numpy.array([[1,2,3], [4,5,6]])
array_sum = numpy.cumsum(array)#somar linha por linha
print(array_sum)


#Resultado do produto(cumprod)
print('-'*30)
import numpy
array = numpy.array([[1,2,3], [4,5,6]])
array_sum = numpy.cumprod(array)#somar linha por linha
print(array_sum)


#Resultado do produto(cumprod)
print('-'*30)
import numpy
array = numpy.array([[1,2,3], [4,5,6]])
array1 = numpy.cumprod(array, axis=0)#por coluna
array2 = numpy.cumprod(array, axis=1)#por linha
print(array1)
print(array2)

#maior valor e menor valor(amin) menor (amax) maior
print('-'*30)
import numpy
array = numpy.array([[1,2,3,4,5,6]])
print(numpy.amin(array))#menor
print(numpy.amax(array))#maior

#valor absoluto  (abs)
print('-'*30)
import numpy
array = numpy.array([[1,2,3,4,5,6]])
print(numpy.abs(array))#absoluto


#valor absoluto  (abs)
print('-'*30)
import numpy
array = numpy.array([[1,2,3],[4,5,6]])
print(array)
print(numpy.amin(array))#menor valor geral
print(numpy.amin(array, axis= 1))#menor valor por linha
print(numpy.amin(array, axis= 0))#menor valor por coluna