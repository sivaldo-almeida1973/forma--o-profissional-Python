"""
Criar um programa que receba um número arbitrário
(definido pelo usuário) de numeros que serão lidos
e retorne a soma de todos eles.
"""
numeros_que_devem_ser_lidos = int(input('Quantos numeros devem ser lidos?' ))
soma_atual = 0
numeros_lidos = 0
while( numeros_lidos < numeros_que_devem_ser_lidos):
    num_str = input('digite um valor:')
    num_lido = float(num_str)
    if num_lido >= 0:
      soma_atual += num_lido 
    numeros_lidos += 1


print('A soma dos numeros é: %.0f' % soma_atual)
