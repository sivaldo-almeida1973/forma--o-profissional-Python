
"""import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([1,2,3,4,5])
y1 = x1 * 2

x2 = np.array([5,10,15])
y2 = x2 + 2


print(plt.plot(x1,y1))
print(plt.plot(x2,y2))
print(plt.show())"""


"""import matplotlib.pyplot as plt
import numpy 
x1 = numpy.arange(1,10)
y1 = x1 * 2

x2 = numpy.arange(1,10)
y2 = x2 ** 2  #exponenciação

print(plt.plot(x1, y1))
print(plt.plot(x2, y2))
print(plt.axis([0,10, -1,50]))#modifica eixo original
print(plt.show())
"""

#mudar os eixos individualmente
import matplotlib.pyplot as plt
import numpy 
x1 = numpy.arange(1,10)
y1 = x1 * 2

x2 = numpy.arange(1,10)
y2 = x2 ** 2
print(plt.plot(x1, y1))
print(plt.plot(x2, y2))
print(plt.xlim(0,10))#eixo orizontal
print(plt.ylim(-1,50))#eixo vertical
print(plt.show())