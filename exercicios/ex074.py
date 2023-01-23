class Base1:
  def __init__(self):
    pass
  def imprime(self):
    print("Base 1")
 
class Base2:
  def __init__(self, atributo2):
    pass
  def imprime(self):
    print("Base 2")
 
class MinhaClasse(Base1, Base2):
  def __init__(self):
    pass
  def imprime(self):
    Base1.imprime(self)
    Base2.imprime(self)
 
var = MinhaClasse()
var.imprime()



class Pai: 
  def __init__(self): 
    print('Pai') 
 
class Filha(Pai):
  def __init__(self): 
    print('Filha')
 
classe = Filha()
