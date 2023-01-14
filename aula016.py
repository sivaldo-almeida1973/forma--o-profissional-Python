#continuação de While
soma = 0
numeros_lidos = 0

while (numeros_lidos < 5):# quantas vezes vai repetir
    num_str = input('Digite um valor:' )
    num_lido = float(num_str)#Mudar a string em float
    soma += num_lido# numero digitado 
    numeros_lidos += 1 # faz o while parar

print('Soma é %.2f' % soma)