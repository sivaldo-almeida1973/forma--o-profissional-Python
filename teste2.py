import teste

dir(teste)


import teste
print(teste.PI)
teste.MyFunc(10)


from teste import PI
print(PI)

from teste import MyFunc
MyFunc('teste')

from teste import PI as Numero_PI
print(Numero_PI)