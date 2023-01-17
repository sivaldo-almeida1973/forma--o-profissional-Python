"""percorra os numeros de 0 a 20 e crie um array,
onde caso o numero , terminar com zero o valor
devera ser '0' caso contrario devera se '-
'"""

lista = ['0' if str(x)[-1] == '0' else '-'for x in range(0,21)  ]
print(lista)