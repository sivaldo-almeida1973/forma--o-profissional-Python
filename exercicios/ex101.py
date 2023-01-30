#faça uma expressão regular para validar se uma string dada #é um dia da semana. As possibilidades são
#Segunda feira
#Terça feira
#Quarta feira
#Quinta feira
#Sexta feira
#Sábado
#Domingo

import re
texto = 'Terça-feira'
info = re.search('^(Segunda-feira|Terça-feira|Quarta-feira|Quinta-feira|Sexta-feira|Sábado|Domingo)$', texto)
if info != None:
  print('Encontrado ocorrencia em', info.span())
  print('Dia encontrado', info.group())

else:
  print('Valor invalido')
