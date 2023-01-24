#crie uma função que rceba uma lista e um numero e retorne o 
#elemento da llista na posição deste numero. Faça um tratamento para que #caso haja um acsso fora do indice a função retorne o valor None.

def acessa_seguro(lista,indice):# função
  try:
    return lista[indice]
  except:
   return None;

lista = [1]
print(acessa_seguro(lista, 0))  

