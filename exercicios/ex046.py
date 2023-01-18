"""crie uma função que receba um array de num
(int ou float), e retorne sua soma.
"""
def soma_array(arr):
    soma = 0
    for i in arr:
       soma += i
    return soma
         
print(soma_array([10,50,40]))
