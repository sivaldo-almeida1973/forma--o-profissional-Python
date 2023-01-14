"""
Percorra os numeros de 2 até 10 e diga se o numero é 
par ou impar.
"""
num_atual = 2
while (num_atual <= 10):
    resto = num_atual % 2
    if ( resto == 0):
        print('o numero %d é par' % num_atual)
    else:
        print('o numero %d é impar' % num_atual)
    num_atual += 1

print('Fim')

