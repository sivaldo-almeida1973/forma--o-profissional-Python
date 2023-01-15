numero_de_leituras = input('digite o numero de textos desejado: ')
numero_int = int(numero_de_leituras)
texto_total = " "
for i in range(numero_int):
    texto_total += input('digite o texto: ')

print('texto completo:', texto_total)