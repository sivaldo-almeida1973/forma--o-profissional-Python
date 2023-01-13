#Estudos dos (ifs)
"""
print('isto está fora dos ifs')
if (True):
    print('este codigo será executado!')

print('este também esta fora dos ifs')

if (False):
    print('este codigo não será executado!')   

print('mas um que esta fora!') 

if (True):
    pass
"""
valor1 = 10
valor2 = 20
sao_iguais = (valor1 == valor2)
if sao_iguais:
    print('sivaldo')
else:
    print('lucas e lice')
print('-'*20)

valor1 = 10
valor2 = 10
(valor1 == valor2)
if (valor1 == valor2):
    print('sivaldo')
    print('sivaldo')
    print('sivaldo')
print('-'*20)

valor1 = 10
valor2 = 10
if (valor1 == valor2): print('alice')

print('-'*20)

if(10 != 20):
    print('sim são diferentes')

print('-'*20)

if('olá' != 'alo'):
    print('são diferentes')

    print('-'*20)
numero = 11
if (numero >= 11):
    print('É maior que 10')

print('-'*20)

nome = input('digite seu nome:' )
if 'a' in nome:
    print('Sim  seu nome possui a letra \'a\'')


print('-'*20)

nome = input('digite seu nome: ')
possui_vogal = ('a' in nome) or ('' in nome) or ('i' in nome) or ('o' in nome) or ('u' in nome) 
if possui_vogal:
    print('possui vogal!')



