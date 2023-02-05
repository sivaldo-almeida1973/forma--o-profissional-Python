#Histogramas(hist)
#(edgeColor)cor da borda
#  (bins) barras intervalos que quero que mostre a frequencia de determinada altura
import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75,1.50, 1.46, 1.65,1.74,1.76,1.80,1.73,1.89,1.90])
plt.hist(alturas, color='red',edgecolor='b', bins= [1.40,1.50,1.60,1.70,1.80,1.90,2])
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuição de alturas')
print(plt.show())


#Definir Bins automaticamente

import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75,1.50, 1.46, 1.65,1.74,1.76,1.80,1.73,1.89,1.90])
plt.hist(alturas, color='red',edgecolor='b', bins= 7)
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuição de alturas')
print(plt.show())


#Deixa mas automatico ainda se não definir os bins

import matplotlib.pyplot as plt
import numpy as np

alturas = np.array([1.75,1.50, 1.46, 1.65,1.74,1.76,1.80,1.73,1.89,1.90])
plt.hist(alturas, color='red',edgecolor='b')
plt.xlabel('Alturas')
plt.ylabel('Ocorrencias')
plt.title('Distribuição de alturas')
print(plt.show())


#comparar a altura das pessoas do mundo com determinado pais
import matplotlib.pyplot as plt
import numpy as np

altura_mundial = np.random.normal(loc= 175, scale=11, size=1000)/100
altura_brasil = np.random.normal(loc=185, scale=9, size=1000)/100

plt.hist(altura_mundial, bins=7, color='b', edgecolor='g', alpha=0.5)
plt.hist(altura_brasil, bins=7, color='y', edgecolor='r', alpha=0.5)
plt.legend('Altura Mundial','Altura Brasil' )
plt.xlabel('Altura')
plt.ylabel('Ocorrencias')
plt.title('Distribuição de altura')
print(plt.show())


