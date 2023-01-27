#usando um dicionario

import json
idades ={
  'Rogério': 20,
  'Maria': 43,
  'lucas': 22

}

print(json.dumps(idades, ensure_ascii=False))
print(json.dumps(23))
print(json.dumps(3.14))
print(json.dumps([1,2,3,4,5]))
print(json.dumps(True))
print(json.dumps(None))

#um pouco mais eleborado
import json
DadosPessoa = {
      'Alice':{
        'CPF':'12345678-33',
        'sexo': 'Feminino',
        'Idade': 38,
        'Endereço':'Caso 245',
        

      },
       'Sivaldo':{
        'CPF':'987564321-99',
        'sexo': 'Masculino',
        'Idade': 22,
        'Endereço':'Rua 33',
        'Filhos': ['rodrigo', 'lucas']
        

      }
}

texto = json.dumps(DadosPessoa, indent=4)
print(texto)

with open('exemplo.json','wt') as arquivo:#salvar arquivo
  arquivo.write(texto)


import json
dicionario = None
with open('exemplo.json', 'rt') as arquivo:
  arquivo_lido = arquivo.read()
  dicionario = json.loads(arquivo_lido)

print(dicionario)
print(type(dicionario))
print(dicionario['Sivaldo'] ['Idade'])