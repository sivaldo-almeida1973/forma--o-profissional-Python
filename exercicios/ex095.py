#Faça um programa que leia um arquivo CSV separado por virgula
#'exercicio6.csv', onde cada lina tem os seguintes valores
#(id_empresa,nome_empresa, numero_funcionarios, lucro)
#modele uma classe empresa que será usada pra guardar os #valores do arquivo.Imprima o resultado
import csv
class Empresa:#criar classee
  def __init__(self, id, nome, numero_funcionarios, lucro):
    self.id = id
    self.nome = nome
    self.numero_funcionarios = numero_funcionarios
    self.lucro = lucro
#primeiro criar uma lista vazia
empresas = []
#ler arquivo

with open('exercicio6.csv','r') as arquivo:
  leitor = csv.reader(arquivo, delimiter=',')
  for linha in leitor:
    emp = Empresa(linha[0], linha[1], linha[2], linha[3])
    empresas.append(emp)

for emp in empresas:
  print(emp.id, emp.nome, emp.numero_funcionarios, emp.lucro)



