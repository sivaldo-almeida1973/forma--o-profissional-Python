#Agrupando valores com pandas
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)

#adicionar mais valores
data.loc['Rogerio'] = (43,70.0, 1.65, 'programador', 'rua coritiba')
data.loc['james'] = (52,85.0, 1.75, 'empresario','rua uruguai')
data.loc['Antonio'] = (56, 70.0, 1.70,'empresario','rua minas')
data.loc['José'] = (54,90.0, 1.75, 'empresario','rua goias')
data.loc['Vanusa'] = (47,65.0, 1.60, 'medica','rua paraná')
data.loc['Gute'] = (45,86.0, 1.60, 'empresario','rua paraná')
print(data)
#mostrar de acordo com profissão(criar grupo)
grupos = data.groupby('profissao')

for indice, grupo in grupos:
  print(indice)
  print(grupo)
#selecionar por profissao
#print('-'*60)
#data = grupos.get_group('Eng.software')
#print(grupos)



print('-'*60)
grupos = data.groupby(['profissao','Idade'])
print(grupos.describe())


