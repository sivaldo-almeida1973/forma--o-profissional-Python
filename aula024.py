#Mas sobre listas
#como concatenar listas
array1 = [1,2,3]
array2 = [4,5,6]
soma = array1 + array2#concatenação
print(soma)

print('-'*30)
#multiplicação
arra1 = [1,2,3]
mult = array1 * 3
print(mult)

print('-'*30)
#desempacotar array(caso queira os tres)
#printa um por um

numeros = ['um','dois','três']
x,y,z = numeros
print(x) #imprime individualmente
print(z)

print('-'*30)# usando o laço (for)pelo objeto
cores = ['azul', 'brando','amarelo']
for x in cores:
    print(x)

print('-'*30)# usando o laço (for)pelo indice

cores = ['azul', 'brando','amarelo']
for i in range(0,len(cores)):
    print(cores[i])

print('-'*30)
#usando while em listas

cores = ['azul', 'brando','amarelo']
indice = 0
while(indice < len(cores)):
    print(cores[indice])
    indice += 1
    