#Slicing(fatiamento)

var = 'exemplo'
var[3]
print(var[:5])

#Operadores sobre Strings

texto1 = 'Olá'
texto2 = ', '
texto3 = 'mundo!'
texto_completo = texto1 + texto2 + texto3 #concatenação
print(texto_completo)
print('-'*20)

texto1 = 'Olá ,'
texto1 += 'mundo!'
print(texto1)
print('-'*20)

texto = 'python é bem produtivo,'
texto_repetido = texto * 3
print(texto_repetido)
print('-'*20)
texto = 'exemplo'
print(texto[0])
print(texto[5])
print(texto[1:4])
print(texto[1:])
print(texto[:])
print(texto[:-1])
print(texto[-1])
print(texto[-1])
print(texto[-4:])

print('-'*20)

texto ='Eralice'#invertido
print(texto[::-1])
print(texto[3::-1])


print('-'*20)

texto = '023'
texto2 = '1' + texto[1:]#incluir outro numero
print(texto2)

print('-'*20)
texto = 'abcdefg'
texto = texto[:3] + texto[:4]
print(texto)

text1 = 'Olá'
texto2 = 'Olá'
igual = text1 == texto2
print('textos são iguais ?', igual)

print('-'*20)

print('a' != 'b')
print('-'*20)
texto = ' programação '
print('a' in texto)
print('a' in texto)
print('proggram' in texto)
print('program' not in texto)
print('a' in texto)
print('vinte' not in texto)

#tamanho do texto (len)
print('-'*20)

brasil = len(texto)
print(brasil)

print('-'*20)

