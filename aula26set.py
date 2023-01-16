#Set não pode ser alterado atraves do indice
#se declar set por chaves {} ou ({})
lista_set = {}
lista2_set = {1,2,3}
lista3_set = set({1,2,3})
print(lista_set)
print(lista2_set)
print(lista3_set)

print('-'*20)
#adicionar e remover valores
lista_set = {1,2,3,}
lista_set.add(5)#adiciona valor
print(lista_set)
lista_set.remove(1)#remove valor
print(lista_set)

print('-'*20)
#não permite duplicidade,ignora repetições.
lista_set = {1,2,3,3,3,3}
print(lista_set)

print('-'*20)
#limpar lista 
lista_set = {1,2,3,3,3,3}
lista_set.clear()
print(lista_set)

print('-'*20)
#contagem de itens
lista_set = {1,2,3,4,5}
print(len(lista_set))

#verifica se existe na lista
lista_set = {1,2,3,4,5}
print(6 in lista_set)

print('-'*20)
#percorrer lista com for
# true não aprarece por ter o mesmo valor do 1
# o mesmo acontece com 0 (0) e false
lista_set = {1,2,3,'4', True, 6.1}
for item in lista_set:
    print(item)

print('-'*20)
#podemos fazer junção(união) de sets
set1 = {1,2,3}
set2 = {1,2,3,4,5}
set_unido = set1.union(set2)
print(set_unido)

print('-'*20)
#interseção
set1 = {1,2,3}
set2 = {1,2,3,4,5}
set_inter = set1.intersection(set2)
print(set_inter)

print('-'*20)
#interseção
set1 = {1,2,3}
set2 = {1,2,3,4,5}
set_dife = set2.difference(set1)
print(set_dife)