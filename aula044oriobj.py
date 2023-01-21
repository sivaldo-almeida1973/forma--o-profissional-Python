#Propriedades de Objetos
class teste:
    pass

minha_classe = teste()
print(type(minha_classe))

print('-'*30)
class nossaClasse:
    def __init__(self):
        print('eu existo')

var = nossaClasse()
print(type(var))

print('-'*30)
class pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        print('pessoa com o nome %s e idade %d criada'% (nome,idade))



pessoa1 = pessoa('Rodrigo', 34)
pessoa2 = pessoa('Lucas',22)

print(pessoa2.nome, pessoa2.idade)


print('-'*30)
class pessoa:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        print('pessoa com o nome %s e idade %d criada'% (nome,idade))

pessoa1 = pessoa('Lucas',22)

pessoa1.nome = "Sivaldo"
print(pessoa1.nome)



print('-'*30)
class pessoa:
    especie = 'Homo Sapiens'
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        print('pessoa com o nome %s e idade %d criada'% (nome,idade))

pessoa1 = pessoa('Rodrigo', 34)
pessoa2 = pessoa('Lucas',22)

print(pessoa1.especie)
print(pessoa2.especie)


print('-'*30)
class pessoa:
    especie = 'Homo Sapiens'
    num_pessoas = 0
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
        pessoa.num_pessoas += 1

pessoa1 = pessoa('Rodrigo', 34)
pessoa2 = pessoa('Lucas',22)
pessoa3 = pessoa('Alice', 34)
pessoa2 = pessoa('Sivaldo',22)

print(pessoa.num_pessoas)
