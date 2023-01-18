#Decorators(decoradores)
#criar executar  fuções de forma aninhada
def DeixaMaiuscula(func): # criar função, que recebe (func)
    def inner_func(): #função aninhada 
        return func().upper() #vai transformar em maiuscula
    return inner_func #retorno pra deixar maiuscula

@DeixaMaiuscula # decorador com arroba(@)
def retorna_string(): 
    return 'string de teste'

valor = retorna_string()
print(valor)


print('-'*20)

def DeixaMaiuscula(func): # criar função, que recebe (func)
    def inner_func(str1, str2): #função aninhada 
        return func(str1,str2) .upper()
    return inner_func 

@DeixaMaiuscula
def concatena_string(str1,str2):
    return str1 + str2

valor = concatena_string('teste','abc')
print(valor)
