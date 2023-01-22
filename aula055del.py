#Como excluir objetos
#del em listas
arr = [1,2,3,4,5,]
del arr[2]
print(arr)

#Del em classes

class Teste:
    def __init__(self):
        pass

variavel = Teste()
#del variavel
print(variavel)



print('-'*20)


class Teste:
    def __init__(self, num):
        self.num = num

variavel = Teste(10)
print(variavel.num)

#del variavel.num

print(variavel.num)

print('-'*20)

#como criar alerta de deletado!!!
class Teste:
    def __init__(self):
        self.lista = [1,2,3,4]
    def __del__(self):
        print('fui deletado!')
teste = Teste()
del teste


print('-'*20)

class Pessoa:
    def __init__(self,nome):
       self.__nome = nome

    def get_nome(self):
       print('pegando nome')
       return self.__nome

    def set_nome(self, nome):
        print('setando nome')
        self.__nome = nome

    def del_nome(self):
        print('deletando nome!')
        del self.__nome

    nome = property(get_nome, set_nome, del_nome)

instancia = Pessoa('larissa')
del instancia.nome

print('-'*20)

class Pessoa:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self

    @nome.deleter 
    def nome(self):
        print('deletando nome')
        del self.__nome

    instancia = Pessoa('larissa')
    del instancia.nome


