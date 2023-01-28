#usando classes
import json

class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia

  @staticmethod
  def salva_carros(*carros):
    dicionario = dict()
    for carro in carros:
      dicionario[carro.nome] = carro.potencia
    texto = json.dumps(dicionario, indent=4)
    with open('carros.json', 'w')as arquivo:
      arquivo.write(texto)
  @staticmethod
  def le_carros():
    lista = []
    texto = None
    with open('carros.json', 'r') as arquivo:
     texto = arquivo.read()
    dicionario = json.loads(texto)
    for chave in dicionario:
      carro = Carro(chave, dicionario[chave])
      lista.append(carro)
    return lista

carro1 = Carro('fusca', 40)
carro2 = Carro('focus', 290)
carro3  = Carro('golf', 300)

Carro.salva_carros(carro1, carro2, carro3)
lista_carros = Carro.le_carros()

for carro in lista_carros:
  print(carro.nome, carro.potencia)



  
