"""crie duas listas com os seguintes valores 30,4,43,
52,65,-10  e 43,2,4,76,32,65,3. Agora faça a junção 
delas listas.mas s houver valores repetidosdeixe fora
dalista unida.

"""
lista_set1 = {30,4,43,52,65,-10}
lista_set2 = {43,2,4,76,32,65,3}
novo_set = lista_set1.union(lista_set2)
print(novo_set)