from random import randrange

def get_random_lista(inicial, final, tam):
  lista = []
  for i in range(0, tam):
    numero = randrange(inicial, final)
    lista.append(numero)
  return lista 
print(get_random_lista(1,100,10))