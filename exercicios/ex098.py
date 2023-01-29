#crie um arquivo XMl, nesse arquivo haverá a tag raiz Root.
#dentro dessa raiz podera haver varias tags Esyado com o #atributo nome.Dentro de cada estado pode haver a tag Cidade #mas nesse caso o valor da tag(texto)deverá sr o nome da cidade
#crie um programa que gere esse arquivo com alguns estados e #municipios.

import xml.etree.ElementTree as xml
import os

def cria_estado(nome, cidades):
  element_estado = xml.Element('Estado',attrib={'nome':nome})
  for cidade in cidades:
    elemento_cidade = xml.SubElement(element_estado, 'Cidade')
    elemento_cidade.text = cidade
  return element_estado

raiz = xml.Element('Root')
no_estado1 = cria_estado('Rio de Janeiro', ['Macaé','Rio de janeiro', 'Volta Redonda'])
no_estado2 = cria_estado('São Paulo', ['Santo Andre','São Caetano', 'Santos'])
raiz.append(no_estado1)
raiz.append(no_estado2)

arvore = xml.ElementTree(raiz)

with open('exercicio9.xml','wb') as files:
  arvore.write(files)
