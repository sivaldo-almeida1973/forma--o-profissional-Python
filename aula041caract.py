#Caracteres / Numeros e Numeros / Caracteres
numero = 70
caractere = chr(numero)
print('o numero %d é mapeado para o caractere %s' %(numero, caractere))


#como gerar caracteres
print('-'*20)

for i in range(5,50):
    caractere = chr(i)
    print('%d - %s' %(i, caractere), end='\n')

#codigo de caracteres

caractere = 'A'
numero = ord(caractere)
print('O caractere %s se mapeia para o numero %d'%(caractere, numero))