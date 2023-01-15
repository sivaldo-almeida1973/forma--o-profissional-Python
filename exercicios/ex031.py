fatorial_str = input('digite o fatorial desejado:')
fatorial_numero = int(fatorial_str)
resultado = 1

for i in range(1, fatorial_numero + 1):
    resultado *= i

print('o fatorial de %d é %d ' % (fatorial_numero, resultado))