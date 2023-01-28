#Criando XML a partir de um dicionario

import xml.etree.ElementTree as xml
import os

def criaTagPesoa(nome, cpf, sexo, endereco):
  no_pessoa = xml.Element('Pessoa', attrib={'Nome': nome})
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf

  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_sexo.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereco')
  no_endereco.text = endereco

  return no_pessoa

dados = {
      'Alice':{
        'CPF':'12345678-33',
        'Sexo': 'Feminino',
        'Idade': 38,
        'Endereco':'Caso 245',
        

      },
       'Sivaldo':{
        'CPF':'987564321-99',
        'Sexo': 'Masculino',
        'Idade': 22,
        'Endereco':'Rua 33',
        'Filhos': ['rodrigo', 'lucas']
        

      },
      'Lucas':{
        'CPF':'12345678-33',
        'Sexo': 'Masculino',
        'Idade': 22,
        'Endereco':'Casa 34',
         }
}

raiz = xml.Element('DadosPesoais')

for Key in dados:
  nome = Key
  dados_pessoa = dados[nome]
  cpf = dados_pessoa['CPF']
  sexo = dados_pessoa['Sexo']
  endereco = dados_pessoa['Endereco']
  #idade = dados_pessoa['Idade']
  pessoa = criaTagPesoa(nome, cpf,sexo,endereco)
  if 'filhos' in dados_pessoa:
    filho = xml.SubElement(pessoa, 'filhos')
    for filhos in dados_pessoa['filhos']:
      pessoa_filho = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
  raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais_3.xml', 'wb') as files:
  arvore.write(files)