numero = 2
if numero == 1 or numero == 0:
    print('verdade!')
else:
    print('mentira!')

print('-'*20)

print('-'*20)
numero = -10
if numero > 0 and numero < 10:
    print('verdade')
else:
    print('nao existe')


print('-'*20)

numero = 11
if numero > 0:
    print('numero maior que zero')
    if numero > 10:
        print('numero maior que 10')

# Elif

print('-'*20)

num = 1000
if num < 10:
    print('Menor que 10')
elif num < 100:
    print('Menor que 100')
elif num <= 1000:
    print('Menor que 1000')
else:
   print ('Nenhuma das opções!')


print('-'*20)

texto = 'n'
if texto == 'a':
    print('é vogal A')

elif texto == 'e':
    print('é vogal E')

elif texto == 'i':
    print('é vogal I')
elif texto == 'o':
    print('é vogal O')

elif texto == 'u':
    print('é vogal U')

else:
    print('É consoante')
print('-'*20)

num = 10
resultado = 'PAR' if num % 2 ==0 else 'impar'
print(resultado)

print('-'*20)

num = 3
res = 'UM' if num == 1 else 'dois' if num =='2' else 'tres'
print(res)
