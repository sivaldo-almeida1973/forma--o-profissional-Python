#Graficos de Pizza, mostra o dados usando angulos,que #dificulta um pouco a analize.
#É usado com poucos dados e quando não necessecita de muita precisão
import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe Baixa', 'Classe Media','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
#(shadow=True )coloca sobra , (startangle=90) , muda o anuglo de visão
plt.figure(figsize=(8,8))#aumenta tamanho do grafico
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90)
plt.title('Distribuição de classes')
plt.legend(classes, loc='upper right')
print(plt.show())



#AUMENTAR E DIMINUIR TAM DO RAIO(radius=0.5 ,ou qualquer tamanho)
##mover fatia da pizza
import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe Baixa', 'Classe Media','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
offsets = np.array([0.2,0.03,0.03])#var mover pedaços da pizza+ (explode=offsets)

#criar bordas
edge_props ={
    'linewidth':1,
    'edgecolor':'black',
    'linestyle': 'dashed'
}
#(shadow=True )coloca sobra , (startangle=90) , muda o anuglo de visão
plt.figure(figsize=(8,8))#aumenta tamanho do grafico
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, radius=0.50 ,explode=offsets, wedgeprops=edge_props)
plt.title('Distribuição de classes')
plt.legend(classes, loc='upper right')
print(plt.show())



import matplotlib.pyplot as plt
import numpy as np

classes = np.array(['Classe Baixa', 'Classe Media','Classe alta'])
dados = np.array([10,30,80])
cores = np.array(['r','g','y'])
offsets = np.array([0.2,0.03,0.03])#var mover pedaços da pizza+ (explode=offsets)

#criar bordas
edge_props ={
    'linewidth':1,
    'edgecolor':'black',
    'linestyle': 'dashed'
}
text_props ={
    'color': 'blue',
    'style':'oblique',
    'size': 8
}
#(shadow=True )coloca sobra , (startangle=90) , muda o anuglo de visão
plt.figure(figsize=(8,8))#aumenta tamanho do grafico
plt.pie(dados, labels=classes, colors=cores, shadow=True, startangle=90, radius=0.50 ,explode=offsets, wedgeprops=edge_props, textprops=text_props, autopct= lambda value:'%.2f %s' % (value, '%'))
plt.title('Distribuição de classes')
plt.legend(classes, loc='upper right')
print(plt.show())

