"""
crie um programa que receba 5 numeros, 
e que realize a soma destes,mas caso um deles
seja negativonão o inclua na soma. 
"""

soma_atual = 0
numeros_lidos = 0
while( numeros_lidos < 5 ):
    num_str = input('digite um numero:')
    num_lido = float(num_str)
    if num_lido >= 0:
      soma_atual += num_lido 
    numeros_lidos += 1


print('A soma dos %.2f' % soma_atual)


