#Funções de objetos


print('-'*30)
class pessoa: #classe
    especie = 'Homo Sapiens'#atributo estático da classe.
    num_pessoas = 0 #atributo estático da classe
    def __init__(self, nome,idade):
        self.nome = nome #instancia de classe
        self.idade = idade # instancia de classe
        pessoa.num_pessoas += 1 #se refere a classe

pessoa1 = pessoa('Rodrigo', 34)
pessoa2 = pessoa('Lucas',22)
pessoa3 = pessoa('Alice', 34)
pessoa2 = pessoa('Sivaldo',22)

print(pessoa.num_pessoas)



print('-'*30)
class pessoa: # classe
    def __init__(self, nome,idade): #funçao (init)
        self.nome = nome #instancia de classe
        self.idade = idade #instancia da classe
    def print_nome(self): # metodo
        print('Meu nome é %s ' % (self.nome))

pessoa1 = pessoa('Lucas', '22') # variavel
pessoa2 = pessoa('Alice','38') # variavel

pessoa1.print_nome()
pessoa2.print_nome()


print('-'*30)

class pessoa: # classe
    def __init__(self, nome,idade): #funçao (init)
        self.nome = nome #instancia de classe
        self.idade = idade #instancia da classe

    def print_string(self, nome):#criei função
         print('Meu nome é %s ' % (nome))

    def print_nome(self): # criei função
        self.print_string(self.nome)

pessoa1 = pessoa('Lucas', '22') # variavel
pessoa2 = pessoa('Alice','38') # variavel

pessoa1.print_nome()
pessoa2.print_nome()




print('-'*30)
class pessoa: # classe
    def __init__(self, nome): #funçao (init)
        self.nome = nome #instancia de classe
    def inser_idade(self, idade):
        self.idade = idade
lucas = pessoa('lucas')
lucas.inser_idade(34)

print(lucas.idade)