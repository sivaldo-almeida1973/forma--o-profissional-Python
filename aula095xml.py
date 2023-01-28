
import xml.etree.ElementTree as xml
import os
class Carro:
  def __init__(self, nome, potencia):
    self.nome = nome
    self.potencia = potencia

  @staticmethod #metodo est para salvar xml
  def salva_carros(*carros):# instancia de carros
    raiz = xml.Element('Raiz') #elemento raiz

    for carro in carros:#percorrer carro
      no_carro = xml.Element('Carro')#criar elento carro
      no_nome = xml.SubElement(no_carro, 'Nome')#sub el nome
      no_nome.text = carro.nome #atribuir  valor para nome

      no_potencia = xml.SubElement(no_carro, 'Potencia') #sub el poten
      no_potencia.text = str(carro.potencia) #transforma em texto

      raiz.append(no_carro)
    arvore = xml.ElementTree(raiz) #adicionar no_carro a elem raiz
    with open('carros.exemplo.xml', 'wb') as files:# salvar
      arvore.write(files)

  @staticmethod  # metod estatico para ler carro
  def le_carros():
    lista = [] #cria lista vazia
    tree = xml.parse('carros_exemplo.xml') #leitura no arquivo xml
    root = tree.getroot() #elemento root
    for carro in root: #percorrer todos os element na raiz
      nome = None
      potencia = None
#atribuir valores para o no potencia
      for dado in carro: #para cada dado encontrado em carro
        if (dado.tag == 'Nome'):#procura tag Nome
          nome = dado.text  #atribuir texto a variavel nome
        if (dado.tag == 'Potencia'):#procura tag Potencia
          potencia = dado.text #atribuir texto a variavel Potencia
      carro = Carro(nome, potencia) #fazer inst da class Carro passando(nome ,potenc)
      lista.append(carro)
    return lista
#criar objetos do tipo carro
carro1 = Carro('maverik', 330)
carro2 = Carro('golf', 220)
carro3 = Carro('vectra', 200)
#salvar carros
Carro.salva_carros(carro1, carro2, carro3)

lista_carros = Carro.le_carros()

for carro in lista_carros:
  print(carro.nome,carro.potencia)




    