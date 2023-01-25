#crie uma classe iteravel chamada 'Tabuada' que calcule :
# que calcule tab. multiplicação do num recebido n construtor
#a cada iteração ele deve retornar um result da tab
#para testar use o for.
class Tabuada:
  def __init__(self, num):#construtor padrão
    self.num = num  #tab que a gente quer calcular
  def __iter__(self): #inicializador do obj iteravel
      self.atual = 0 # controla qual posiç tab calculando
      return self
  def __next__(self):# serve para cada vez que o for chamar
    self.atual +=1
    if(self.atual == 11):
      raise StopIteration #se for 11 para a iteração
    return self.atual * self.num

tabuada_calc = Tabuada(2) #ciar uma instancia da classs e inicializa com o init

for i in tabuada_calc:
  print(i)


