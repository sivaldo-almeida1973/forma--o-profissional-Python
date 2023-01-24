#crie uma função que receba duas strings que serão #convertidadas para numeros pra serem somadas, se ao #realizar o casting acorrer um erro, gere uma #excessão informando o motivo.

def soma(str1, str2):
  try:
    num1 = float(str1)
    num2 = float(str2)
    return num1 + num2 
  except:
    raise Exception('Falha no casting')
  
print(soma('a', '2'))
