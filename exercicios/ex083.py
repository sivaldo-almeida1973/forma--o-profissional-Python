#crie uma classe que represente um caractere (string de tam 1)
#use propriedades ou crie uma função para isso (mas deixe valor privado)
#e caso o usuario tente inserir um texto gere uma excessão dizendo
#o motivo.
class Caracter:
  def __init__(self ,Caracter):
    self.__caracter = '' #prop privada
    self.caracter = Caracter #não privado

  @property #propriedade
  def caracter(self):
    return self.__caracter

  @caracter.setter  # metodo pra aceitar o valor
  def caracter(self,value):
    if len(value) > 1:  #tratamento
      raise Exception('caracter deve ter no maximo tamanho 1')

     
    self.__caracter = value #definir valor

letra = Caracter('a') # testando
print(letra.caracter)

try:
  letra.caracter = 'ab' #instanciar
except Exception as ex:
  print(str(ex))

print(letra.caracter)
 

