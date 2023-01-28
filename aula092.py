import xml.etree.ElementTree as xml
import os

no_raiz =  xml.Element('DadosPessoais')
no_pessoa = xml.Element('Pessoa', attrib={'Nome': 'Lucas'})
no_cpf = xml.SubElement(no_pessoa, 'CPF')
no_cpf.text = '123234345-99'

no_sexo = xml.SubElement(no_pessoa, 'Sexo')
no_sexo.text = 'Masculino'

no_end = xml.SubElement(no_pessoa, 'Endereco')
no_end.text = 'Rua brasil'
#juntar no_raiz ao no_pessoa
no_raiz.append(no_pessoa)
#agora transf em xml
arvore = xml.ElementTree(no_raiz)
#salvar em disco
with open('dados_exemplo.xml','wb') as files:
  arvore.write(files)
