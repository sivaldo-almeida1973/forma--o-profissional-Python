#como aumentar grafico()

import matplotlib.pyplot as plt
import numpy as np

#caso queira adiconar texto aleatorio(plt.text())
font_props = {
'family':'arial',
'color':'blue',
'weight': 'bold',
'size'  : 16

}
#personalização do texto
font_props2 = {
'family':'arial',
'color':'red',
'weight': 'normal',
'size'  : 20

}
x = np.arange(-10,10,0.1)
y = x**2
#aumentar tamanho do grafico(resolução)
plt.figure(figsize=(10,10))

plt.text(-5,50, 'É uma parábola', fontdict= font_props2)

print(plt.xlabel('vendas', fontdict= font_props))
print(plt.ylabel('temperatura',fontdict=font_props))
print(plt.title('Gráfico de Vendas', fontdict=font_props))

print(plt.plot(x,y))
print(plt.show())



#Imagem menor
import matplotlib.pyplot as plt
import numpy as np

#caso queira adiconar texto aleatorio(plt.text())
font_props = {
'family':'arial',
'color':'blue',
'weight': 'bold',
'size'  : 16

}
#personalização do texto
font_props2 = {
'family':'arial',
'color':'red',
'weight': 'normal',
'size'  : 10

}
x = np.arange(-10,10,0.1)
y = x**2
#aumentar tamanho do grafico(resolução)(padrão 6.4,4.8)
plt.figure(figsize=(3.2,2.4))

plt.text(-5,50, 'É uma parábola', fontdict= font_props2)

print(plt.xlabel('vendas', fontdict= font_props))
print(plt.ylabel('temperatura',fontdict=font_props))
print(plt.title('Gráfico de Vendas', fontdict=font_props))

print(plt.plot(x,y))
print(plt.show())