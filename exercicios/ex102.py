#faça uma expressão regular para detectar telefones que comecem com 95.
#telefones que começam com 95 devem ser bloqueados.Um numero de telefone
#deve ser valido para poder ser validado, na forma xxxxxxxxxxx onde X é
#um numero .Primeiro diga se é um numero valido.
#Caso seja diga se ele foi bloquado ou não.

import re
texto = '94234567'

info = re.search('^([0-9]{8})$', texto)

if info != None:
  print('Numero valido')
  info2 = re.search('^95([0-9]{6})#', texto)
  if info2 != None:
    print('Telefone bolquado')
  else:
    print('telefone não bolquado')
else:
  print('Numero invalido')