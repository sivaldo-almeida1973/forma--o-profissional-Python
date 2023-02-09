#Machine 
#computador aprende com eventos passados
#este aprendizado é modelado: criação de um modelo
#com este modelo , ele é capaz de prever o que vai acontecer.


#modelo
#redes Neurais
#Maquina de Vetor de Suporte
#Naive Bayes
#Arvore de Decisão
#Regressão Linear
#Florestas Aleatorias

#tanformação de Dados

#Label encoding
#cada categoria recebe um numero , normalmente em ordem alfabtica

#One-hot encoding
#cada categoria é transformada em outro atributo:dummy variable
#um valor binario informa a ocorrencia

#Dummy Variable trape
# Scikit-Learn

#Conhecendo os Dados
import pandas as pd
import numpy as np
import Encoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEnconder
from scikit.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier


credito = pd.read_csv('Credit.csv')
print(credito.head())



labelencoder = LabelEncoder()
for i in credito.select_dtypes(include='object'):
  if i != 'class':
    credito[i] = labelencoder.fit_transform(credito[i])
credito.head()

