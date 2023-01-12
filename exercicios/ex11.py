faltou_comida = False
hoje_sabado = True
ir_ao_mercado = faltou_comida  or hoje_sabado

print('preciso ir ao mercado hoje ?' , ir_ao_mercado)

sinal_estiver_verm = True
vem_carro_direita = False
vem_carro_esquerda = False
atravessar_rua = sinal_estiver_verm and not vem_carro_direita and not vem_carro_esquerda
print('posso atravessar a rua?' , atravessar_rua)



sinal_estiver_verm = False
vem_carro_direita = True
vem_carro_esquerda = True
atravessar_rua = sinal_estiver_verm or not vem_carro_direita or not vem_carro_esquerda
print('posso atravessar a rua?' , atravessar_rua)