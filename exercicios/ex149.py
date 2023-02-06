#Plote a função y=5x +1.Onde x vai de 0 até 10.Use #marcadores do tipo quadrado.Informe o titulo do #grafico e eixos x e y. De cores vermelho aos #marcadores(mfc) e azul a reta(onde fica os #marcadores).

import matplotlib.pyplot as plt
import numpy as np

x =  np.arange(0,11)
y = 5 * x + 1

plt.title('Função y = 5 *x + 1')
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.plot(x, y , color='blue', mfc='r', marker='s' )
print(plt.show())