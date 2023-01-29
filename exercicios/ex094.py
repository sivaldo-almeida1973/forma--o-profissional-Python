#Crie um arquivo CSV separado por vigula para guardar inform
#de sua familia.Neste deve constar em cada linha o nome de um
#membro da familia e o grau de parentesco(EX: pai).Escreva 5
#membros da familia no arquivo.Faça uma função que ira escrevar 
# #no arquivo e outro que ira ler o arquivo.

import csv

def escreve_arquivo():#criar função 
  with open('exercicios5.csv', 'w')as arquivo:# abrir arquivo pra escrita
    escritorCSV = csv.writer(arquivo, delimiter=',')#instanciar elemeto CSV(variavel)
    escritorCSV.writerow(['Nome','Parentesco'])
    escritorCSV.writerow(['Antonio','vô'])
    escritorCSV.writerow(['Lucas','filho'])
    escritorCSV.writerow(['Alice','esposa'])
    escritorCSV.writerow(['Sivaldo','marido'])
    escritorCSV.writerow(['Maria','vó'])
#ler o arquivo
def Le_arquivo():
  with open('exercicios5.csv', 'r')as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linha in leitor:
      print(linha)
#chamar arquivo
escreve_arquivo()
Le_arquivo()

