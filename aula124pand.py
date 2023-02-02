#Importando dados
import pandas as pd
data = pd.read_csv('pessoa2.csv', index_col='nome')
print(data)

print(data.loc['Lucas'])
print(len(data.columns))
print(data.columns)
print(len(data.index))
print(data.index)
print(data.shape)#fromato

print('-'*30)
#a cada interaçao 
for indice, linha in data.iterrows():
  print(indice, linha[0], linha[1])

for coluna in data:
  print(coluna)

#acessar todos os valores de uma determinada coluna
print(data['profissao'])

print('-'*30)
for coluna in data:
  print(data[coluna])
  
print('-'*30)
print(data.loc['Sivaldo']['profissao'])
print(data.loc['Sivaldo'][0])

print('-'*30)
print(data.iloc[0]['profissao'])
print(data.iloc[0][0])



