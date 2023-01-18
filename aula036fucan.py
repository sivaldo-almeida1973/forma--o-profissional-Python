#funções aninhadas(quando tem função pai e 
# função filho)
def pai(): #criei função pai
    def filho():# criei função filho
        print('sou filho') # print identado em filho
    filho() #dentro da função pai chamo a func filho
pai()
print('-'*20)
# calculadora que faz soma e subtração
def calculadora(num1, num2,op):
    def soma(a,b):
        return a + b
    def subtrai(a,b):
        return a- b
    if (op == '+'):
        return soma(num1,num2)
    elif (op == '-'):
        return subtrai(num1, num2)

print(calculadora(2,5 ,'-'))
print(calculadora(2,5 ,'+'))

print('-'*20)

def pega_func_print():
    def print_var(var):
        print(var)
    return print_var

print_me = pega_func_print()

print_me(10)
print(type(print_me))

