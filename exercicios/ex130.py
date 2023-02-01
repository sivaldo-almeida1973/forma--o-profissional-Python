#Crie um array 4x9 com os valores quaisquer,redimensione para as dimensões 36, e 6x6.
import numpy
array = numpy.random.randint(0,10,(4,9))
print(array.reshape((36)))
print(array.reshape((6,6)))