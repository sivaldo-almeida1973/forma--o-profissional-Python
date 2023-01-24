#Excessões(corrigindo erro)

#print('Inicio')
#lista = [1,2,3]
#print(lista[10])
#print('fim')
#deu erro

#nesse caso iremos corrigir o erro de cima(excessão)

print('Inicio')
lista = [1,2,3]
try:
  print(lista[10])
except:
  print('falha do acessar ,linha não encontrada!')
print('Fim!!')


print('-'*30)

print('Inicio')
lista = [1,2,3]
try:
  print(lista[10])
except Exception as ERROR:
  print('falha do acessar ,linha não encontrada,mensagem: ' + str (ERROR))
print('Fim!!')

print('-'*30)

try:
  numero = int('b')
except Exception as error:
    print('falha no cast:', str )



print('-'*30)

print('Inicio')
lista = [1,2,3]
try:
  print(lista[0])
except:
  print('falha do acessar ,linha não encontrada!')
finally:
  del lista
  print('ececuta sempre que o try-except acabar, mesmo que não ocorra erro!')
print('Fim!!')



print('-'*30)

print('Inicio')
lista = [1,2,3]
try:
  print(lista[10])
except:
  print('falha do acessar ,linha não encontrada!')
else:
  print('não houve erro!')
print('Fim!!')



print('-'*30)

print('Inicio')
lista = [1,2,3]
try: #codigo que pode dar erro
  print(lista[0])
except: # codigo executado se der erro
  print('falha do acessar ,linha não encontrada!')
else: #codigo executado se não der erro
  print('Não houve erro!')
finally: #codigo executado sempre
  del lista
  print('ececuta sempre que o try-except acabar, mesmo que não ocorra erro!')
print('Fim!!')
