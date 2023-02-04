#5.Mostre apenas as equipes que tem  10 ou mais mundiais e mais de 300 vitorias.
import pandas as pd
dados = {
    'Sede': ['Nova Iorque', 'Sao Paulo','Nova Iorque', 'Londres','Londres'],
    'Piloto':['Mike Ross','Sebastian Thomas','Glen Are','Michael Schum','Luiz da Silva'],
     'Mundiais':[10,11,0,3,44],
     'Vitorias':[321,229,12,44,1023]
}
data_frame = pd.DataFrame(dados, index=['X Racing','Equatorial', 'Type','Blue Race','Capa Racing'])

data_frame[ (data_frame['Mundiais']>=10) & (data_frame ['Vitorias'] >= 300 )]
print(data_frame)

