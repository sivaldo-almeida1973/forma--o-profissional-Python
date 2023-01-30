#Numpy
#bliblioteca para operar sobre dados multidimensionais
#estremamente eficiente, altamente funcional
#usada em eng e ciencia de daos e computação em geral
#Tipos De Dados (foco operações matematica).

import numpy

boolean = numpy.bool_(True)
print(boolean, (type(boolean)))

print('-'*20)
#não pode ter acento (caracter ascii) 
import numpy
string = numpy.string_('este e um texto')
print(string, type(string))

print('-'*20)

#pode ter acento  classe (unicode) str 
print('-'*20)
import numpy
string = numpy.unicode_('este é um texto')
print(string, type(string))


print('-'*20)
#Tipos numericos (inteiros) de 32 bits
import numpy
inteiro = numpy.intc(-102)

#inteiro 32 bits sem sinal
uinteiro = numpy.uintc(102)

#inteiro de 64 bits
long = numpy.int64(84848484)

#inteiro de 64 bits sem sinal
ulong = numpy.uint64(34353434)

print(inteiro, type(inteiro))
print(uinteiro, type(uinteiro))
print(long, type(long))
print(ulong, type(ulong))






