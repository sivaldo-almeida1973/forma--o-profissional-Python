#se uma senha possui determinados caracteres obrigatorios
#se um dado é valido:email,data,hora etc
#se um texto possui uma determinda letraou palavra
#Extrair determinadas parte de um texto(por ex: CEP)
#substituir caracteres(% po %% em URLS)
#metodo (search) caracteristicas de procurar:
#span (posição inicial e final) e group(e o que foi encontrado)
import re
texto = '00123451'
info = re.search('1', texto)
if info != None:
  print('Encontrado ocorrencia em ',info.span())#(posição inicial e final)
  print('O que foi encontrado', info.group())#(e o que foi encontrado)
else:
  print('Nada foi encontrado!')

#se quiser encontrar todas as ocorrencias(findall)=encontrar tudo
print('-'*30)
import re
texto = '00123451'
info = re.findall('1', texto)#não mostra o indice
print(info)

#metodo split
print('-'*30)
import re
texto = '001234510'
info = re.split('1', texto)#não inclui o proprio caracter(em forma de lista)
print(info)

#metodo sub
print('-'*30)

import re
texto = '001234510'
info = re.sub('1','#', texto)#substitui o proprio caracter pelo elem escolhido
print(info)

