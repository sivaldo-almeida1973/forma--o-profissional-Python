#como controlar escopocom (With)

class Lista:
    def __init__(self):
        pass

    def __enter__(self):
        print('Memoria Iniciada!')
        self.lista = [ i for i in range(0,10)]
        return self.lista

    def __exit__(self,*args, **Kwargs):
        print('Memoria Liberada!')
        del self.lista

with Lista() as temp_lista:
    for i in temp_lista:
        print(i)

print('Aqui o objeto já não existe mais!')


print('-'*30)
class Lista:
    def __init__(self):
        pass

    def __enter__(self):
        print('Memoria Iniciada!')
        self.lista = [ i for i in range(0,10)]
        return self.lista

    def __exit__(self,*args, **Kwargs):
        print('Memoria Liberada!')
        del self.lista

minha_lista = Lista()   

with minha_lista as temp_lista:
    for i in temp_lista:
        print(i)

print('Aqui o objeto já não existe mais!')
