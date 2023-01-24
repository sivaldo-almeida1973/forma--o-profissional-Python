#importe do modulo rando a função radrange e crie um
#programa que gere um unico numero aleatorio entre
#2 e 100.Em seguida diga se esse numero é par ou #impar.
from random import randrange
numero = randrange(2,100)
resto = numero % 2
if resto == 0:
    print('O numero %d é par ' % (numero))
else:
    print('o numero %d é impar' %(numero))

