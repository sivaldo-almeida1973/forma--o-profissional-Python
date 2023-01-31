#Interação em arrays
import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in array:
  print(i)

print('-'*30)

import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in array:
  for j in i:
   print(j)

print('-'*30)
import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])
for i in array:
  print(array)


print('-'*30)
import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8]])
print(array)

for x in np.nditer(array, order='F'):
  print(x)
