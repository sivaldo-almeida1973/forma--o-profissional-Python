#leia por input sua proxima data de aniversário
#no formato dia/Mes/ano e mostre quantos dias
#faltam para seu proximo aniverssario.
import datetime
data_txt = input('digite a data do seu proximo aniversario no formato dia/mes/ano:')
data_aniversario = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
data_agora = datetime.datetime.now()
diferenca_datas = data_aniversario - data_agora
print('voce fara aniversario daqui' ,diferenca_datas.days, 'dias')
