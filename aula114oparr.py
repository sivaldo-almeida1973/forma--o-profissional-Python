#Operações sobre arrays(matrizes)
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 / array2)
print(array1 * array2)
print(array1 ** array2)
print(array1 // array2)


#dessa forma soma arr1 co prim e segundo 
print('-'*30)
import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([[4,5,6],[1,2,3]])
array3 = np.array([[2,3,4],[1,2,3],[4,5,6]])
print(array1 + array2 )
print(array1 + array3 )


print('-'*30)
#posso fazer operações com array e elementos primitivos
import numpy as np
arry1 = np.array([1,2,3])
print(array1 + 2)
print(array1 - 2)


#Operadores de comparação
import numpy as np
array1 = np.array([11,21,31,41,51])
array2 = np.array([1,29,3,45,5])

print(array1 > array2)#maior 
print(array1 == array2)#igual
print(array1 != array2)#diferente

#se array é gual comparando todos os elementos
import numpy as np
array1 = np.array([11,21,31,41,51])
array2 = np.array([1,29,3,45,5])
array3 = np.array([11,21,31,41,51])
print(np.array_equal(array1,array2))
print(np.array_equal(array1,array3))





