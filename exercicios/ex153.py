#Crie um grafico de pizza para apresentar os seguintes dados:
#Destino de exportações do Brasil:
#China:30% , Estados:Unidos 40% ,Europa:20%, Outros:10%

import matplotlib.pyplot as plt
import numpy as np

paises = np.array(['China','Estados Unidos','Europa','Outros'])
dados = np.array([30,40,20,10])
cores = np.array(['red','blue','orange','g'])#cores para cada pais
#cores para as bordas
edge_props ={
   'linewidth':1,
   'edgecolor':'black',
   'linestyle':'dashed'#pontilhado
}
#propriedades do texto
text_props ={
   'color':'black',
   'style':'oblique',
   'size':13,
   'family': 'sans'
}

plt.figure(figsize=(7,7))#tamanho do objeto
#agora dados para criar a pizza
plt.pie(dados,labels=paises, colors= cores, shadow=True, radius=0.8,startangle=90, autopct=lambda value:'%.2f %s' % (value,'%'), textprops=text_props)
plt.legend(paises, loc='lower right')#legendas
plt.tight_layout() #ajusta o layaut
print(plt.show())
