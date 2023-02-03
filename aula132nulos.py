#tratando Nulos e Ordenando

import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')

data.loc['Antonio'] = (56,70.0,1.7, 'empresario','Rua Belgica')


#primeiro inluir um valor nulo
data.loc['Antonio','Idade'] = None



#como verificar se um valor é nulo chamando a função isnull()
data = data.isnull()
print(data)

#posso usar o metodo diretamente do pandas por colunas
data = pd.isnull(data['Idade'])
print(data)

#posso verificar tambem valores não nulos
data = data.notnull()
print(data)


import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')

data.loc['Sivaldo','Idade'] = None
print(data)




#Filtra valores nulos(mask)
mask = pd.notnull(data['Idade'])
print(mask)

#se aplicar a mascara o valor ira sumir
data = data[mask]
print(data)
