#arquivos Csv(formato universal)biblioteca CSV estutrurado 2 colunas
import csv 
with open('pessoas.csv','w') as arquivo: #with open (abrir arquivo)
  escritorCsv = csv.writer(arquivo, delimiter=',')#objeto vai permitir criar arq
  escritorCsv.writerow(['id ','nome ','profissão'])# com escrever as linhas csv
  escritorCsv.writerow(['1 ','Lucas ','advogado']) # metodo writerow(escrever)
  escritorCsv.writerow(['2 ','Alice ','Eng. software'])
  escritorCsv.writerow(['3 ','Sivaldo ','Eng. software'])
  escritorCsv.writerow(['4 ','Gute ','empresario'])


#como criar arquivos csv apartir de uma lista
import csv 
linhas = [  ['id ','nome ','profissão'],['1 ','Lucas ','advogado'] ,
            ['2 ','Alice ','Eng.software'],['3 ','Sivaldo ','Eng.software']
          ]
with open('pessoas.2.csv','w')as file:
  escritorCsv = csv.writer(file)# writer (leitora)
  escritorCsv.writerows(linhas)#ler varias writerows(linhas gravação)

#como ler arquivos csv
import csv
with open('pessoas.csv','r')as arquivo: #open(abrir)
  leitor = csv.reader(arquivo, delimiter=',')#ler arquivo(header)
  for linha in leitor:
   print(linha)