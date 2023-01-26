#Criando e excluindo pastas

#como criar pasta (mkdir)

#import os
#os.mkdir('pasta')
 #remover pasta (rmdir)
#import os
#os.rmdir('pasta')#pasta deve estar vazia

#criar pasta dentro de outra pasta
#import os
#os.rmdir('pasta/pasta')

#Criar variaspasta e arquivos dentro delas
import os 
for i in range(0,10):
 nome_pasta = 'pasta' + str(i) #nome de pasta
 try:
  os.mkdir(nome_pasta)#criar a pasta
 except:
    pass

 try:
  open(nome_pasta + '/texto.txt','wt').close()
 except:
   pass

#como deletar pastas com arquivos
import shutil
for i in range(0,10):
    nome_pasta = 'pasta' + str(i)
    try:
       shutil.rmtree(nome_pasta)
    except:
       print('falha ao excluir a pasta', nome_pasta)
  


#excluir pasta e arquivos

#import os
#for i in range(0,10):
 # nome_pasta = 'pasta' + str(i) #nome de pasta
 # try:
 #   os.remove(nome_pasta + '/texto.txt')#criar a pasta
#  except:
 #     pass

  #try:
  #  os.rmdir(nome_pasta)
  #except:
  #    print('falha ao excluir a pasta', nome_pasta)


#como ver o que tem dentro de uma pasta

import os 
files = os.listdir()
print(files)

#como ver o que tem dentro de uma pasta(definir uma pasta)
import os 
files = os.listdir('teste.py')
print(files)
