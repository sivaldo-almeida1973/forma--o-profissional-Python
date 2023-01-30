#faça uma expressão regular para dizer se a palavra 'Python' está na frase.

import re
texto = 'Este notbook utiliza python'
info = re.search('python', texto)
if info != None:
  print('Encontrado ocorrencia em', info.span())
  print('', info.group())
