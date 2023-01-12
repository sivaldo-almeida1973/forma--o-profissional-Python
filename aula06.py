"""
Ordem de prioridades
---------------------
1º o que esta entre Parênteses
2ª ** exponenciação
3º * multiplicação
4º / divisão
5º % resto da divisão
6º // divisão inteira
7º soma e subtração
"""

num1 = 10 * 2 + 1
print(num1)

print('-'*10)

num1 = 10 * (2 + 1)
print(num1)

print('-'*10)

num1 = 3 * (3-9)
print(num1)

print('-'*10)


num1 = 20
num2 = 30 
num3 = 40
resultado = num1 + num2 + num3
print(resultado)

print('-'*10)
resultado = resultado * 2
print(resultado)

print('-'*10)
a = 1
a += 1
print(a)
