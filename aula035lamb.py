#função lambda na pratica
faz_soma = lambda x : x + 10
valor = faz_soma(22)
print(valor)

print('-'*20)
multip = lambda x,y : x * y
valor = multip(20,10)
print(valor)

print('-'*20)

def multiplica(y):
    return lambda x : x * y

valor = multiplica(2)
resultado = valor(10)
print(resultado)
