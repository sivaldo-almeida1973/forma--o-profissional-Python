def encontra_indice(array, item):
    for i in range(0,len(array)):
        if (array[i] == item):
            return True, i
    return False, -1

arr = [1,'3',True, 'olá',7.1]
print(encontra_indice(arr,'abc'))
print(encontra_indice(arr,'olá'))
print(encontra_indice(arr,'3'))
print(encontra_indice(arr,'False'))
print(encontra_indice(arr,'True'))