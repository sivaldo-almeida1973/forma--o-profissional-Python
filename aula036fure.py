#funções recursivas
#cria uma contagem de 0 a 10
def print_num(num):
    print(num)
    if num >=10:
        return
    print_num(num + 1)

print_num(0)
#chamando texto
print('-'*20)
def print_str(texto, indice):
    if indice == len(texto):#se indice é do tamanho do texto
        return #chamo o return
    print(texto[indice]) #se não imprime texto na posit indice
    print_str(texto,indice +1) # incrementar indice

print_str('Python', 0)#chamo a função

print('-'*20)
#iprimir fatorial de um numero recursivo
def fatorial(num):
    if(num == 1):
        return 1
    return num * fatorial(num-1)

print(fatorial(10))
