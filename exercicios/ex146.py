#.Atualize com o mesmo comando a equipe X Racing, definindo sede como "São Paulo e vitoria como 32".

import pandas as pd
dados = {
    'Sede': ['Nova Iorque', 'Sao Paulo','Nova Iorque', 'Londres','Londres'],
    'Piloto':['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
     'Mundiais':[10,11,0,3,44],
     'Vitorias':[321,229,12,44,1023]
}
data_frame = pd.DataFrame(dados, index=['X Racing','Equatorial', 'Type','Blue Race','Capa Racing'])

data_frame.loc['X Racing',['Sede',' Vitoria']] =( 'Sao Paulo',322)
print(data_frame)