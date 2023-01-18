"""crie uma função que receba 2 numeros e uma 
string dizendo se deve realizar a soma ou sub
tração
"""
def calculo(num1, num2, op):
    if(op == '+'):
        return num1 + num2
    else:
        return num1 - num2

print(calculo(1,5,'-'))
