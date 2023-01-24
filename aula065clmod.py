#Como acessar a documentação de uma função

import sys
print(sys.__doc__)

print(print.__doc__)


print('-'*50)
#para criar uma doc de uma função

'''
este é o arquivo principal contendo uma variavel chamada euler e uma função chamada soma
'''
euler = 2.71828
def soma(num1,num2):
    '''função que soma dois numeros recebidos por uma entrada'''
    return num1 + num2
    '''função que soma dois numeros recebidos por uma entrada'''

print(__doc__) #doc especifica de modulo
print(soma.__doc__) #doc da função


print('-'*50)
def soma(num1,num2):
    '''função que soma dois numeros recebidos por uma entrada'''
    return num1 + num2
help(soma)

print('-'*50)

import teste

print(teste.__doc__)
print(teste.Teste.__doc__)
print(teste.MyFunc.__doc__)
help(teste)