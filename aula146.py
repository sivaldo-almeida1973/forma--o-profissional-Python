#Graficos de Barras(bar)barras verticais
import matplotlib.pyplot as plt
import numpy

x= numpy.array([1,2,3,4,5])
y = numpy.array([2,4,6,8,10])

plt.bar(x,y, color='g' ,width=0.5)
print(plt.show())

#Graficos de Barras(bar)barras horizontais
import matplotlib.pyplot as plt
import numpy

y= numpy.array([1,2,3])
x = numpy.array(['um', 'dois','tres'])

plt.barh(x,y ,color='red' , height=0.4)
plt.title('Grafico de Barras')
plt.ylabel('Numeros')
plt.xlabel('Valores')
print(plt.show())


#Mais de um Serie em um Grafico

import matplotlib.pyplot as plt
import numpy

valores_esquerda = numpy.arange(0,6) #valor positivo(horiz)
valores_direita = numpy.arange(6,0,-1)#valor negativo(hori)
ys = numpy.arange(6) #variavel valor vertical

#adicionar 2 series de barras horizontais
plt.barh(ys, valores_esquerda, color='y')#valor vertical
plt.barh(ys, -valores_direita,color='c')#valor vertical

plt.legend(['a','b'])#legenda

#elementos de textos
plt.title('Grafico de barras dividido')
plt.ylabel('Valores de Y')
plt.xlabel('Valores esquerda vs direita')

print(plt.show())



#O mesmo Grafico na Vertical
import matplotlib.pyplot as plt
import numpy

valores_esquerda = numpy.arange(0,6) #valor positivo(horiz)
valores_direita = numpy.arange(6,0,-1)#valor negativo(hori)
xs = numpy.arange(6) #variavel valor horizontal

#adicionar 2 series de barras horizontais
plt.bar(xs, valores_esquerda, color='y')#valor vertical
plt.bar(xs, -valores_direita,color='c')#valor vertical

plt.legend(['a','b'])#legenda

#elementos de textos
plt.title('Grafico de barras dividido')
plt.ylabel('Valores de Y')
plt.xlabel('Valores esquerda vs direita')

print(plt.show())



