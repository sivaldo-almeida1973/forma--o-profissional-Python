#Presonalizando Fontes

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

print(plt.xlabel('vendas'))
print(plt.ylabel('temperatura'))
print(plt.title('Gráfico de Vendas'))
print(plt.plot(x,y))
print(plt.show())


#print(plt.title('Gráfico de Vendas', y=1.1))
#titulo do grafico e posicionamento (pra cima ou pra baixo)
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

print(plt.xlabel('vendas'))
print(plt.ylabel('temperatura'))
print(plt.title('Gráfico de Vendas', y=1.1))
print(plt.plot(x,y))
print(plt.show())

#print(plt.title('Gráfico de Vendas', y=1.1, loc=rigth)) direita ,esquerda, centro
#titulo do grafico e posicionamento 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

print(plt.xlabel('vendas'))
print(plt.ylabel('temperatura'))
print(plt.title('Gráfico de Vendas', y=1.1 , loc='center'))
print(plt.plot(x,y))
print(plt.show())

#print(plt.title('Gráfico de Vendas', y=0.9, loc=rigth)) direita ,esquerda, centro
#titulo do grafico e posicionamento 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

print(plt.xlabel('vendas'))
print(plt.ylabel('temperatura'))
print(plt.title('Gráfico de Vendas', y=0.9 , loc='center'))
print(plt.plot(x,y))
print(plt.show())


#print(plt.title('Gráfico de Vendas', y=0.9, loc=rigth)) direita ,esquerda, centro
#titulo do grafico e posicionamento 
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2

print(plt.xlabel('vendas'))
print(plt.ylabel('temperatura'))
print(plt.title('Gráfico de Vendas', y=0.9 , loc='left', x= 0.01))
print(plt.plot(x,y))
print(plt.show())

#Posso customizar
import matplotlib.pyplot as plt
import numpy as np


font_props = {
'family':'arial',
'color':'blue',
'weight': 'bold',
'size'  : 20

}
x = np.arange(0,20,0.5)
y = x**6

print(plt.xlabel('vendas', fontdict= font_props))
print(plt.ylabel('temperatura',fontdict=font_props))
print(plt.title('Gráfico de Vendas', fontdict=font_props))

print(plt.plot(x,y))
print(plt.show())



#caso queira adiconar texto aleatorio(plt.text())
font_props = {
'family':'arial',
'color':'blue',
'weight': 'bold',
'size'  : 16

}

font_props2 = {
'family':'arial',
'color':'red',
'weight': 'normal',
'size'  : 20

}
x = np.arange(-10,10,0.1)
y = x**2

plt.text(-5,50, 'É uma parábola', fontdict= font_props2)

print(plt.xlabel('vendas', fontdict= font_props))
print(plt.ylabel('temperatura',fontdict=font_props))
print(plt.title('Gráfico de Vendas', fontdict=font_props))

print(plt.plot(x,y))
print(plt.show())