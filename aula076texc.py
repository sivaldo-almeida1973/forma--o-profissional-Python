#Tratando Exceções

"""lista = [1,2,3,4]
iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
"""

print('-'*30)

lista = [1,2,3]

iterator = iter(lista)

while(True):
  try:
    print(next(iterator))
  except:
      break
