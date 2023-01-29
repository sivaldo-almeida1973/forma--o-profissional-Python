if info != None:
  print('Encontrada ocorrencia em', info.span())
  print('O que foi encontrado ', info.group())


print('-'*30)
#podemos usar o (s\)para não ocorrencia espaços em branco
texto ='01234 ABC'
info = re.search('\S', texto)

if info != None:
  print('Encontrada ocorrencia em', info.span())
  print('O que foi encontrado ', info.group())


print('-'*30)
#alfanumericos de A a Z \w de qualquer texto
texto ='01234 ABC'
info = re.search('\w', texto)

if info != None:
  print('Encontrada ocorrencia em', info.span())
  print('O que foi encontrado ', info.group())

print('-'*30)
#a ausencia alfanumericos de A a Z \W de qualquer texto
texto ='01234 ABC'
info = re.search('\W', texto)

if info != None:
  print('Encontrada ocorrencia em', info.span())
  print('O que foi encontrado ', info.group())

