#crie uma func que receba uma lista de frases e junte as #mesmas em uma só, separadas por ponto final.

def frase (lista):
  return '.'.join(lista) + '.'

textos = ['ola, sou sivaldo','gostode python','trabalho como dev']
print(frase(textos))
