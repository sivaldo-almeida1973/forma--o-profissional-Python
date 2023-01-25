#join de Iteradores(pra cada elemento do texto junta com objeto iteravel)
texto1 = "Olá"
print('#'.join(texto1))#coloca # entre elementos


print('-'*30)

lista = ['1','2','3','4','5','6','7']
numeros = ' '.join(lista)#coloca espaços entre os elementos
print(numeros)

#coloca traços entre os numeros
letras = '-'.join([str(i) for i in range(10)])
print(letras)


print('-'*30)
#com função geradora

def anos():
  for i in range (2020,2030):
    yield str(i)

letras =  '-'.join(anos())
print(letras)