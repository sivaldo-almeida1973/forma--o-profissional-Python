#Crie uma matriz 2x2 e imprima o primeiro elemento da #primeira linha, e o ultimo da ultima linha.
import numpy
array = numpy.random.randint(1,5,(2,2))
print(array)
print(array[0][0])
print(array[1][1])