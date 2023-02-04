#Aprimorando com Linhas de Grade(marker)

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(1,100)
y1 = x1**2

plt.plot(x1,y1)
plt.grid(
  c='red',  #color
  ls='dotted', #formato
  lw='1.5',  #largura da linha
  alpha=0.1 #transparencia
) #cria uma grade no grafico
print(plt.show())


print('-'*50)

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(1, 100)
y1 = x1**2

plt.plot(x1, y1, color= 'r')
plt.grid(color='b', ls= 'dotted', lw = 1.5)
plt.xticks([1,2,3,4,10,20,40,80,120,180])#muda largura dos blocos da grade
print(plt.show())
