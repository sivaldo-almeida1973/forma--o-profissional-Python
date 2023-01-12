"""
OPERADOR LÓGICO END:
"""
#resultado = True and False
#print(resultado)

#resultado2 = True and True
#print(resultado2)

#var1 = True
#var2 = False
#var3 = False
#print(var1 and var2 and var3)

clima_bom = False
estou_disposto = True
vou_mercado = clima_bom and estou_disposto
print('vou ao mercado? ' , (vou_mercado))

print('-'*20)

resultado = True or False
print(resultado)


resultado = False or False
print(resultado)

sei_programar = True
sei_investir = False
ganho_bom_salario = sei_programar or sei_investir
print('terei um bom salario?', ganho_bom_salario)

print('-'*20)
resultado = True
print(not resultado)

print('-'*20)
porta_aberta = True
tem_chave = True
print('estou trancado?', not porta_aberta and not tem_chave)

#Prioridade:
# NOT , AND, OR

bool1 = True or False and True
print(bool1)

bool2 = True or not False
print(bool2)

bool3 = True and not (True or False)
print(bool3)