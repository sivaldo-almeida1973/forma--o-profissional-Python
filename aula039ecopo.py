var2 = 10

def func():
    var2 = 20
    print(var2)

func()
print(var2)

print('-'*20)

#função global
var2 = 10

def func():
    global var2 #serve pra imprimir alteração interna
    var2 =20

func()
print(var2)


print('-'*20)

def func_pai():
    pai = 10
    def func_filho():
        print(pai)
    func_filho()

func_pai()

print('-'*20)

def func_pai():
    pai = 10
    def func_filho():
        pai = 20
        print(pai)
    func_filho()
    print(pai)

func_pai()

print('-'*20)


def func_pai():
    pai = 10
    def func_filho():
       nonlocal pai #serve para alterar 
       pai = 20
       print(pai)
    func_filho()
    print(pai)

func_pai()

print('-'*20)
#vai dar um erro ,foi deletado
#var = 20
#print(var)
#del var
#print(var)

print('-'*20)
#deletar elemento 0
array = [1,2,3]
del array[0]
print(array)

print('-'*20)
#deletar ate elemento 2
array = [1,2,3]
del array[:2]
print(array)
