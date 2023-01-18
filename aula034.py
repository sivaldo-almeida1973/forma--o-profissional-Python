#funções com retorno de valores

def subtrai(num1,num2):
    valor = num1 - num2
    return valor

subtracao = subtrai(10,3)
print(subtracao)

print('-'*20)
def subtrai(num1,num2):
    valor = num1 * num2
    return valor

multip = subtrai(10,3)
print(multip)

print('-'*20)

#tamanho de textos
def len_int(numero):
    numero_em_texto = str(numero)#converte numero em texto
    return len(numero_em_texto)

num1 = '10' #textar a função
num2 = 1230

tamanho1 = len_int(num1) # variavel para receber
tamanho2 = len_int(num2) # variavel para receber

print('O numero %s tem %d digitos '% (num1,tamanho1))
print('O numero %d tem %d digitos'% (num2,tamanho2))

print('-'*20)
def retorna_multiplo():
    return 1,2

valor = retorna_multiplo()
print(valor)
print(type(valor))

print('-'*20)

def retorna_multiplo(a,b,c):
    a += a
    b += b
    c += c
    return a,b,c

x,y,z = retorna_multiplo(1,2,3)
print(x,y,z)
a = retorna_multiplo(1,2,3)
print(a)


print('-'*20)

def func():
    print('olá')
    return
    print('123')

func()#chamar função


print('-'*20)

def func(x):
    if x == 'olá':
     print('olá')
     return
    print('123')
    return x

print(func('x'))#chamar função

