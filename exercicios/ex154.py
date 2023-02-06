#Crie um grafico de dispersão mostrando a relação entre peso e altura
#de algumas pessoas.Analize os resultados
#Dados altura =[1.60,1.62,1.65,1.65,1.70,1.75,1.80,1.85,1.90,1.90,1.95,2.0].
#Dados do peso=[60,61,64,67,70,73,75,80.85,90,85,1.95,2.0]

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1.60,1.62,1.65,1.65,1.70,1.75,1.80,1.85,1.90,1.90,1.95,2.0])
y = np.array([60,61,64,67,70,73,75,80.85,90,85,95,100])

ax = plt.scatter(x,y)#relação peso e altura
plt.title('Relação Peso e Altura')
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.plot(x,y)
print(plt.show())