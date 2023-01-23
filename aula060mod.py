#Explorando um modulo

import random
dir(random)


import random
dir(random.randrange)

import random
print(random.__name__)
print(random.__file__)
print(random.__doc__)

print('-'*50)

from random import randrange
print(randrange.__name__)
print(randrange.__doc__)

print('-'*50)

print(__name__)
print(__doc__)