#List inserir elemento em lista
#append-> iserir no final da list
#Insert -> inserir em determinada position

array = [10,2,3]
print(array)
array.append(2)#iserir valor ao final da list
print(array)
array.insert(2,'4')#insrir 4 na position (2)
print(array)

#Remover valores de um array...
#remove e pop
print('-'*20)

array = [10,2,3,20,'3']
array.remove(10)#remover o (10)
print(array)
array.pop(2)#remover na position (2) o num (20)
print(array)
print('-'*20)
#Contagem de elementos 
print(len(array))#contagem de elementos

print('-'*20)
#limpar array (clear)
array = [1,2,3,4,5,6]
array.clear()
print(array)

print('-'*20)
# testar se existe determinado elemento
array = [1,2,3,4,5,6, True]
print(1 in array)# vê se existe 1 no array (True)
print(False not in array)# false não está na matriz

print('-'*20)
#testar quantas vezes o elemento repete

lista = [5,6,7,2,3,4,7,]
teste = lista.count(7)#quantas 7 existe na matriz
print(teste)

print('-'*20)
#position de determinado elemento
lista = [5,6,7,2,3,4,7,]
pos = lista.index(5)#qual a position do (5)
print(pos)



