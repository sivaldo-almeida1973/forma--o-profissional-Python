#como coverter um list do tipo (dictionaries.)
#para uma lista do tipo (tupla) 
#lembrando que tupla é imutável

idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
lista = idades.items()#criando lista que recebe (tupla)idades
print(lista, end='\n\n')# \n\n quebra linha
print('-'*20)
for item in lista:#percorrer itens
    print(item[0], item[1])

print('-'*20)


idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
chaves = idades.keys()#acessar chaves
valores = idades.values()#acessar valores
for item in chaves:
    print(item)
print('-'*20)
for item in valores:
    print(item)

#achar quantas pessoas tem 20 anos
print('-'*20)
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':20}
lista_nome = list(idades.values())
pessoas_com_20_anos = lista_nome.count(20)
print(pessoas_com_20_anos)

print('-'*20)
#limpar lista
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':20}
idades.clear()
print(idades)

print('-'*20)
#dicionários aninhados(dentro de outro)
dados_maria = {
    'sexo':'feminino',
    'cpf': '123.123.123.44',
    'Rg': '23456345'
}
dados_lucas = {
    'sexo':'Masculino',
    'cpf': '155.123.123.88',
    'Rg': '33456389'
}
dados_Alice = {
    'sexo':'feminino',
    'cpf': '144.123.123.44',
    'Rg': '38456345'
}

dados_po_nome ={
  "maria":  dados_maria,
  'lucas':  dados_lucas,
  'Alice':  dados_Alice
}
print(dados_po_nome['lucas']['sexo'])
print(dados_po_nome['lucas']['cpf'])

