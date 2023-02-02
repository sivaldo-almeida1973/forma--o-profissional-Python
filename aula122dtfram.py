#Data Frames do panda

import pandas as pd
data_frame = pd.DataFrame()
print(data_frame)

print('-'*30)

import pandas as pd
nomes = ['Lucas', 'Alice', 'Sivaldo', 'Maria']
data_frame = pd.DataFrame(nomes)
print(data_frame)

print('-'*30)
import pandas as pd
numeros =[
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14']

]
data_frame = pd.DataFrame(numeros)
print(data_frame)


print('-'*30)
import pandas as pd
numeros =[
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14'],
          ['11','12','13','14'],
         
]
data_frame = pd.DataFrame(numeros, columns=['a','b','c','d'], index=['x','y','z','w'])
print(data_frame)

