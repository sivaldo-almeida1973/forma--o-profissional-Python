#Mascaras
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)

print('-'*30)
colunas = data.iloc[:,1:3]
print(colunas)

#imprimir da coluna idade ate a coluna profissão
print('-'*30)
colunas = data.loc[:,'Idade':'profissao']
print(colunas)

#mascara
print('-'*30)
mask = data['Idade'] > 30
print(mask)

#remove quem tem idade menor que 30 anos
print('-'*30)
nova_dframe = data[mask]
print(nova_dframe)


print('-'*30)
#multiplas funções
nova_dframe = data[(data['Idade'] > 30) & (data['Altura'] >= 1.70)]
print(nova_dframe)

#Mudar dados pelo objeto
print('-'*30)

data.at['Sivaldo','Idade'] = 48
data.at['Sivaldo', 'Altura'] = 1.72
data.at['Alice', 'Idade'] = 38
print(data)

#Mudar dados pela posição
print('-'*30)
data.iat[2,0] = 37
data.iat[2,0] = 37
data.iat[2,3] = 'eng. software'

print(data)
print('-'*30)
#Usando loc e indice posso alterar mais de um valor simultaneamente.
data.loc['Alice','Idade':'Peso'] =( 35, 62.0)
print(data)
print('-'*30)
#altera varias colunas
data.loc['Alice',['Idade','Peso','Altura']] =( 35, 62.0, 1.70)
print(data)
print('-'*30)
#alterando usando o iloc
data.iloc[0,2] = 1.80
print(data)

print('-'*30)
#atualizar a idades de todos, altura e peso
data.loc[:,'Idade'] = 22
data.loc[:,'Altura'] = 1.80
data.loc[:,'Peso'] = 60.0

print(data)

print('-'*30)

data.loc[:,'Idade':'Altura'] = None
print(data)

#posso alterar colunas especificas
print('-'*30)
data.loc[:,['Idade','Altura']] = (23,1.90)
print(data)

print('-'*30)

import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)

data.loc[(data['Idade'] <40), 'Altura'] = 1.99
print(data)

#atualizar mais de um valor
data.loc[(data['Idade'] == 27) & (data['profissao'] == 'Eng.software'),['Idade','Altura']] = (35, 1.7)
print(data)