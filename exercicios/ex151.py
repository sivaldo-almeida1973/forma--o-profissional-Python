#Faça o mesmo exercicio anterior em um grafico de barras, compare os resultados.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2016, 2023)
y = np.array([3.15,3.26,3.88,4.30,5.33,5.45,5.39])

plt.xlabel('Ano')
plt.ylabel('Valor do Real (R$)')
plt.title('Variação Dolar vs Real')
plt.bar(x,y , color='r')
print(plt.show())






