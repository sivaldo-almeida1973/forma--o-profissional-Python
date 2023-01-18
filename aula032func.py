def func():#cirar função
    num = 10
    print('uma função %d '%(num))
func()#chamar função
func()

def fun():#função vazia
 pass
func
print('-'*30)

def print_var(numero):
    print(numero)

print_var(2)
print('maça')

print('-'*30)

def func_soma(num1, num2,num3):
    print(num1 + num2 +num3)

func_soma(1,3,4)
func_soma(3.3,1.1,5)
func_soma('Olá ', 'mundo','!')
func_soma('sivaldo ','Alice ', 'lucas')

print('-'*30)

def func(*args):
    print(type(args))
    print('argumentos são:',args)

func(1,2,3)
func()
func('olá',True, [1,2,3,])

print('-'*30)

def func_sub(num1, num2,num3):
    print(num1 , num2 ,num3)

func_sub(10,2,3)
func_sub(num1=2, num2=3, num3=10)

#parametros arbitrarios.
def func(*args, outro):
    print('argumentos são:',args)
    print(outro)

func(1,7,3, outro='1')
func(outro=5)
func('olá ',True, [1,2,34], outro='3')
