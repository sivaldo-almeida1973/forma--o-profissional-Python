saldo = input('Digite seu saldo:')
divida = input('Digite o valor da divida:')
total_saldo = float(saldo) - float(divida)
if total_saldo  > 0 :
    print('Seu saldo é positivo, voce tem  R$ %.2f ' %(total_saldo))
else:
    print('Seu saldo é negativo, voce deve R$ %.2f !' % (total_saldo))
