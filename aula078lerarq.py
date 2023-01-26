#lendo Arquivos

with open('exemplo_with.txt', 'wt') as arquivo:# abertura /variavel e parametros
   arquivo.write('Olá  estou escrevendo no arquivo\n')#escrevendo no arquivo
   arquivo.write('Esta , é a segunda linha do arquivo')

#fazendo leitura do arquivo inteiro
arquivo = open('exemplo.txt', 'rt')
lido = arquivo.read()#lendo arquivo
print(lido)
arquivo.close()# fechar arquico


print('-'*30)
#fazendo leitura do arquivo por partes
arquivo = open('exemplo.txt', 'rt')
lido = arquivo.read(10)#lendo arquivo ate o 10 caracter
print(lido)
arquivo.close()# fechar arquico

print('-'*30)
#lendo linha por linha
arquivo = open('exemplo.txt', 'rt')
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()

print(primeira_linha)
print(segunda_linha)

arquivo.close()

print('-'*30)
#ler arquivo usando o for
arquivo = open('exemplo.txt', 'rt')
for linha in arquivo:
  print(linha)

arquivo.close()


print('-'*30)
#ler arquivo usando o for com with
with open('exemplo.txt', 'rt') as arquivo:
 for linha in arquivo:
  print(linha)