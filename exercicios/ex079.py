#crie um programa que tenha a entrada na função e modulo main().Ele deve receber dois numeros via parametro do programa e mostrar sua soma.Mas com uma condição: Verificar se possui dois parametros de entrada.Caso contrario parar a execução do programa a avisar qual o problema.

import sys 

if (__name__== '__main__'):
  if len(sys.argv) != 3: #se o comprimento dos argum
    print('numero de argumentos incorretos')
    sys.exit(1) # abortar programa
  numero1 = float(sys.argv[1]) # ler parametros
  numero2 = float(sys.argv[2]) # ler parametros
  print(numero1 + numero2)
  print(sys.argv[0])

  