#uso basico dos modulos
import datetime #modulo precisa qualificar
print(type(datetime))#classe module
data = datetime.datetime(2023,1,23,15,42,30)# qualificado
print(data)

print('-'*30)
#tempo
import datetime as tempo
data = tempo.datetime(2023,1,23,15,42,30)
print(data)

print('-'*30)

#modulo random(precisa qualificar)
import random
print(random.randrange(10,100))#qualificado

#pra não precisar  qualificar usar a função randrange direto
from random import randrange
print(randrange(10,100))#não qualificado


#posso dar apelido a função (num_aleatorio)

from random import randrange as num_aleatorio
print(num_aleatorio(10,100))#usando apelido


#poedomos importar varias fuções de um modulo
from random import randrange , randint
print(randrange(10,100))#não qualificado


#podemos usar todas as funções de random (import *)
from random import *
print(randrange(10,100))