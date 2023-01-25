#Crie uma classe que retorne os fatoriais de um numero
#no intervalo de X a Y ,recebidos por parametros no construtor da classe
class Fatorial:
  def __init__(self, x, y): #const da class
    self.x = x #propiedade x
    self.y = y #propiedade y

  def __iter__(self): # const do iterador
    self.atual = self.x #inicializa
    return self #retorma self

  @staticmethod  #metodo estatico
  def calcula_fatorial(num): # 
    result = 1 # variavel de controle
    for i in range(1, num+1): #percorrer
      result *= i # fazer o calculo atraves do met estatico
    return result 

  def __next__(self): # criar o metod next vai ser cham sepre que houver iteração com a classe
    if (self.atual == self.y + 1):#trat par iterção caso
      raise StopIteration
    result = Fatorial.calcula_fatorial(self.atual) #chama func estatica
    self.atual +=1
    return result

for i in Fatorial(1,10):#percorrer o fatorial
  print(i)



