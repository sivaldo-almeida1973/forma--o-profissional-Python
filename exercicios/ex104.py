#faça uma expressão reg para detectar se a hora é valida:
#o formato é 24 horas, e é especificado da seguinte #forma:HH :MM
#Ex:19:30 ,09:30, 23:45, 23:70 (invalido)

import re 
texto = '00:59'

info = re.search('^([0-1][0-9]|[2][0-3]):[0-5][0-9]$', texto)

if info != None:
  print('Horario valido')
else:
  print('Horario invalido')
