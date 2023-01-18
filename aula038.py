def DeixaMaiuscula(func):
    def inner_func(texto):
        return func(texto).upper()
    return inner_func

def InsereParenteses(func):
    def inner_func(texto):
        return '(' + func(texto) + ')'
    return inner_func

@DeixaMaiuscula
@InsereParenteses
def formata_string(texto):
    return texto

print(formata_string('Olá este texto sera formatado!'))