media_input = input('Digite sua media na prova: ')
nota_input = input('Digite sua nota no exame: ')
media_prova = int(media_input)
nota_exame = int(nota_input)
aprovado = media_prova >= 7 or nota_exame >= 5
print('aprvação:', aprovado)
