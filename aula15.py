#Laços/loops.
#repeticao = 10
#while(repeticao > 0):
 #   print(repeticao)
 #   repeticao -= 1
#print('Encerrou!!')

indice = 10
print('Programa começou')
while (indice >= 2):
    resto = (indice % 2)
    if resto == 0:
       print('O numero %d é Par!' %( indice))
    else:
       print('o numero %d é impar' % (indice))
    indice -= 1

print('programa finalizou!')
