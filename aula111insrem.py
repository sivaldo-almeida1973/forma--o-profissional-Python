#Inseri e remover elementos no numpy
import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
print(array, end='\n\n')
array[0] = [1,2,4]#substituir valores na linha 0
array[1,1:3] = [0,0]#trocar na linha 1
array[0:,2] = 10 # trocar na linha 0 na pos 0
print(array)

print('-'*30)
import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
print(array, end='\n\n')
array[0:,2] = [0]
print(array)

#fazer  append (adicionar elementos)
print('-'*30)
import numpy as np
array = np.array([[1,2,3,4]])
array2 = np.append(array, [5,6,7,8])
print(array2)

#fazer append em mas de uma dimenssão(assim muda a forma da matriz)
print('-'*30)
import numpy as np
array = np.array([[1,2,3],[5,6,7],[7,8,9]])
print(array, end='\n\n')
array2 = np.append(array, [0,0,0])
print(array2)

#vamos concertar o de cima(tenho que informar onde quero substituir) se não #provoca o fleping
print('-'*30)
import numpy as np
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array, end='\n\n')
array1 = np.append(array,[ [10,11,12]], axis=0) #adicionando por linha
array2 = np.append(array,[[10],[11],[12]], axis=1) #adicionando por coluna
print(array1, end='\n\n')
print(array2, end='\n\n')


#metodo insert
print('-'*30)
import numpy as np
array = np.array([1,2,3])
array = np.insert(array, 1,10)#inserir na position 1 o elem 10
print(array)


print('-'*30)
#insert em multiplas dimensões 
import numpy as np
array = np.array([[1,2,3],[7,8,9],[10,11,12]])
array1 = np.insert(array,1,[4,5,6], axis=0)#inserir no indice 1 a linha
array2 = np.insert(array,1,[0,0,0], axis=1)# inserir na coluna 1
print(array1)
print(array2)


print('-'*30)
#para remover elementos (delete)
import numpy as np
array = np.array([[1,2,3],[7,8,9],[10,11,12]])
array1 = np.insert(array,1,[4,5,6], axis=0)#inserir no indice 1 a linha
array2 = np.insert(array,1,[0,0,0], axis=1)# inserir na coluna 1
array2 = np.delete(array,1, axis= 1)
print(array1, end='\n\n')
print(array2)