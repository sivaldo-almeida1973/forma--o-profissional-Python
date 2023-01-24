#Gerando as proprias excessões (raise)
#raise Exception('Nos geramos erros')

print('-'*30)
#erro especifico do python

#raise IndexError('Excessão de indice')


#tratamento de exceções
def printa_positivo(numero):
  if numero < 0:
    raise ValueError('valor não pode ser negativo')
  print(numero)

try:
  printa_positivo(-1)
except ValueError as erro:
  print('o erro é', str(erro))
except Exception as erro1:
  print('erro qualquer>', str(erro1))


  #outra função importante do python (assert)
def printa_positivo(numero):
  assert (numero >= 0)
  print(numero)

try:
  printa_positivo(-1)
except AssertionError as erro:
  print('o erro é', str(erro))
except Exception as erro1:
  print('erro qualquer', str(erro1))


print('-'*30)

lista = [1]
try:
  print(lista[10])
except IndexError as error:
  raise error
