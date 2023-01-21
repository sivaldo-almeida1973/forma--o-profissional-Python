#Protegendo Atributos com Property
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        print('pegando nome')
        return self.__nome
    
    nome = property(get_nome)

instancia = Pessoa('Maria')
print(instancia.nome)

print('-'*30)

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        print('pegando nome')
        return self.__nome
    
    def set_nome(self, nome):
      if len(nome) > 0:
        print('setando nome')
        self.__nome = nome
    
    nome = property(get_nome, set_nome)

instancia = Pessoa('Maria')
print(instancia.nome)
instancia.nome = 'Marcos'
print(instancia.nome)


print('-'*30)

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome   
    
    def set_nome(self, nome):
      if len(nome) > 0:
        print('setando nome')
        self.__nome = nome
    
    nome = property(fset = set_nome)

instancia = Pessoa('Maria')
instancia.nome = 'Marcos'
#fset, fget, fdel