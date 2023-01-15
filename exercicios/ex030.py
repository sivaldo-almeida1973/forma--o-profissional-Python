texto = input('Digite um texto:')
num_caracteres = 0

for letra in texto:
    if (letra != ' '):
        num_caracteres += 1

print('tem %d caracteres  no texto:' % (num_caracteres))