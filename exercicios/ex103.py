#faça uma expressão regular para reconhecer palavrados no gerundio.
#Normalmente essas palavras podem ser detectadas caso elas terminam com ando,
#sendo, indo: Exmplo: sorrindo , andando.usa a função 'find all'
# para retornar as ocorrencias.

import re
texto = 'Olá, eu estou sonhando,lendo, e não dormindo'
info = re.findall('([\w]+indo|[\w]+ando|[\w]+endo)+', texto)
print(info)