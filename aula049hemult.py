#Herança multipla
class base1:
    def __init__(self, atributo1):
        self.atributo1 = atributo1
    def base1_print(self):
        print('base1')

class base2:
    def __init__(self, atributo2):
        self.atributo2 = atributo2
    def base2_print(self):
        print('base2')

class minhaClasse(base1,base2):
    def __init__(self):
        base1.__init__(self, 10)
        base2.__init__(self, 20)

var = minhaClasse()
print(var.atributo1)  
print(var.atributo2)  
var.base1_print()
var.base2_print()    

       

