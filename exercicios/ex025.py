"""
crie um programa que receba 5 numeros e retorne a média aritimética entres eles.
"""
soma_atual = 0 #criar variável
numeros_lidos = 0 # var pra controlar num lidos
while (numeros_lidos < 5): # ate quantos numeros
    num_str = input('digite um valor:')# entrada numeros
    num_lido = float(num_str) # mudar para float
    soma_atual += num_lido # somar 0 com numero digitado
    numeros_lidos += 1 # controle de fim do laço

media = soma_atual / 5
print('A media é %.2f ' % (media))