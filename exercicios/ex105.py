#faça um exp reg para validar se um exp é uma conta #matematica valida.Nessa conta só podem haver 2 numeros
#inteiros sendo somados ou subtraidos entre si.Valide se é #expressão matematica ou não.

#^  *inicia com multiplos espaços  
# (\+ *) um ou n digitos, espaços 0 n espaços
#(-|+) pode ser menos ou mais(+)sentido literal
#  *\d+ multip 0 ou espaços n digitos
# *$ fim esperado 
import re 

texto = '310-4453'
info = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto)
if info != None:
  print('Expressão válida')
else:
  print('Expressão inválida')
