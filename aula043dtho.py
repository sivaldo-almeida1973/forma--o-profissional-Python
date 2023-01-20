#manipulando data e hora
# 'timedelta'(permite mostrar diferença dentre datas)
import datetime
data1 = datetime.datetime(2020,10,20)
data2 = datetime.datetime(2023,1,20)
diferenca = data2 - data1
print(diferenca)
print(type(diferenca))

print('-'*30)
#usando timedelta
from datetime import datetime, timedelta

data_atual = datetime.now()
datafutura1 =data_atual + timedelta(weeks=4)
datafutura2 = data_atual + timedelta(days= 30)
datafutura3 = data_atual + timedelta(hours= 12)
datafutura4 = data_atual + timedelta(minutes= 60)

print('Data_atual:' , data_atual)
print('Mais 4 semanas:', datafutura1)
print('Mais 30 dias:', datafutura1)
print('Mais 12 horas:', datafutura1)
print('Mais 60 minutos:', datafutura1)

print('-'*30)
#como saber quanto ano/mes/ dia/ hora /minu/ seg /se passou
# desde 2000

import datetime
data_2000 = datetime.datetime(2000,1,1,0,0,0)
data_agora = datetime.datetime.now()
diferenca = data_agora - data_2000

print('desde de o ano 2000 passou', diferenca.days, 'dias')
print('desde de o ano 2000 passou', diferenca.seconds, 'segundos')
print('desde de o ano 2000 passou', diferenca.microseconds,'microsegundos')


anos = int(diferenca.days/365)
meses = anos * 12
print('desde de o ano 2000 passou', anos, 'anos')
print('desde de o ano 2000 passou', meses, 'meses')

print(diferenca)