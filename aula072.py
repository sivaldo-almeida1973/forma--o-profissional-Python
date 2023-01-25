#Generators(funções iteraveis) (yield)
def ancora():
   yield 1 #salva o estado da funcão(ordem)
   yield 2 #função iteravel
   yield 3

for item in ancora():
    print(item)

print(10 in ancora())
print(2 in ancora())

func = ancora()

print(next(func))
print(next(func))
print(next(func))


for i in range(10):#vai imprimir os num até 9
  print(i)


print('-'*30)

def meu_range(num):
  local_num = 0
  while local_num < num:
    yield local_num
    local_num += 1


for i in meu_range(10):
  print(i)