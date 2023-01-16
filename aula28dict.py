#Dictionaries(lista) possui-chave e valor {}

idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
print(idades)

print('-'*20)

nome_numeros = {7.1: 'sete virgula um',9.8:'nove virgula oito'}
print(nome_numeros)

print('-'*20)
#busca por chave(indice)
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
print(idades['maria'])#indice maria
print(idades['lucas'])

print(idades.get('joão'))#metodo get usa parametro () 

print('-'*20)
nome_numeros = {7.1: 'sete virgula um',
                9.8:'nove virgula oito'}
print(nome_numeros[7.1])
print(nome_numeros.get(9.8))

print('-'*20)
#operador (in)
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
print('ana'in idades)
print('Alice' not in idades)

#atualizar idades 
print('-'*20)
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
idades['maria'] = 30 #alterar idade de maria para 30
idades.update({'ana':40}) #alterar idade de ana para 40
print(idades)

#adicionar elementos
print('-'*20)
idades = {'ana':10, 'maria': 20,'joão':34, 'lucas':'advogado'}
idades['sivaldo'] = 39 # adiciona sivaldo
idades.pop('ana') #remove ana
print(idades)
idades.popitem() #remove o ultimo
print(idades)