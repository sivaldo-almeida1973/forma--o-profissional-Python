#Verificando Existencia e tratamento de erros
from os import path
arquivo_existe = path.exists('exemplo.txt')#caminho relativo

if arquivo_existe: #teste logico
  print('O arquivo existe!')
else:
  print('O arquivo não existe!')

#para excluir arquivo
#import os 
#os.remove('exemplo.txt')

#Tratamento de exceções com (file)

file = open('teste','w')
try:
  file.write('hello world')#tentar gravar arquivo
finally: #vai acontercer o fechamento de qualquer maneira
  file.close()#fechar arquivo

#
import os
try:
  os.remove('encerrei.txt')
except Exception as error:
  print('ocorreu um erro:' + str(error))