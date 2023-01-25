#crie uma função iteravel 'meses' que retorne meses.
#Use o laço for para mostrar os valores.
def meses():
    yield 'janeiro'
    yield 'fevereiro'
    yield 'março'
    yield 'abril'
    yield 'maio'
    yield 'junho'

for indice , valor in enumerate(meses()):
  print(indice, valor)



print('-'*30)

def meses():
  meses = ['janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
  for i in meses:
    yield i

for mes in meses():
  print(mes)

