#argumentos arbitrários

def func(valor, nome='teste'):
    print(nome, valor)

func(3)
func(3,'outro')

print('-'*30)

def func(**args):
    print(type(args))
    print(args)
    print(args['Valor'])

func(Valor = '10', operacao = 'soma',resultado = 10)

def printa(x):
    print(x)

def executa_func(func,x):
    func(x)

minha_funcao = printa 
print(type(minha_funcao))

executa_func(minha_funcao, 10)



