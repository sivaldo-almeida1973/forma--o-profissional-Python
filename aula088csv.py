#Arquivos CSV
import csv
with open('pessoas.csv', 'w') as arquivo:#crair e salvar 
  escritorCsv = csv.writer(arquivo, delimiter=',')#permiter criar arq
  escritorCsv.writerow(['id', 'nome', 'profissao'])
  escritorCsv.writerow(['1', 'Lucas', 'Advogado'])
  escritorCsv.writerow(['2', 'Alice', 'eng. software'])
  escritorCsv.writerow(['3', 'Sivaldo', 'eng software'])
  escritorCsv.writerow(['4', 'Gute', 'empresario'])


#listas
import csv
lista= [
        ['id', 'nome', 'profissao'],['1', 'Lucas', 'Advogado'],
           ['2', 'Alice', 'eng. software'],['3', 'Sivaldo', 'eng software']

  ]
with open('pessoa2.csv', 'w') as file:
  escritorCsv = csv.writer(file)
  escritorCsv.writerows(lista)


  #ler arquivo csv.
import csv
with open('pessoas.csv', 'r')as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
   print(lista)




