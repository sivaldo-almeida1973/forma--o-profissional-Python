#search pode ser uasdo para buscar uma palavra interira
import re
texto = 'existem 64 predios com 700 metros'
info = re.search('predios', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

print('-'*30)
#buscar reconhecimento de um determinado grupo da caracter.
import re
texto = 'ABCDefgHI123'

#[] => escontra um conj de caracter
info1 = re.findall('[Ae3]',texto)
info2 = re.findall('[A-Z]',texto)
info3 = re.findall('[a-z]',texto)
info4 = re.findall('[0-9]',texto)
info5 = re.findall('[A-za-z]',texto)
print(info1)
print(info2)
print(info3)
print(info4)
print(info5)

print('-'*30)
#buscar ocorrencia de mais de um texto
#| equivale => or
import re
texto = 'existem 64 predios com 700 metros'
info = re.findall('predios|metros', texto)#ou um ou outro
print(info)

print('-'*30)
#diferentes comjuntos de caracter
import re
texto = 'ABCDefgHI123'
info = re.findall('[A-Z]|[0-9]', texto)
print(info)

print('-'*30)
#Buscar padrão no inicio (^existem) (metros$)no final
import re
texto = 'existem 64 predios com 700 metros'
info = re.search('^existem', texto)#(^existem)no inicio
if info != None:
  print('encontrado ocorrencia em: ', info.span())
  print('encontrado ocorrencia em: ', info.group())

#Buscar padrão no final (metros$)no final
print('-'*30)
import re
texto = 'não existem 64 predios com 700 metros'
info = re.search('metros$', texto)#(^existem)no inicio
if info != None:
  print('encontrado ocorrencia em: ', info.span())
  print('encontrado ocorrencia em: ', info.group())