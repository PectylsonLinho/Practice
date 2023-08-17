# Biblioteca Math
# Porção inteira de um número decimal

arredondar = float(input('Digite um numero com casas decimal para mostrar porção inteira: '))
from math import(trunc)

print('A parte inteira do valor digitado é: {}'.format(trunc(arredondar)))