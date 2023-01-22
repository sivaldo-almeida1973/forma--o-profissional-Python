#Protegendo Atributos com Decorators
class Natural:
    def __init__(self,Numero):
     self.__numero = Numero
    @property
    def numero(self):
     print('pegando numero')
     return self.__numero
    @numero.setter
    def numero(self,value):
     if value >= 0:
        self.__numero = value
        print('setando numero para',value)

numero = Natural(10)
numero.numero = 20
print(numero.numero)



print('-'*30)

class Pessoa:
    def __init__(self, nome):#cria prop privada igua a nome
        self.__nome = nome
    @property
    def nome(self):#ler nome
        return self.__nome.capitalize()# retorna 1º letra maiuscula
    @nome.setter
    def nome(self, value):#alterar valor
        if (len(value) != 0): #diferente de 0
            self.__nome = value

pessoa = Pessoa('lucas')
print(pessoa.nome)
pessoa.nome = 'alice'#altera para alice
print(pessoa.nome)
pessoa.nome = '' #alterar para vazio
print(pessoa.nome)

