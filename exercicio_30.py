# Exercitando estruturas condiçionais!

panel = ' PAR OU IMPAR '
print('{:`^20}'.format(panel))

from time import sleep

number = int(input('Digita um numero qualquer: '))
print('Analizando...')
sleep(3)

if (number % 2) == 0:
    print('O numero {} é PAR!'.format(number))
else:
    print('O numero {} é IMPAR!'.format(number))
print('Fim!')