#crie uma função que receba argumentos de tama
#-nho arbitrário.Todos esses argumentos serão 
#números .Em seguida retorne o menor número
#entre todos os recebidos.

def menor(*numeros):#tamanho arbitrarios
    menor = numeros[0]
    for i in numeros:
        menor = min(i,menor)
    return menor

print(menor(10,20,30,1000,-2))
print(menor(10,-20,30,1000,-2))