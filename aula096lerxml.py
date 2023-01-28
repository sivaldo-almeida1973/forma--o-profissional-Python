import xml.etree.ElementTree as xml
tree = xml.parse('dados_pessoais_4.xml')#(parse)metodo
root = tree.getroot() #(root)metodo pra acessar raiz
print(root.tag)#imprimir raiz
for pessoa in root:#criar variavel pessoa
  print('  ' ,pessoa.tag, pessoa.attrib['Nome'])
  for dado in pessoa: #percorrer tag pessoa
    if (dado.tag == 'filhos'):#verificar se é filho
      for filho in dado: #percorrer filhos
        print('  ', filho.tag, filho.attrib['nome'])
    else:
      print(' ',dado.tag, dado.text)#vai imprimir todos os outros elementos
