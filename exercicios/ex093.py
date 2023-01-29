#Escreva num arquivo todos os numeros positivos e menores
# que 100 que são divisiveis por

with open('exercicio4.txt','wt' ) as arquivo:
  for i in range(0,101):
    if i % 3 == 0:
      arquivo.write(str(i) + '\n')
