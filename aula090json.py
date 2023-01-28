#json usando dicionarios pode transformar funcoes de  python em objeto json

import json
idades = {
  'rogerio': 20,
  'maria': 33,
  'pedro':45
}
print(json.dumps(idades))
print(json.dumps(23))
print(json.dumps(23.4))
print(json.dumps([1,2,3,4,5]))
print(json.dumps(True))
print(json.dumps(None))

#vamos criar um arquivo Json mas elaborado,transfo, salvar

import json
DadosPessoas = {
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
#transf esse dicionario de cima em obj json usando(dumps)mettodo
texto = json.dumps(DadosPessoas, indent=4)
print(texto)
#salvar esse json
with open('exemplo.json', 'wt')as arquivo:
  arquivo.write(texto)





#como ler arquivo json
dicionario = None
with open('exemplo.json','rt') as arquivo:
  arquivo_lido = arquivo.read()
  dicionario = json.loads(arquivo_lido)

print(dicionario)
print(type(dicionario))
print(dicionario['sivaldo']['Idade'])