#Criando nossos tipos
#vamos criar uma classe
import numpy

class Pessoa :
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
#criando array do numpy
array = numpy.array([Pessoa('Lucas', 22),Pessoa('Alice',38)])
print(array)
print(type(array)) #tipo para o python
print(array.dtype,  end='\n\n')#tipo para numpy

print(array[0].nome, array[0].idade)

print('-'*30)

import numpy
#outro exemplo(tipo especifico do numpy)
tipo_pessoa = numpy.dtype([ ('nome', 'S10'), ('idadde', 'i4') ])

array = numpy.array([('Rodrigo', 24),('lucas',22)], dtype= tipo_pessoa)

print(array)
print(type(array)) #tipo para o python
print(array.dtype)#tipo para numpy


