#Criando arquivo csv novamente
import csv 
with open('funcionarios.csv', 'w') as arquivo:
  escritorCsv = csv.writer(arquivo, delimiter=',')
  escritorCsv.writerow(['Idade','Nome','Peso', 'Altura','profissao','endereco'])
  escritorCsv.writerow(['22','Lucas','78.0', '1.76','Advogado','Rua Brasil'])
  escritorCsv.writerow(['27','Alice','63.5', '1.60','Eng.software','Rua Brasil'])
  escritorCsv.writerow(['35','Sivaldo','85.5', '1.70','Eng.software','Rua Brasil'])
  escritorCsv.writerow(['34','Gute','89.9', '1.65','Empresario','Rua Canada'])
  escritorCsv.writerow(['50','Maria','60.0', '1.55','Comerciante','Rua Europa'])
  
