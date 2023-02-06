#Graficos de Dispersão(scatter)
import matplotlib.pyplot as plt
import numpy 

x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

plt.scatter(x,y)
plt.title('Grafico de Dispersão')
print(plt.show())


#definir um estilo ao mesmo grafico de cima
#usa-se para comparar duas variaveis numericas
import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

cores = numpy.array(['r','r','g','b','b','r','y','brown','pink','gray'])

plt.scatter(x,y, color=cores, marker='o', s=100)# s=tamanho dos marcadores
plt.title('Grafico de Dispersão')
print(plt.show())



#criar uma terceira variavel(z)
import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])
z = numpy.array([100,50,150,200,100,120,130,80,90,144])


cores = numpy.array(['r','r','g','b','b','r','y','brown','pink','gray'])

plt.scatter(x,y, color=cores, marker='o', s=z)# s=variavel z
plt.title('Grafico de Dispersão')
print(plt.show())



#Ao inves de ter uma lista de cores e tamanho,posso criar um indice.
import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])


z = numpy.array([25,50,75])
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

plt.scatter(x,y, color=cores[z_cores], marker='o', s=z[z_indices])# s=variavel z
plt.title('Grafico de Dispersão')
print(plt.show())



#variação da cor da borda
import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

z = numpy.array([125,250,375])#tamanho ods elementos
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

plt.scatter(x,y, color=cores[z_cores], marker='^', s=z[z_indices], edgecolor='y', linewidths=2)#cor da borda( edgecolor='y')  (linewidths=2)engrossa borda 
plt.title('Grafico de Dispersão')
print(plt.show())


#variação da cor da borda(nesse cirei uma var z_borda) com cores !=
import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

z = numpy.array([125,250,375])#tamanho ods elementos
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

z_bordas = numpy.array([2,0,0,1,2,1,1,1,2,1])

plt.scatter(x,y, color=cores[z_cores], marker='^', s=z[z_indices], edgecolor=cores[z_bordas], linewidths=2)#cor da borda( edgecolor='y')  (linewidths=2)engrossa borda 
plt.title('Grafico de Dispersão')
print(plt.show())




import matplotlib.pyplot as plt
import numpy 
plt.style.use('bmh')
x = numpy.arange(0,10)
y = numpy.array([1,4,9,12,4,7,4,9,2,1])

x1 = numpy.arange(10,20)
y1 = numpy.array([4,4,5,12,4,7,7,9,9,1])

z = numpy.array([125,250,375])#tamanho ods elementos
z_indices = numpy.array([0,2,1,1,1,0,2,1,1,0])

cores = numpy.array(['r','g','b'])
z_cores = numpy.array([0,1,1,0,1,2,2,0,1,0])

z_bordas = numpy.array([2,0,0,1,2,1,1,1,2,1])

plt.scatter(x,y, color=cores[z_cores], marker='^', s=z[z_indices], edgecolor=cores[z_bordas], linewidths=2)#cor da borda( edgecolor='y')  (linewidths=2)engrossa borda 

plt.scatter(x1,y1, color=cores[z_cores], marker='o', s=z[z_indices], edgecolor=cores[z_bordas], linewidths=2)#cor da borda( edgecolor='y')  (linewidths=2)engrossa borda 

plt.title('Grafico de Dispersão')
print(plt.show())



#como colococar legenda no grafico de dispersão
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('default')#zerar estilos anteriores(resetar)

x = np.random.randint(10,size=10)
y = np.random.randint(10,size=10)
x2 = np.random.randint(10,size=10)
y2 = np.random.randint(10,size=10)

plt.scatter(x,y ,label= 'Meninos')
plt.scatter(x2,y2 ,label= 'Meninas')
plt.title('Grafico de dispersão')
plt.legend()
print(plt.show())

