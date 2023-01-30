#Faça uma expressão regular para reconhecer números de 20 até 35 apenas.
#O texto deve ser composto apenas destes numeros, nenhum outro caracter é #permitido

import re 
texto = '34'
info = re.search('^([2][0-9])|([3][0-5])$ ', texto)

if info != None:
  print('Encontrado ocorrencia em', info.span())
  print('Numero encontrado', info.group())
else:
  print('Valor invalido')