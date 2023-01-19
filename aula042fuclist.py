#funcões em listas


#listas ordenadas
lista = [1,29,3,4,6,12,20,30,25]
lista.sort()
print(lista)


print('-'*20)
lista = ['a','ab', 'b', 'd','f']
lista.sort()
print(lista)


print('-'*20)
#listas reversa (decrescente)
lista = [1,29,3,4,6,12,20,30,25]
lista.sort(reverse=True)
print(lista)

print('-'*20)
#ordena a lista por tamanho
def sort_por_tamanho (item):
    return len(item)

lista = ['abcde','a','b','ab', 'abc','abcd']
lista.sort(key=sort_por_tamanho)
print(lista)

#inverter uma lista ou texto
lista = [1,2,3,4,5,6,7,8]
lista.reverse()
print(lista)

lista = ['o Brasil esta quente', 'O PARÀ esta frio']
lista.reverse()
print(lista)

print('-'*20)
produtos = [
    ['carro','R$ 100.000'  ],
    ['Geladeira','R$ 1.000'],
    ['Moto','R$ 10.000'    ],
    ['TV','R$ 1.000'       ],
    ['Desktop','R$ 2.000'  ],
    ['Bicicleta','R$ 3.000']
    ]
for produto, valor in produtos:
    print(produto, valor)
    
#criar um dicionario  e acrescentar chave  10 a ele 
print('-'*20)
nomes = ('Guti', 'Lucas','Sivaldo','Alice')
dicionario = dict.fromkeys(nomes,10)
print(dicionario)


