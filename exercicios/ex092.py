#Escreva num arquivo os numeros de 0 até 100.and
# #uma linha para cada número. 

#abrir arquivo
with open('exercicio3.txt', 'wt') as arquivo:
  for i in range(0,101):
    arquivo.write(str(i) + '\n')