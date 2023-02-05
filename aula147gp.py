#Graficos Empilhados na Vertical.
import matplotlib.pyplot as plt
import numpy as np
xs = np.array(['Janeiro','Fevereiro', 'Março', 'Abril'])
time1 = np.array([5,10,15,20])
time2 = np.array([1,2,4,9])
time3 = np.array([5,8,2,2])
time4 = np.array([6,7,2,1])


plt.bar(xs,time1  ,  color='red', width=0.5)
plt.bar(xs,time2 ,bottom=time1, color='blue',  width=0.5)
plt.bar(xs, time3 ,bottom=time2+time1 , color='yellow',  width=0.5)
plt.bar(xs, time4, bottom=time1+time2+time3, color='orange',  width=0.5)

plt.title('Rendimento no Esporte')
plt.xlabel('Meses')
plt.ylabel('Gols')
plt.legend(['Tim1','Tim2','Tim3','Time4'])
print(plt.show())


#Graficos Empilhados na Orizontal.
import matplotlib.pyplot as plt
import numpy as np
xs = np.array(['Janeiro','Fevereiro', 'Março', 'Abril'])
time1 = np.array([5,10,15,20])
time2 = np.array([1,2,4,9])
time3 = np.array([5,8,2,2])
time4 = np.array([6,7,2,1])

plt.xlim(0,40) #melhra a posição da legenda
plt.barh(xs,time1  ,  color='red' )
plt.barh(xs,time2 ,left=time1, color='blue'  )
plt.barh(xs, time3 ,left=time2+time1 , color='yellow' )
plt.barh(xs, time4, left=time1+time2+time3, color='orange'  )

plt.title('Rendimento no Esporte')
plt.xlabel('Meses')
plt.ylabel('Gols')
plt.legend(['Tim1','Tim2','Tim3','Time4'])
print(plt.show())