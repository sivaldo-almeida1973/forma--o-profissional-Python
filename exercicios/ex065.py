#leia por input sua data de nascimento no formato
# Dia/Mes/Ano e mostre quantos dias voce ja viveu
import datetime

data_txt = input('digite a data em que voce nasceu em formato dia/mes/ano:')
data_nascimento = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_agora - data_nascimento
print('voce ja viveu', diferenca_datas, 'dias')
