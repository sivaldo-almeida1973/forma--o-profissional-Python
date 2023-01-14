cpf = '222.222.222.22'
senha = '12345'
senha_usuário = input('Digite sua senha:')
if senha_usuário == senha:
   print('Acesso permitido esse é seu CPF: %s' % (cpf))
else:
   print('Senha incorreta:')
