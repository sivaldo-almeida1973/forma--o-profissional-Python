#Tuplas são lista que não podem modificadas .
# pode ter no mimino 2 elementos.
#uma vez declarada não pode ser alterada
# usa-se tuple(()) () duplos

doces = tuple(('chocolate', 'bom bom', 'paçoca'))
print(doces)

print('-'*20)
doces = ('chocolate', 'bom bom', 'paçoca')
print(doces)

num = ('1','2','3')
print(len(num))

print('-'*20)
#procurar por indice

num = (1,2,3,4,5)
print(num[0])

print('-'*20)

num = (1,2,3,4,5)
sub_tupla = num[2:4]
print(sub_tupla)

print('-'*20)
num = (1,2,3,4,5)
print(4 in num)

print('-'*20)
#contagem de intem
tupla = tuple((10,20,30,40,50))
print(tupla.count(40))

print('-'*20)
#posição do elemento
tupla = (91,2,'3',4, True, 765)
pos = tupla.index('3')
print(pos)

print('-'*20)
#percorrer pelo for pelo elemento
tupla = (91,2,3,4, True, 765)
for x in tupla:
    print(x)

print('-'*20)
#percorrer pelo for pelo indice
tupla = (91,2,3,4, True, 765)
for i in range(0,len(tupla)):
    print(tupla[i])

print('-'*20)
#percorrer com while
tupla = (5,'3', True, 765)
indice = 0
while (indice < len(tupla)):
    print(tupla[indice])
    indice += 1

#para alterar valor em tupla tem que transformar ela em lista

numero_set = (1,2,3,4)
numero_lista = list(numero_set)#transforma em lista
numero_lista[0] = 12# substituir de 1 para 12
numero_lista.append('fim')#incluir fim em lista
numero_set = tuple(numero_lista)#transforma em tupla novamente
print(numero_set)
