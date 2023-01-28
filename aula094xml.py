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
  'lucas':{
    'CPF': '12312312311',
    'Sexo': 'Masculino',
  'Endereco':'Rua Brasil',
  'Idade': 22
  },
  'sivaldo':{
    'CPF': '99876588900',
    'Sexo': 'Masculino',
  'Endereco':'Rua Brasil',
  'Idade': 43
  },
  
  'Alice':{
    'CPF': '777655444333',
    'Sexo': 'Feminino',
  'Endereco':'Rua Brasil',
  'Idade': 43,
  'filhos': ['lucas']
  }
  
}

raiz = xml.Element('dadosPessoais')

for Key in dados:
  nome = Key
  dados_pessoa = dados[nome]
  cpf = dados_pessoa['CPF']
  sexo = dados_pessoa['Sexo']
  endereco = dados_pessoa['Endereco']
  #idade = dados_pessoa['Idade']
  pessoa = criaTagPesoa(nome, cpf, sexo, endereco)
  if 'filhos' in dados_pessoa:
    filhos = xml.SubElement(pessoa, 'filhos')
    for filho in dados_pessoa['filhos']:
      pessoa_filhos = xml.SubElement(filhos, 'Pessoa', attrib={'nome': filho})
  raiz.append(pessoa)

arvore = xml.ElementTree(raiz)
with open('dados_pessoais_4.xml', 'wb')as files:
  arvore.write(files)

