# CONDIÇÕES
# Jogo para advinhar um numero aleatório
from random import randint
from time import sleep

panel = 'Vou pensar em um número entre 0 e 5. Tente advinhar...'
print("""
      {}
      {}
      {}
""".format(('-=-') * 20, panel, ('-=-') * 20)
)

computer = randint(0,5)

play = int(input('Em que número eu pensei? : '))

print('Processeando...')
sleep(3)

if computer == play:
    print('Parabéns Você ganhou! Eu pensei sim no numero {}'.format(computer))
else:
    print('Ganhei! Eu pensei no número {} e você pensou no número {}!'.format(computer, play))
print('Fim!')