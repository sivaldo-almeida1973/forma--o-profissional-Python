#Adicionando Linhas e no final do data_frame
import pandas as pd
data = pd.read_csv('funcionarios.csv', index_col='Nome')
print(data)
data.loc['Antonio'] = (56,70.0,1.7, 'empresario','Rua Belgica')
print(data)


#criando outra data_frame.
data_adicional = pd.DataFrame({
             'Idade': [48,57,58],
             'Peso':[70.0, 65.0,85.0],
             'Altura':[1.65,1.60,1.75],
             'profissao': ['gerente','ass. social','empresario'],
             'endereco':['Rua portugal','Rua alemanha','Rua Italia']},
             index = ['Rogerio','Vanusa','James'])

data_adicional.index.name = 'Nomes'
print(data_adicional)

#inserindo data_adicional no primeiro data_frame
data = data.append(data_adicional)
print(data)


#adicionando colunas, existem varias formas.
#dessa forma ,adiciona no final, ficara vazio
data['sobrenome'] = None
print(data)

#dessa forma adiciona o proprio sobrenome escolhido
data['sobrenome'] = ['Almeida','Moraes ', 'Vieira Almeida','','','','','','']
print(data)


#agora inserindo em um local especifico
data.insert(loc=1,column='Data Nascimento', value=['02/06/2000' for i in range(9)])
print(data)

