"""
crie um lista contendo todos os numeros de 0 a
100, mas filtre,mantendo apenas os que termi-
nam em zero.
"""
lista = [x for x in range(0,100) if str(x)[-1] == '0' ]
print(lista)