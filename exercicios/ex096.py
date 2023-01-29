#crie uma classe que represnte uma pessoa , com nome ie idade.
#Após criar pelo menos 3 instancias da classe, crie um metodo
#que transforme essas instancias em um dicionario,para poder #salva-la em um arquivo em formato Json,com nome de 'exercicio7.#json'.Este método deve ser um tipo estatico da classe.Leia o #arquivo depois de salvo.
import json
class Pessoa:#cria classe pessoa
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
#cirar metodo estatico para salvar
  @staticmethod
  def transforma_dict(*args):#recebe multiplos argumentos
    dicionario = dict() #criar dicionario vazio
    for pessoa in args: #percorrer metodo
      dicionario[pessoa.nome] = pessoa.idade #chave e valor
    return dicionario 
#criar 3 instancias
pessoa1 = Pessoa('Lucas',22)
pessoa2 = Pessoa('Alice',33)
pessoa3 = Pessoa('Sivaldo',42)
#chamar o met transf dict (chama pela classe)
dictionario_pessoas = Pessoa.transforma_dict(pessoa1,pessoa2,pessoa3)
#transformar o dicionario em Json
texto = json.dumps(dictionario_pessoas, indent=4)
print(texto)
#salvar em disco
with open('exercicio7.json','wt')as arquivo:
  arquivo.write(texto)
