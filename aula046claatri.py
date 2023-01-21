class tipo1:
    def __init__(self, outra_classe):
        self.outra = outra_classe

class tipo2:
    numero = 10

classe2 = tipo2()
classe1 = tipo1(classe2)

print(classe1.outra.numero)



print('-'*30)

class exemplo:
    def __init__(self):
        pass

lista = []
ex1 = exemplo
ex2 = exemplo

lista.append(ex1) #incluir ex1 em lista
lista.append(ex2) # incluir ex2 em lista

print(lista[0])