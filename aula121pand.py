#Pandas(séries)
import pandas as pd
pd.Series([1,2,3,4,5])

print('-'*30)
import pandas as pd
minha_series = pd.Series([1,2,3,4,5], dtype='i4')
print(minha_series)


print('-'*30)
import pandas as pd
minha_series = pd.Series([1,2,3,4,5],dtype='i4', name='Meus numeros')
print(minha_series)

print('-'*30)
import pandas as pd
minha_series = pd.Series([1,2,3,4,5],dtype='i4', name='Meus numeros', index=['um','dois','tres','quatro', 'cinco'])
print(minha_series)
print(minha_series['um'])
print(minha_series['quatro'])
print(minha_series.shape)

#Adicionar um novo valor
print('-'*30)
import pandas as pd
minha_series = pd.Series([1,2,3,4,5],dtype='i4', name='Meus numeros', index=['um','dois','tres','quatro', 'cinco'])
minha_series['seis']= 6
print(minha_series)

#como criar uma serie apartir de um objeto numpy.
import pandas as pd
import numpy as np
array = np.array([73.5, 63.5, 76.5, 85.5])
pesos = pd.Series(array, index=['Lucas','Alice','sivaldo', 'guti'])#transf pandas
print(pesos)
print(type(pesos))
