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

data_frame.loc['Red Cow'] = ('Sao Paulo','Fernado Vetel', 0, 0)
print(data_frame)

dados = data.iloc[:,1:3]
print(dados)