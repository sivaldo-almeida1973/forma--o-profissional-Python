#copiando um array

import numpy as np
array = np.array([1,2,3])
cop_array = array
cop_array[0] = 0#copia por referencia
print(array)

#essa é uma verdadeira copia
import numpy as np
array = np.array([1,2,3])
cop_array = array.copy()
cop_array[0] = 0
print(array)