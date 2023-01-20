def e_maiuscula_ou_minuscula(texto):
    return texto.islower() or texto.isupper()

print(e_maiuscula_ou_minuscula('AAAAAAAA'))
print(e_maiuscula_ou_minuscula('AAaaaaaa'))
print(e_maiuscula_ou_minuscula('aaaaaaaaa'))

print('-'*30)
