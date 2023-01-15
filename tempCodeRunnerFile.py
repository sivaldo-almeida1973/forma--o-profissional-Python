letra = input('digite uma letra: ' )
texto = input('digite uma texto: ' )
for i in range(0, len(texto)):
    if letra == texto[i]:
        
        print('encontrei a letra %s na posição %d '% (letra, i))
