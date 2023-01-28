#transformar xml em função

import xml.etree.ElementTree as xml
import os

def criaTagPesoa(nome, cpf, sexo, endereco):
  no_pessoa = xml.Element('Pessoa', attrib={'Nome': 'Nome'})
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf


  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_cpf.text = sexo

  no_endereco = xml.SubElement(no_pessoa, 'Endereco')
  no_cpf.text = endereco

  return no_pessoa

raiz = xml.Element('DadosPessoais ')
pessoa1 = criaTagPesoa('Lucas', '123334556778', 'Masculino', 'Rua brasilia')
pessoa2 = criaTagPesoa('Sivaldo', '123334556778', 'Masculino', 'Rua brasilia')
pessoa3 = criaTagPesoa('Alice', '123334556778', 'Feminino', 'Rua brasilia')
pessoa4 = criaTagPesoa('Gute', '123334556778', 'Masculino', 'Rua brasilia')

raiz.append(pessoa1)
raiz.append(pessoa2)
raiz.append(pessoa3)
raiz.append(pessoa4)

arvore = xml.ElementTree(raiz)

with open('dados_exemplo2.xml','wb') as files:
  arvore.write(files)