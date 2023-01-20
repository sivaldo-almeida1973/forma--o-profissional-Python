def encontra_ocorrencias(texto,caracter):
    indices = []
    indice = 0
    for char in texto:
        if char == caracter:
            indices.append(indice)
        indice += 1
    return indices

print(encontra_ocorrencias('abcdaa','a'))
print(encontra_ocorrencias('aabbccdd','d'))