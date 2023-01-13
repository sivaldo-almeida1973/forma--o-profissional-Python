#se texto possui vogal

texto = input('digite um palavra:')
possui_vogal = ('a'in texto) or ('e' in texto)or ('i' in texto) or ('o' in texto) or('u' in texto)
print('possui vogal?',possui_vogal)