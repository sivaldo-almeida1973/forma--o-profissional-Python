#Adicionando marcadores
import matplotlib.pyplot as plt
import numpy

x= numpy.arange(0,19)
y = -x**4
#marcador(marker)ponto de econtro entre x e y
#opçoes (, . v ^ < > s p *  h H +  D | )
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Grafico da função y = -x**4')
plt.plot(x,y, c='orange', lw='1.5', marker = '<')
print(plt.show())


#Presonalizar  marcadores(mostra a intersecão dos eixos)
import matplotlib.pyplot as plt
import numpy

x1 = numpy.arange(0,20,0.5)
y1 = numpy.cos(x1)

x2 = numpy.arange(0,20,0.5)
y2 = numpy.cos(x2)*2

plt.xlabel('Vendass')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

#aumenta o tamanho do marcador(markersize)
#borda  marker( markeredgecolor) interior do marker(markerfacecolor)colore
plt.plot(x1,y1, c='g' , lw='1.5' , ls='dashed', label='vendas', marker= '+', markersize='10')
plt.plot(x2,y2, c='r' , lw='1' , ls='solid', label='Temperatura', marker='s', markerfacecolor='red', markeredgecolor='black')
plt.legend(loc='upper right')#posição da legenda(varios parametros)
print(plt.show())