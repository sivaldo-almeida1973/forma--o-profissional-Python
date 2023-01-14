idade = input('Digite a sua idade:' )
idade = int(idade)
if idade  <= 3 :
    print('voce é um bebê')
elif idade > 3 and idade <= 13:
    print('voce é uma Criança!')
elif idade > 13 and idade <= 18:
    print('voce é um adolescente!')
elif idade > 18 and idade <= 65 :
    print('voce é um adulto!')
else:
    print('voce é um idoso!')

print('Parabens!')

