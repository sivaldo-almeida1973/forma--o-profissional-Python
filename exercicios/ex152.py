#Com base nos dados do exercicio anterior.
#Plote dois graficos separados (um no lado do outro)
#Em um voce ira plotar o rafico da variação Dolar x Real.
#E no outro ira plotar o PIB per Capita do brasil, nos mesmos anos.
#Escolha o tipo de grafico que preferir.
#Dados do PIB(dados ficticios):
#2016:8710,50
#2016:9928,50
#2016:9151,58
#2016:8897,29
#2016:6795,50
#2016:7500,50
#2016:7542,50


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2016, 2023)
y1 = np.array([3.15,3.26,3.88,4.30,5.33,5.45,5.39])
y2 = np.array([8710.50,9928.50,9151.58,8897.29,6795.50,7500.0,7542.34])
#grafico 1
plt.subplot(1,2,1)#(uma linha),( 2 colunas) ,(grafico 1).
plt.xlabel('Ano')
plt.ylabel('Valor do Real (R$)')
plt.title('Variação Dolar vs Real')
plt.bar(x,y1 , color='r', width=0.7)

#Grafico 2
plt.subplot(1,2,2)
plt.xlabel('Ano')
plt.ylabel('PIB per Capita')
plt.title('Variação do PIB per Capita')
plt.plot(x,y2 , color='r' ,lw='3.5', ls='solid', marker='s', mfc='g')


plt.suptitle('Situação Economica do Brasil', y =1)
plt.tight_layout()#corrige defeitos de sobreposição
print(plt.show())

