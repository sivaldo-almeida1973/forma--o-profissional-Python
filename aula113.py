#Alterando Dimensões(remodelar)reshape
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array = array.reshape(9)#remodelar
print(array)


print('-'*30)
#produzir um vetor de 27 elem
import numpy as np
array = np.array([i for i in range(0,27)])
print(array, end='\n\n')
array = array.reshape(3,9)#transfor na mariz 3x9
array1 = array.reshape(9,3)#transfor na matriz 9x3
array1 = array.reshape(3,3,3)#transfor 3 matriz 3 linha 3 colunas
print(array, end='\n\n')
print(array1)


print('-'*30)

import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array = array.flatten()#remodelar
print(array)