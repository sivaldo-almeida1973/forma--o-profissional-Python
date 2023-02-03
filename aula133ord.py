#Ordenar valores

import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
data.loc['Sivaldo','Idade'] = None
print(data)
#cria uma copia e ordena por idade
copy = data.sort_values('Idade', ascending=True, inplace=False)
print(copy)

#ordenar com valor nulo em primeiro (first)
copy = data.sort_values('Idade', ascending=True , inplace=False, na_position='first')
print(copy)

#ordenar com valor nulo em ultimo (last)
copy = data.sort_values('Idade', ascending=True , inplace=False, na_position='last')
print(copy)

#ordenar por mais de uma coluna, primeiro deixar duas idades iguais
data.loc['Maria','Idade'] = 34
print(data)
#ordenar de forma ascendente por idade, segundo criterio altura da maior
copy = data.sort_values(['Idade','Altura'], ascending=[True,False ],inplace=False, na_position='first')
print(copy)