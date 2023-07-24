import random

a = str(input('Digite o nome do aluno_1: '))
b = str(input('Digite o nome do aluno_2: '))
c = str(input('Digite o nome do aluno_3: '))
d = str(input('Digite o nome do aluno_4: '))

lista = [a, b ,c ,d]

random.shuffle(lista)

print(lista)