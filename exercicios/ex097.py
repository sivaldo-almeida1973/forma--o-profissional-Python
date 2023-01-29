#Com base no exercicio anterior, agora crie uma função do tipo #da classe que leia o arquivo gerado e retorne as instancias
#de classes de volta em lista.
import json
class Pessoa:#cria classe pessoa
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @staticmethod #criar met est
  def transforma_para_pessoa():
    pessoas = [] #lista vazia
    with open('exercicio7.json', 'rt')as arquivo:#abrir arquivo
      arquivo_lido = arquivo.read() #ler arquivo que ja existe
      dicionario = json.loads(arquivo_lido)#transf em dicion
      for key in dicionario: # interar
        pessoa = Pessoa(key, dicionario[key])#intanciar
        pessoas.append(pessoa)#adicionar a lista
    return pessoas 
#criar objeto pess
pess = Pessoa.transforma_para_pessoa()
#percorrer
for pessoa in pess:
  print(pessoa.nome, pessoa.idade)


