def encontra(array, item):
    for i in array:
      if (i == item):
        return True
    return False

arr = [1,'3',True, 'olá',7.1]
print(encontra(arr,'abc'))
print(encontra(arr,'olá'))
print(encontra(arr,'3'))
print(encontra(arr,'False'))
print(encontra(arr,'True'))