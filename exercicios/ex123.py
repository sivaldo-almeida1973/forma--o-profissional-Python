#Crie um array com os numeors de 0 a 8, utilize 2 #dimenssões, ou seja,com 3 linhas(3x3).
import numpy
array = numpy.array([[1,2,3],[6,7,8],[11,12,13]])
print(array)

print('-'*30)
#pode ser assim tambem
import numpy
array = numpy.arange(9).reshape((3,3))
print(array)
