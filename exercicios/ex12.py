saldo_texto = '2500'
saldo = int(saldo_texto)
total = saldo - 1000
print('tenho no banco RS %.2f' % (total))

print('-'*40)

saldo = 0.0
esta_zerado = not bool(saldo)
print('saldo zerado:', esta_zerado)

print('-'*20)

altura = 1.75
altura_inteira = int(altura)
print('tenho pelo menos %i metro de altura'  % (altura_inteira))