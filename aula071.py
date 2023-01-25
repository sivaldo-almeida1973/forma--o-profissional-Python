#criar classe iteravel

class ColecaoNumeros:
  def __init__(self, numero_max): #inicializador da classe
    self.max = numero_max #parametro numero maximo
  def __iter__(self): # iplementar a clas construtor do objeto iteravel
    self.numero_atual = 1 #definir numero inicial
    return self #retorna a instancia do objeto

  def __next__(self): #criar func que vai ser execut sempre que gerar proximo elemento
    if self.numero_atual <= self.max: #lógica
      retorno = self.numero_atual #retorna
      self.numero_atual += 1 #implementação
      return retorno #variavel retorno
    else: #exceção (StopIteration)
      raise StopIteration

colecao = ColecaoNumeros(6)

for item in colecao:
  print(item)

print('-'*30)

class ColecaoNumeros:
 def __init__(self, numero_max): #inicializador da classe
  self.max = numero_max #parametro numero maximo
 def __iter__(self): # iplementar a clas construtor do objeto iteravel
  self.numero_atual = 1 #definir numero inicial
  return self #retorna a instancia do objeto

 def __next__(self): #criar func que vai ser execut sempre que gerar proximo elemento
  if self.numero_atual <= self.max: #lógica
    retorno = self.numero_atual #retorna
    self.numero_atual += 1 #implementação
    return retorno #variavel retorno
  else: #exceção (StopIteration)
    raise StopIteration

colecao = ColecaoNumeros(6)


iterador = iter(colecao)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))


