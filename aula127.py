import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)

print('-'*20)

print(data.loc['Lucas']['profissao'])
print(data.loc['Lucas'][0])

print('-'*20)
print(data.iloc[0]['Idade'])
print(data.iloc[0][0])


print('-'*20)
#loc pelo indice
print(data.loc['Lucas'])
print(type(data.loc['Lucas']))


#Iloc pela posição
print('-'*20)
print(data.iloc[0])


print('-'*20)

#Slicing (fatiamento) usando loc
print(data.loc['Lucas':'Sivaldo'])


print('-'*20)

#Slicing (fatiamento) usando iloc
print(data.iloc[0:3])

print('-'*20)
#usando o nome da coluna(serie)
print(data['Idade'])


print('-'*20)
#usando o nome da coluna(serie)
idade = data['Idade']
print(idade[3])
print(idade['Lucas'])


print('-'*20)
print(data[['Idade','Altura']])

colunas = data[['Idade','Altura']]
print(type(colunas))

