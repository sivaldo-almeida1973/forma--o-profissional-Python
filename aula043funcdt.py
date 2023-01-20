#funções de data e hora

import datetime

data_completa = datetime.datetime.now()#dia/mes/ano/hora/min/s
data = data_completa.date()  #dia/mes/ano
hora = data_completa.time() #hora/min/seg.

print(data_completa)
print(data)
print(hora)


print('-'*30)
import datetime

data_completa = datetime.datetime.now()


print('Dia:',data_completa.day)
print('Mês:',data_completa.month)
print('Ano:',data_completa.year)
print('Hora:',data_completa.hour)
print('Minuto:',data_completa.minute)
print('Segundo:',data_completa.second)

print('-'*30)
import datetime

data = datetime.date(2000,9,30)
data = datetime.date(day=30, month=9, year=2000)
print(data)
print(type(data))


print('-'*30)
import datetime
hora = datetime.time(10,30,20)
print(hora)


print('-'*30)
import datetime

data = datetime.datetime(2000,9,30,10,30,20)
print(data)

print('-'*30)
#formatação de data
import datetime
# y ano
# m mês
# d dia
# H hora
# M minuto
# S segundo
atual = datetime.datetime.now()
current_time = atual.strftime('%y/%m/%d %H:%M:%S')#tranform em string(strftime)
print(current_time)
print(type(current_time))


print('-'*30)
#formatação de data
import datetime
# y ano
# m mês
# d dia
# H hora formato 24 horas/ ou militar
# M minuto
# S segundo
# A dia da semana
# a dia da semana abrev.
# B nome do mês 
# b nome do mês abrev.
# I hora no format de 12 horas
# p AM PM

data = datetime.datetime(2000,9,30,10,30,20)
print(data.strftime('%A  - %a'))
print(data.strftime('%B  - %b'))
print(data.strftime('%H  - %I'))
print(data.strftime('%I  - %p'))


