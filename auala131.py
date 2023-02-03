#Remoção de colunas
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)
data.loc['Antonio'] = (56,70.0,1.7, 'empresario','Rua Belgica')
print(data)


#remover a coluna peso
data.drop(columns=['Peso'], inplace=True)
print(data)

#remover coluna pelo indice
data.drop(columns=data.columns[[1,3]], axis=1, inplace=True)
print(data)