
import csv
class Pessoa:
  def __init__(self,id, nome, profissao):#const da classe
    self.id = id #variaveis privadas
    self.nome = nome
    self.profissao = profissao
  
  @staticmethod #criar metodo estatico
  def le_pessoas(): #classe pessoa
    pessoas = [] #inicializa lista vazia
    with open('pessoas.csv', 'r') as arquivo:#abre arquivo 
      leitor = csv.reader(arquivo, delimiter=',')#leitor
      for linha in leitor: #percorre as linhas do leitor
        pessoa = Pessoa(linha[0],linha[1],linha[2])
        pessoas.append(pessoa)
    return pessoas

  @staticmethod
  def salva_pessoas(*pessoas):#salvar varias inst de do bojeto
    with open('pessoas.csv', 'w') as arquivo:
      escritorCsv = csv.writer(arquivo, delimiter=',') 
      for pessoa in pessoas:
        escritorCsv.writerow([pessoa.id,pessoa.nome,pessoa.profissao])

pessoa1 = Pessoa(23,'Lucas','advogado')
pessoa2 = Pessoa(38,'Sivaldo','engenheiro')
pessoa3 = Pessoa(38,'Alice','engenheira')

Pessoa.salva_pessoas(pessoa1, pessoa2, pessoa3)

lista_pessoa = Pessoa.le_pessoas()

for pessoa in lista_pessoa:
 print(pessoa.id, pessoa.nome, pessoa.profissao)

  
