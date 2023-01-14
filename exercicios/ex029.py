"""
Crie um programa que receba como input uma 
string:
em seguida percorra a string e diga quantos 
espaços em branco esta string tem.
"""

texto = input('digite uma palavra:')
indice = 0
num_vazio = 0

while(indice < len(texto)):
    if texto[indice] == " ":
        num_vazio += 1
    indice += 1

print('numero de espaços no texto é de %d' % num_vazio )

