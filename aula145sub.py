#Ajustando Multiplos Graficos
import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x1)*2

plt.subplot(1,2,1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A primeira função coseno')
plt.plot(x1,y1, color='g', lw='2.5', ls='dashed', label= 'y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-2,1) #serve para ampliar espaços do grafico e tirar legendada frente


plt.subplot(1,2,2)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A segunda função coseno')
plt.plot(x2,y2, color='b', lw='3.5', ls='solid', label= 'y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3,2)#serve para ampliar espaços do grafico e tirar legendada frente
#Outra propriedade interessante plt.tight_layout() centariza os (eixos centrais)
plt.tight_layout()
print(plt.show())




import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x1)*2

plt.subplot(2,2,1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A primeira função coseno')
plt.plot(x1,y1, color='g', lw='2.5', ls='dashed', label= 'y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-2,1) #serve para ampliar espaços do grafico e tirar legendada frente

plt.subplot(2,2,2)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A primeira função coseno')
plt.plot(x1,y1, color='black', lw='2.5', ls='dashed', label= 'y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-2,1) #serve para ampliar espaços do grafico e tirar legendada frente

plt.subplot(2,2,3)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A segunda função coseno')
plt.plot(x2,y2, color='b', lw='3.5', ls='solid', label= 'y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3,2)#serve para ampliar espaços do grafico e tirar legendada frente

plt.subplot(2,2,4)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A segunda função coseno')
plt.plot(x2,y2, color='red', lw='3.5', ls='solid', label= 'y=cos(x)*2')
plt.legend(loc='lower right')
plt.ylim(-3,2)#serve para ampliar espaços do grafico e tirar legendada frente
plt.subplots_adjust(wspace=0.8)#Ajustar espaços entre os graficos(top ,left,rigt)
plt.subplots_adjust(hspace=0.8)# ajusta na vertical

plt.suptitle('Meus Graficos')
print(plt.show())
