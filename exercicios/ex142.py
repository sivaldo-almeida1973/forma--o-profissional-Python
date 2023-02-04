#3 Mostre o numero de Mundiais de cada equipe Capa Racing.
import pandas as pd
dados = {
    'Sede': ['Nova Iorque', 'Sao Paulo','Nova Iorque', 'Londres','Londres'],
    'Piloto':['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
     'Mundiais':[10,11,0,3,44],
     'Vitorias':[321,229,12,44,1023]
}
data_frame = pd.DataFrame(dados, index=['X Racing','Equatorial', 'Type','Blue Race','Capa Racing'])

data = data_frame.loc[ 'Capa Racing', 'Mundiais']
print(data)