#sem usar 'ifs', crie uma função que receba #dois numeros e retorne a soma dos mesmos,mas #o valor retornado não pode passar de 10000 e #deve ser sempre maior que 0.
def soma(num1,num2):
    soma =  num1 + num2
    soma = min(10000,soma)
    soma = max(0,soma)
    return soma

print(soma(20,20))
print(soma(5000,6000))
print(soma(10,-10))

