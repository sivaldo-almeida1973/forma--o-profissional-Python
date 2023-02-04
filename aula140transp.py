#Legendas e Transparencias

import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel('Vendass')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

plt.plot(x1,y1, c='g' , lw='6.5' , ls='dashed', label='vendas')
plt.plot(x2,y2, c='r' , lw='3.5' , ls='solid', label='Temperatura')
plt.legend(loc='lower right')#posição da legenda(varios parametros)
print(plt.show())



#transparencia(alpha=10) coloca no eixo escolhido
import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel('Vendass')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

plt.plot(x1,y1, c='g' , lw='6.5' , ls='dashed', label='vendas', alpha=0.1)
plt.plot(x2,y2, c='r' , lw='3.5' , ls='solid', label='Temperatura')
plt.legend(loc='upper right')#posição da legenda(varios parametros)
print(plt.show())