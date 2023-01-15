#for x in range(10):
 #   print(x)
#for x in range(5, 10):
#    print(x)
#for x in range(5,25,5):
 #   print(x)

#for x in range(25,5,-5):
 #   print(x)

#texto ='123456A8910'
#for x in range(len(texto)):
 #   print(texto[x])
letra = input('digite uma letra: ' )
texto = input('digite uma texto: ' )
for i in range(0, len(texto)):
    if letra == texto[i]:
        print('encontrei a letra %s na posição %d '% (letra, i))
