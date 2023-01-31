#concatenação de array

import numpy as np
array1 = np.array([10,20,30,5])
array2 = np.array([20,40,10,5])
array12 = np.concatenate((array1,array2),axis=0)#linha
print(array12)

print('-'*30)
#concatenação com mais de uma dimenssão
import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12 = np.concatenate((array1,array2), axis=0)#linha
print(array12, end='\n\n')
array12 = np.concatenate((array1,array2), axis=1)#coluna
print(array12)


print('-'*30)
#
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array12r = np.vstack((array1, array2))#linha
array12c = np.hstack((array1, array2))
print(array12r)
print(array12c)



print('-'*30)
#concatenação com mais de uma dimenssão
import numpy as np
array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[7,8,9],[10,11,12]])
array12r = np.vstack((array1,array2))#linha por linha
print(array12r, end='\n\n')
array12c = np.hstack((array1,array2))#coluna por coluna
print(array12c)