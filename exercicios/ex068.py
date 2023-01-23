#crie uma classe que represente uma pessoa
#ela deve possuir um nome,cpf  e um depen 
#dente, onde o dependente é outra pessoa.
#Dependente não é obrigatorio.Crie duas #instancias: pai e #filho e imprima a saida

class Pessoa:
    def __init__(self, nome,cpf,dependente=None ):
        self.nome = nome
        self.cpf  = cpf
        self.dependente = dependente

filho = Pessoa('Lucas','200.300.400-45' )
pai = Pessoa('Sivaldo',' 333.444.555.45',filho)

print('Nome:', filho.nome, 'CPF:',filho.cpf,'Dependente:',filho.dependente)
print('Nome:', pai.nome, 'CPF:',pai.cpf,'Dependente:',pai.dependente.nome)

