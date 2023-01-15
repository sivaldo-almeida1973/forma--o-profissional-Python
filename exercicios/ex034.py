for numero in range(3,31):
    e_primo = True

    for num_teste in range(2, numero):
        if (numero % num_teste == 0):
           e_primo = False
           break

    if (e_primo):
        print(' %d sim primo' %(numero))
    else:
        print(' %d não primo:' % (numero))
