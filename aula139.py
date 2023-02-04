#Personalizando Serie(com cores)
import matplotlib.pyplot as plt
import numpy 

x = numpy.arange(0,10,0.5)
y = x**6

plt.plot(x,y, color='g' )

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('A função y = x**6')
plt.show

print(plt.plot(x,y))
print(plt.title)
print(plt.plot(x,y, color='g' ))

print(plt.show())

#engrossando a linha(linewidth='5.5')
print('-'*50)
import matplotlib.pyplot as plt
import numpy
x = numpy.arange(0,10)
y = 2*x + 1

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

print(plt.plot(x,y, c='b' ,linewidth='5.5'))
print(plt.show())


print(plt.show())

#Mudar o estilo da linha(linestyle= 'dashed')
#tem tambem solid, dotted, dashdot
print('-'*50)
import matplotlib.pyplot as plt
import numpy
x = numpy.arange(0,10)
y = 2*x + 1

plt.xlabel('Vendas')
plt.ylabel('Temperatura')
plt.title('Grafico de Vendas')

print(plt.plot(x,y, c='g' ,linewidth='6.5', linestyle= 'dotted'))
print(plt.show())