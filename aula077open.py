#arquivos(Open)
#'r' abre arquivo para leitura(se não existir gera erro)
#'a'abre arquivo para anexar (senão existir ,cria um)
#'w'abre arquivo para escrita(cria um se não existir)
#'x'cria um arquivo,mas se ja existir retorna um erro
# #segunda parte
#'t'abre arquivo em modo texto
#'b'abre um arquivo em modo binario
#Padrão é 'rt'
#operação basica de criar arquivo e salvar o texto


arquivo = open('exemplo.txt', 'wt') # abertura /variavel e parametros
arquivo.write('Olá , estou escrevendo no arquivo\n')#escrevendo no arquivo
arquivo.write('Esta , é a segunda linha do arquivo')#escrevendo no arquivo
arquivo.close()#fechar arquivo
print(arquivo) #executar

#Lista
lista = ['Ana', 'Lucas','Sivaldo', 'Alice']
arquivo = open('nomes.txt','wt') #abertura do arquivo
for i in lista: #percorrendo o arquivo
  arquivo.write(i +'\n')
arquivo.close() #executar

#texto
texto = 'Ana\nLucas\nSivaldo\nAlice'
arquivo = open('nomes2.txt','wt')
arquivo.writelines(texto)# ecrever de uma unica vez
arquivo.close()

#lista 
lista = [str(i) + '\n'for i  in range(0,20)]
arquivo = open('numeros_3.txt','wt')
arquivo.writelines(lista)
arquivo.close() #executar arquivo
