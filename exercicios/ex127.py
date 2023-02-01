#gere uma array 3x3 com numeros inteiros aleatorios entre 5 #e 20.Então imprima a primeira e a ultima linha.
import numpy
array = numpy.random.randint(5,20,(3,3))
print(array, end='\n\n')
print(array[:,0] , end='\n\n')#primeira
print(array[2,:], end='\n\n')#ultima linha