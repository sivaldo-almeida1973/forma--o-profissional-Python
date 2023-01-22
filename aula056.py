#testando tipos de objetos
#checar se um objeto pertenca a uma #determinada classe.

e_inteiro = isinstance(5, int)
print(e_inteiro)

print('-'*20)

e_inteiro = isinstance(5, (int,float, str))
print(e_inteiro)


print('-'*20)

class Base:
    def __init__(self):
        pass

classe = Base()
e_base = isinstance(classe, Base)
print(e_base)


print('-'*20)
class Base:
    def __init__(self):
        pass

class Herdeiro(Base):
    def __init__(self):
        pass

classe = Herdeiro()

e_base = isinstance(classe, Base)
e_herdeiro = isinstance(classe, Herdeiro)

print(e_base)
print(e_herdeiro)



print('-'*20)
class Base:
  def __init__(self):
    pass

class Herdeiro(Base):
  def __init__(self):
        pass

classe = Base()

e_base = isinstance(classe, Base)
e_herdeiro = isinstance(classe, Herdeiro)

print(e_base)
print(e_herdeiro)



print('-'*20)
class Base:
    def __init__(self):
        pass

class Herdeiro(Base):
    def __init__(self):
        pass

e_base = issubclass(Base, Herdeiro)
e_herdeiro = issubclass(Herdeiro, Base)

print(e_base)
print(e_herdeiro)



print('-'*20)
def soma (num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2,(int, float)):
        return num1 + num2
    else:
        return None

print(soma(1,34.3))
print(soma(True, 'Texto'))

print('-'*20)

class Veiculo:
    def __init__(self):
        pass
    def acelera(self):
        pass

class Moto(Veiculo):
    def __init__(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass
    def re(self):
        print('dando ré')

def faz_re(var):
    if isinstance(var, Carro):
        var.re()
    else:
        print( 'não tem')

motinho = Moto()
carrinho = Carro()

faz_re(motinho)
faz_re(carrinho)
