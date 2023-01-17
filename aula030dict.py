dados_por_nome = {
     'ana':{
         'sexo':'feminino',
         'cpf':'12312312312',
         'Rg':'12312312'
    },

     'maria':{
         'sexo':'feminino',
         'cpf':'12312312555',
         'Rg':'123125799'
    },

     'lucas':{
         'sexo':'masculino',
         'cpf':'1231231333',
         'Rg':'12312312'
    }
}
print('Ana:',dados_por_nome['ana']['Rg'])
print('maria:',dados_por_nome['maria']['cpf'])
print('luca:',dados_por_nome['lucas']['sexo'])

print('-'*20)
#cria lista de 0 até 9
lista = [x for x in range(0,10)]
print(lista)

print('-'*20)

lista = ['1','zero', 'quatro']
lista = [x for x in lista]
print(lista)

print('-'*20)
#cria lista só com pares
lista = [x for x in range(1,11) if x% 2 == 0]
print(lista)

print('-'*20)
#criar lista desde que os elementos não exista na outra
lista_aux = [1,5,9]
lista =(x for x in range(1,11) if x not in lista_aux)
print(lista)

print('-'*20)
#numeros positivos
lista = [x for x in range(0,11) if x <= 10 if x >= 0]
print(lista)

#numeros pares
print('-'*40)
lista = [x*2 for x in range(0,11)]
print(lista)

print('-'*40)
#lista em formato de string
lista = [str(x) for x in range(0,21)]
print(lista)

print('-'*40)
#so o primeiro item de cada elemento
lista = [str(x)[0] for x in range(0,21)]
print(lista)

print('-'*40)
# imprimir negativo(-) ou positivo(+) usando if
lista = ['negativo' if x < 0 else 'positivo' for x in range(-3,4)]
print(lista)

# imprimir par ou impar usando if
print('-'*40)
lista = [ str(x) +' par 'if x % 2 == 0 else str(x) + ' impar ' for x in range (2,11)]
print(lista)

