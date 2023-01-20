#CRIE UMA FUÇÃO QUE RECEBA UMA STRING E UMA #LETRA DO ALFABETO.RETORNE A QUANTIDADE DE #VEZES QUE ESSA LETRA TEM NA STRING.CASO NÃO #OCORRA NENHUMA VEZ ,RETORNE 0.
def conta(texto, caractere):
    return texto.count(caractere)

print(conta('abcdaa','a'))
print(conta('aabbccdd','d'))