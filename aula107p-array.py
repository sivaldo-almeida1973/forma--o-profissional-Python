#Propriedades de Arrays

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,0])
print(array) #num de dimensões
print(array.ndim)#dimensoes
print(array.size)#num elem total
print(len(array)) #tamanho pelo python
print(array.shape)#formato
print(array.dtype)#tipo de cada elemento
print(array.itemsize) #tam por item
print(array.nbytes)#bytes gasto pelo array no total


print('-'*30)
#Array em duas dimensoes(vou ter linha e colunas)
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)#num de dimensoes
print(array.ndim)#dimensoes
print(array.size)#num elem total
print(len(array)) #tamanho pelo python
print(array.shape)#formato
print(array.dtype)#tipo de cada elemento
print(array.itemsize) #tam por item
print(array.nbytes)#bytes gasto pelo array no total



print('-'*30)
import numpy
#outro exemplo(tipo especifico do numpy)
tipo_pessoa = numpy.dtype([ ('nome', 'S10'), ('idadde', 'i4') ])

array = numpy.array([('Rodrigo', 24),('lucas',22)], dtype= tipo_pessoa)
print(array)#num de dimensoes
print(array.ndim)
print(array.size)#num elem total
print(array.shape)#formato
print(array.dtype)#tipo de cada elemento
print(array.itemsize) #tam por item
print(array.nbytes)#bytes gasto pelo array no total
