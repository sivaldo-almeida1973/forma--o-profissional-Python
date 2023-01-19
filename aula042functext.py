#funções de textos
# deixar 1º letra do texto maiusculas
texto = 'olá, tudo bem?'
print(texto.capitalize())

texto = 'isto é estranho'
print(texto.lower())#minusculo
print(texto.upper())#maiusculo
print(texto.swapcase())#deixa invertido 

#formatação de titulo
# deixa 1ªletra de cada palavra maiuscula.
texto = "deixa 1ª letra de cada palavra maiuscula"
print(texto.title())

#centralizar texto
texto = "centralizar texto"
print(texto.center(30))

#justificar texto (direita / rjust)(esquerda /l just)
texto = "centralizar texto"
print(texto.rjust(30))# rjust
print(texto.ljust(30)) # ljust

#contagem de texto
texto = 'flamengoflamengoflamengo'
print(texto.count('flamengo'))

#perguntar de começa ou termina de determinada maneira
texto = 'flamengo'
print(texto.startswith('fla'))#se começa por fla
print(texto.endswith('engo'))#se termina em engo

print('-'*20)
# como localizar a posiçao onde cpmeça a palavra 
texto = 'flamengo o malvadão do brasil '
pos = texto.find('mal')
print(pos)
pos = texto.find('brasil')
print(pos)

print('-'*20)
# como localizar a posiçao onde cpmeça a palavra 
texto = 'flamengo o malvadão do brasil '
pos = texto.index('mal')
print(pos)
pos = texto.index('brasil')
print(pos)

print('-'*20)
#como fazer substituição de texto
texto = 'flamengo melhor do brasil'
novo_texto = texto.replace('melhor', 'malvadão')
print(novo_texto)

print('-'*20)
#criar uma lista onde esta a virgula
texto = 'flamengo, melhor ,do brasil'
print(texto.split(','))

#cria lista onde tem quebra de linha
print('-'*20)
texto = 'flamengo\n melhor \n do brasil'
print(texto.splitlines())#onde tem quebra de linha

#se texto é alfanumerico
print('abcd'.isalpha())

print('-'*20)
#se texto é alfanumerico
print('abc,d3'.isalnum())
print('abcd'.isalnum())

print('-'*20)
#se texto é composto só por numeros
print('123456'.isdecimal())

print('-'*20)
#se texto esta em branco
print('1234'.isspace())
print('   '.isspace())


print('-'*20)
#se texto é todo maiuc. o minusc
print('abce'.islower())
print('ADDCCDS'.isupper())