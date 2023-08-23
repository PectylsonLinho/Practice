# Exercitando Extruturas Condiçionais
# Testando um algoritimo básico que veio em mente
# Um mini jogo simulando " Pular ou Baixar " de um Video#Game
# NOTA: Como estou aprendendo Inglês recentemente, motivo de eu estar sempre intercalando o idioma!

#import module "time" for simulate time of close
from time import sleep
close = False

while close == False:
    jump = int(input('For Jump or Down, type 1-Up & 0-Down U 9-Cancel : '))
    if jump == 1:
        print('Pulou...(^-^)')
    elif jump == 0:
        print('Baixou...(^_^)')
    elif jump == 9:
        sure = str(input(""" 
                        Tens certeza que deseja terminar? 
                        s-Sim & n-Não
                        """))
        if sure == 's':
            close = True
            sleep(2)   
            print('Sessão Terminada!')
        elif sure == 'n':
            print('Continue...')
        elif sure != 's' or 'n':
            print('Esta opção ({}) não se encontra listada !!!'.format(sure))