#crie uma função que leia o input do usuario e retorne 
#o que foi digitado ,mas caso o input seja interrompido 
# trate a escessão e retorne o valor None.
def ler_input_seguro():
  try:
    return input('digite algo:')
  except:
    return None

print(ler_input_seguro())