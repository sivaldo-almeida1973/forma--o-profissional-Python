#Exemplos de valor e referencia
#listas e objetos são copiados por referencia
list1 = [1,2,3]
list2 = list1
list2.append(10)
print(list1)

print('-'*30)

class Classe:
    def __init__(self):
        self.num =10

class1 = Classe()
class2 = class1
class1.num = 20
print(class2.num)

# como copiar ojeto ou lista por valor e não por ref.
#se eu quiser fazer um copia independente do objeto.
#No python temos a função (Copy)
from copy import copy
list1 = [1,2,3]
list2 = copy(list1)#naõ vai ser uma ref. vai apontar para um #local em memoria
list2.append(10)
print(list1)

print('-'*30)
from copy import copy
class Classe:
    def __init__(self):
        self.num =10

class1 = Classe()
class2 = copy(class1)#naõ vai ser uma ref. vai apontar para #um local em memoria
class1.num = 20
print(class2.num)




print('-'*30)


class Classe:
    def __init__(self):
        self.num =10

class1 = Classe()
class2 = (class1)
class1.num = 20
print(class2 is class1)#testando se class2 e class1 apontam #pra o mesmo lugar da memoria


print('-'*30)

from copy import copy
class Classe:
    def __init__(self):
        self.num =10

class1 = Classe()
class2 = copy(class1)
class1.num = 20
print(class2 is class1)