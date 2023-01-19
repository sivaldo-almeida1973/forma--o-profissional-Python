def mostra_tipo(*args):
    for i in args:
        print(type(i))

mostra_tipo(1,2,3.4,'texto',True)