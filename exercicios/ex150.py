#Plote os dados a seguir em um grafico com linhas:
#Valor do real em relação ao dolar (dados ficticios)
#2016: 3,15
#2017: 3,26
#2018: 3,88
#2019: 4,30
#2020: 5,33
#2021: 5,45
#2022: 5,39

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2016, 2023)
y = np.array([3.15,3.26,3.88,4.30,5.33,5.45,5.39])

plt.xlabel('Ano')
plt.ylabel('Valor do Real (R$)')
plt.title('Cotação do Dolar')
plt.plot(x,y , color='b', mfc='r', marker='o')
print(plt.show())