#Mais padrões
#todas as ococrrencias de determinada ('(abb)+',texto)
import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb)+', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

print('-'*30)
#encontrar numero exato de ocorrencias
import re
texto = 'aabbaabbbbbbaaccaa'
info = re.search('(aa|bb){2}', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

#nenhuma ou n ocorrencias

print('-'*30)
#encontrar numero exato de ocorrencias
import re
texto = 'bba'
info = re.search('(aa|bb)*', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

print('-'*30)
#^(aa)?$  encontrar 0 ou mais de ocorrencias de um padrão
import re
texto = 'aa'
info = re.search('^(aa)?$', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')



print('-'*30)
#definir intervalo de ocorrencias
import re
texto = 'aaaaaa'
info = re.search('^(aa){2,3}$', texto)# 2ou 3 ocorrencias
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')


#Até 7 letras de um det padrão 
#^x{,7}$ ou menos
print('-'*30)

import re
texto = 'xxxxxxx'
info = re.search('^x{,7}$', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

# 7 ou mais letras de um det padrão 
#^x{7,}$ ou mais
print('-'*30)

import re
texto = 'xxxxxxxx'
info = re.search('^x{7,}$', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

#encontrar um padrao no meio de um texto

import re
texto = 'Olá sou eu , AQUI, e nada para frente'
info = re.search('(.)*(AQUI)(.)*', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')


