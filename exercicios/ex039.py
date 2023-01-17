"""crie um lista contendo todos os dias(numero) do 
mes em que voce nasceu.
Em seguida receba por input o dia (numero) em que 
voce nasceu e remova desta lista.Ao final mostre 
o conteudo da lista"""


dias = []
for i in range(1,32):
  dias.append(i)
dias_nascido = int(input('digite seu dia de nascimento: '))
dias.remove(dias_nascido)
print(dias)


