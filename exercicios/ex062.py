def retira_palavras(texto, palavras):
    for palavra in palavras:
        if palavra in texto:
            texto = texto.replace(palavra,'*')
    return texto

texto_usuario = 'não pode falar a palavra droga ou diabo no chat'
palavras_proibidas = ['droga', 'diabo']
print(retira_palavras(texto_usuario, palavras_proibidas))

