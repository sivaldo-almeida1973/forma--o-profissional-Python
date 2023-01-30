#Tipos de dados
import numpy
#64 bits
ponto_flutuante = numpy.float_(10002.34)
#32 bits
ponto_flutuante2 = numpy.float32(3994.34)
print(ponto_flutuante, type(ponto_flutuante))
print(ponto_flutuante2, type(ponto_flutuante2))

print('-'*30)
#tipos com menos capacidade
#int de 8 bits
int8 = numpy.int8(20)
int16 = numpy.int16(1000)
uint8 = numpy.uint8(34)
uint16 = numpy.uint16(344)
float16 = numpy.float16(16)

print(int8, type(int8))
print(int16, type(int16))
print(uint8, type(uint8))
print(uint16, type(uint16))
print(float16, type(float16))