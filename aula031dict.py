# função lambda pra fazer um filtro.
lista = [1,2,3,4,5,6,7,8,9]
lista = list(filter(lambda x: x % 2 == 0, lista))
print(lista)
print('-'*20)
#gerar um matriz 4x4
lista = [[x for x in range(1,5)] for y in range(1,5)]
print(lista)
print('-'*20)
#imprimir as lista separadas
print('-'*20)
lista = [[str (x) + str(y) for x in range(1,5)] for y in range(1,5)]
print(lista)
print('-'*20)
#criando tabuada
tab=[[str(x) +'*'+ str(y) +'='+ str(x*y) for x  in range(1,8)] for y in range(1,10)]
print(tab)


