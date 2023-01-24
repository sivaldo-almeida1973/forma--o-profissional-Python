#Diferentes tipos de excessoes
print('Inicio')
lista = [1,2,3]
try:
  print(lista[10])
except IndexError as erro1:
  print('Erro de acesso ao indice: ' + str(erro1))
except:
  print('ocorreu outro erro')
else:
  print('executa se não ocorre erro')

print('Fim!!')

print('-'*30)

#Diferentes tipos de excessoes
print('Inicio')
lista = [1,2,3]
numero = 0
try:
  divisão = 10 / numero
  print(lista[12])
except IndexError as erro1:
  print('Erro de acesso ao indice: ' + str(erro1))
except ZeroDivisionError as erro2:
  print('Erro de divisão por zero' + str(erro2))
except Exception as erro3:
  print('ocorreu outro erro' + str(erro3))
else:
  print('executa se não ocorre erro')

print('Fim!!')

#https://docs.python.org/3/library/exceptions.html