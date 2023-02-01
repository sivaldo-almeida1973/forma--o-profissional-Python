#Gere um array com os valores pares de 0 a 100 com list #comprehension.
import numpy
array = numpy.array([i for i in range(0,101) if i % 2 == 0])
print(array)