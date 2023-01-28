#transformar em uma função
import xml.etree.ElementTree as xml
import os

def criaTagpessoa(nome,cpf,sexo,endereco):
#tira no_raiz e criar fução generica
  no_pessoa = xml.Element('Pessoa', attrib={'Nome': nome})#troca por parametro (nome)
  no_cpf = xml.SubElement(no_pessoa, 'CPF')
  no_cpf.text = cpf#troca num de cpf por paramt (CPF)

  no_sexo = xml.SubElement(no_pessoa, 'Sexo')
  no_sexo.text = sexo #troca palavra masculino por (sexo)

  no_end = xml.SubElement(no_pessoa, 'Endereco')
  no_end.text = endereco #trocou rua brasil por endereco

  return no_pessoa
#criar elemeto raiz
raiz = xml.Element('DadosPessoais')

pesso1 = criaTagpessoa('Lucas', '123123112','Masculino','Rua brasil')
pesso2 = criaTagpessoa('sivaldo', '999888998','Masculino','Rua brasil')
pesso3 = criaTagpessoa('alice', '100100100100','Feminino','Rua brasil')
#adicionar ao elemento raiz
raiz.append(pesso1)
raiz.append(pesso2)
raiz.append(pesso3)
#agora cria a arvore
arvore = xml.ElementTree(raiz)
#salvar em disco
with open('dados_exemplo2.xml','wb') as files:
  arvore.write(files)
