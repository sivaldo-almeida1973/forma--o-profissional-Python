import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data,'\n\n')
print(data.loc['Sivaldo'],'\n\n')
print(len(data.columns))
print(data.columns)
print(len(data.index))
print(data.index)
print(data.shape)

for indice , linha in data.iterrows():
  print(indice, linha [0], linha[1],linha[2])

#por coluna
for coluna in data:
  print(coluna)
print('-'*30)
#todos o valores
print(data['Altura'], '\n\n')



for coluna in data:
  print(data[coluna])
