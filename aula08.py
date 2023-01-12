"""
CASTING
"""
texto = 'Olá , mundo'
numero = 10
decimal = 1.5
booleano = True

print(type(texto))
print(type(numero))
print(type(decimal))
print(type(booleano))
print('-'*20)
#CONVERSSÃO DE STRING PARA INT E FLOAT
texto1 = '2'
texto2 = '2.2'

num1  = int(texto1)
num2  = float(texto2)
print(type(texto1))
print(type(num1))
print(type(num2))
print(num1 + num2)

print('-'*20)

num = 21.65433
inteira = int(num)
print('A parte inteira de %f é %d '%(num, inteira))

print('-'*20)

texto = 'O numero é:'
numero = 10.5

num_string = str(numero)
print(texto, num_string)
print(type(num_string))

print('-'*20)

