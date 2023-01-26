#arquivos Csv(formato universal)biblioteca CSV
import csv 
with open('pessoas.csv','w') as arquivo: #criar arquivo
  escritorCsv = csv.writer(arquivo, delimiter=',')#bojeto vai permitir criar arq
  escritorCsv.writerow(['id ','nome ','profissão'])# com escrever as linhas csv
  escritorCsv.writerow(['1 ','Lucas ','advogado'])
  escritorCsv.writerow(['2 ','Alice ','Eng. software'])
  escritorCsv.writerow(['3 ','Sivaldo ','Eng. software'])
  escritorCsv.writerow(['4 ','Gute ','empresario'])


#como criar arquivos csv
import csv 
linhas = [  ['id ','nome ','profissão'] , ['1 ','Lucas ','advogado'] ,
            ['2 ','Alice ','Eng. software'],['3 ','Sivaldo ','Eng. software']
          ]

with open('pessoas.2.csv','w')as file:
  escritorCsv = csv.writer(file)
  escritorCsv.writerows(linhas)

#como ler arquivos csv
import csv
with open('pessoas.csv','r')as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
   print(linha)