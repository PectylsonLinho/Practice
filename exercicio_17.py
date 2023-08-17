# Trabalhando com a biblioteca MAth
# Triângulo rectângulo

style = ' -Hipotenusa de um triângulo rectangulo- '
print('{:=^100}'.format(style))

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adajacente: '))

from math import (sqrt, pow)
hipotenusa = sqrt(pow(co,2) + pow(ca,2))

print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))

'''from math import (hypot)
hipotenusa = hypot(co, ca)

print('O valor da hipotenusa é igual: {:.2f}'.format(hipotenusa))'''
