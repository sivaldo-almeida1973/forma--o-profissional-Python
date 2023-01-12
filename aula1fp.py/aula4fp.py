"""
Formatação
# %s texto
# %d inteiro
# %f real
"""
#nome = 'Alice'
#texto_form = 'O nome dela é %s ' % (nome)
#print(texto_form)

nome = 'Alice'
idade = 22
altura = 1.70
texto = 'meu nome é %s tenho %d e tenho %.2f  metros de latura ' % (nome,idade, altura, )
print(texto)

valor = False
print('o valor é %s' %(valor))
print('o valor é %d' %(valor))

decimal = 23.44556
print('a parte inteira é %d' %(decimal))

texto = 'Olá , asim se quebra a linha ,\n\t entendeu como quebra a linha?\n\t\t fim.'
print(texto)


texto = 'deixa a palavra "entre" aspas'
print(texto)
