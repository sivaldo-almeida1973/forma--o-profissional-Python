#como acessar numpy usando slicing

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array[2])
print(array[2:4])

print('-'*30)
#agora em duas dimensões(matriz 3x3)
import numpy as np
array = np.array([ [1,2,3],[4,5,6]  ,[7,8,9]])
print(array, end='\n\n')
print(array[2])#por linha
print(array[2][2])
print(array[1:3])# 
print(array[2,1:3])#na seg -linha pos1 à pos3

print('-'*30)

import numpy as np
array = np.array([ [1,2,3],[4,5,6]  ,[7,8,9]])
print(array, end='\n\n')
print(array[2, :])#quero daultima linha todo o intervalo
print(array[:,2])#ultima coluna da matriz


print('-'*30)
#quatro colunas com duas linhas
import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8] ])
print(array, end='\n\n')
print(array[1, :])
print(array[:,2])
print(array[:,1])


print('-'*30)
#9 colunas com 3 linhas
import numpy as np
array = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27] ])
print(array, end='\n\n')
print(array[1, :])#imprimir linha 1 com todas as colunas
print(array[1, 1:5])#linha 1 colunas de indice 1 à 4
print(array[1, 0:8:2])#limha 1 do indice 0 a 8 de 2 em 2



