#Crie um array com os numeros de 1 a 20 , escolhendo o tipo #de dado que ocupara o menor espaço da memoria. Em seguida #imprima o quanto ele ocupou em bytes.
import numpy
array = numpy.arange(1,21 , dtype=numpy.int8)
print(array)
print(array.nbytes, 'bytes')