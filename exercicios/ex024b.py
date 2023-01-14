num1 = float(input('Digite um numero:' ))
num2 = float(input('Digite outro numero: '))
operacao = input('digite a operação:')

if ( operacao == '+'):
    soma = num1 + num2
    print('A soma de %s com %s é %d:' %(num1, num2,soma))
elif( operacao == '-'):
    subt = num1 - num2
    print("A subtração de %s menos %s é %s" %(num1,num2,subt))
elif (operacao == '*'):
    mult = num1 * num2
    print('a multiplicação entre %s e %s são %s' % (num1, num2,mult))
elif (operacao == '//'):
    divisao = num1 // num2  
    print('a divisão de %s por %s é %s' %(num1, num2 , divisao))
else:
    print('Operação invalida!!')