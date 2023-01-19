def citacao(func):
    def func_inner(str):
        return '"' + func(str).lower() + '"'
    return func

@citacao
def transforma(str):
    return str

print('E disse joão:', transforma('Só o sabio sabe!'))

 