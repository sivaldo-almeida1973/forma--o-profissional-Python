def transforma_lista(lista):
    lista_inteiros = []
    for item in lista:
        if item.isdecimal():
            lista_inteiros.append(int(item))
    lista_inteiros.sort()
    return lista_inteiros

lista = ['12','123r', '6','9','100','aass']

print(transforma_lista(lista))