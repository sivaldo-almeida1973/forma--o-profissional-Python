#Remoção de linhas
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)
data.loc['Antonio'] = (56,70.0,1.7, 'empresario','Rua Belgica')
print(data)

#remover linhas(drop)copia

data2 = data.drop(index = ['Antonio','Gute'])
print(data2)

#nesse caso não sumiu do frame original, mas caso queira que suma usar(inplace= True)
data.drop(index = ['Antonio', 'Gute'] , inplace = True)
print(data)

#fazer remoção pelo indice
data2.drop(index = data2.index[[1,2]], inplace= True)
print(data2)

print('-'*30)
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)
data.loc['Antonio'] = (56,70.0,1.7, 'empresario','Rua Belgica')
print(data)

#fazer remoção por condição criada
data.drop(index = data[data['Altura'] >= 1.7].index, inplace=True)
print(data)

