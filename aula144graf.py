#Multiplos Gráficos

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = x1**2

x2 = numpy.arange(0,20,0.5)
y2 = numpy.sin(x2)


plt.style.use('classic')
plt.subplot(1,2,1)#(1 linha) (2 col) (imprimir na parte 1)
plt.title('A primeira função')
plt.plot(x1,y1, color='orange', lw='6.5', ls='dashed')


plt.style.use('classic')
plt.subplot(1,2,2)
plt.title('A segunda função')
plt.plot(x2,y2, color='red' ,lw= '3.5', ls= 'dotted')



print(plt.show())