#Data Frame apartir de um dicionario
import pandas as pd
dados = {
    'Nome':['Lucas','Alice','Sivaldo','Gute'],
    'Idade':[22,38,48,45],
    'Profissão':['Advogado','Eng.Software','Eng.Software','Empresario']

}
data_frame = pd.DataFrame(dados)
print(data_frame)

print('-'*30)
#podemos transformar os nomes em indices

import pandas as pd
dados = {
   
    'Idade':[22,38,48,45],
    'Profissão':['Advogado','Eng.Software','Eng.Software','Empresario']

}
data_frame = pd.DataFrame(dados, index=['Lucas','Alice','Sivaldo','Gute'])
print(data_frame)

print(data_frame.loc['Lucas'])