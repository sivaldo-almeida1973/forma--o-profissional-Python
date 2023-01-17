"""
escolha tres ojetos e crie um lista.
para armazenar o objeto e sua fução.
agora por input recba o nome desse objeto.
e imprima sua fução.caso não exista ,informe.

"""
objetos = {
    'cadeira':'serve para sntarmos',
    'balde': 'serve para colocor agua',
    'monitor':'serve para assistir'
}
objeto_procurado = input('digite o objeo:')
if objeto_procurado in objetos:
    print(objetos[objeto_procurado])
else:
    print('objeto não encontrado')