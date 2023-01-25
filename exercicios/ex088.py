#utilizando como base o exerc 1, retorne o num que representa
#o mes e o proprio mes. faça isso de duas maneiras diferentes
#usando enumeradores  e a outra usando join.

def meses_enum():
  meses = ['janeiro', 'fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
  for i in enumerate(meses):
    yield i

for indice , mes in meses_enum():
  print(indice + 1,mes)