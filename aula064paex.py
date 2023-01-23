import teste
print(teste.__name__)


print('-'*30)

#se eu quiser saber onde esse modulo esta 
import teste 
print(teste.__file__)

print('-'*30)
#modulo principal (main)
def main():
  print('aqui inicia o modulo principal')

if(__name__ == '__main__'):
        main()

print('-'*30)
# o programa é executando recebe alguns argumentos

import sys
if(__name__=='__main__'):
    print('o numero de argumentos é',len(sys.argv))
    print('argumentos são',sys.argv)

print('-'*30)

#Encerramento de programa
if (__name__=='__main__'):
  exit(1)