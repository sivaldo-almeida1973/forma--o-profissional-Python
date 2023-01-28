#Leia o seguinte arquivo('exercicio1.txt) e transforme em umalista

lista = []
with open('numeros_3.txt', 'rt')as arquivo:
  for linha in arquivo:
    lista.append(linha)

print(linha)