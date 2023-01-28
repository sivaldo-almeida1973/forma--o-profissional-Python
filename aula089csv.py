import csv
class Pessoa:
  def __init__(self, id, nome, profissao):
    self.id = id
    self.nome = nome
    self.profissao = profissao

  @staticmethod
  def le_pessoas():
    pessoas = [] #listas
    with open('pessoas.csv', 'r') as arquivo:#abre arquivo
      leitor = csv.reader(arquivo, delimiter=',')#cria obj
      for linha in leitor:#percorrer linhas
        pessoa = Pessoa(linha[0], linha[1], linha[2])
        pessoas.append(pessoa)
    return pessoas
  
  @staticmethod
  def salva_pessoas(*pessoas):
    with open('pessoas.csv', 'w') as arquivo:
      escritorCsv = csv.writer(arquivo, delimiter=',')
      for pessoa in pessoas:
       escritorCsv.writerow([pessoa.id, pessoa.nome,pessoa.profissao])

pessoa1 = Pessoa(22,'lucas', 'advogado')
pessoa2 = Pessoa(18,'Alice', 'eng')
pessoa3 = Pessoa(22,'Sivaldo', 'eng')

pessoa1.salva_pessoas()
pessoa2.salva_pessoas()
pessoa3.salva_pessoas()

lista_pessoa = Pessoa.le_pessoas()

for pessoa in lista_pessoa:
  print(pessoa.id, pessoa.nome,pessoa.profissao)




