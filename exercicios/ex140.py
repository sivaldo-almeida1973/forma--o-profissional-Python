#1. Crie um dataframe com a estrutura abaixo.os indices devem ser as 
#Equipes 'X Racing', 'Equatorial','Typo','Blue Race','Capa Racing'.
#utilize um dicionario.





#Inclua uma nova equipe Red Cow, com sede em São Paulo.
import pandas as pd
dados = {
    'Sede': ['Nova Iorque', 'Sao Paulo','Nova Iorque', 'Londres','Londres'],
    'Piloto':['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
     'Mundiais':[10,11,0,3,44],
     'Vitorias':[321,229,12,44,1023]
}
data_frame = pd.DataFrame(dados, index=['X Racing','Equatorial', 'Type','Blue Race','Capa Racing'])
print(data_frame)

#2.mostre todas as iformações da equipe Blue Race.
data = data_frame.loc['Blue Race']
print(data)