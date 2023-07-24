display = ' -SORTEIO- '
print('{:=^20}'.format(display))
print()

import random
'''
a = str(input('Digite o nome do aluno_1: '))
b = str(input('Digite o nome do aluno_2: '))
c = str(input('Digite o nome do aluno_3: '))
d = str(input('Digite o nome do aluno_4: '))
'''
lista = [1,2,3,4]

for count in range(1,4):
    lista[count] = str(input('Digite o aluno_{}: '.format(count)))

sorteio = random.choice(lista)
print('O nome do aluno sorteado é: {}'.format(sorteio))
