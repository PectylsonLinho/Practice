'''
Exercitando as estruturas condicionais / Decisão
Resolvendo alguns exercícios simples Sugerido pelo professor 'Gustavo Guanabara' em seu curso de Python. 
'''
panel = ' Radar Electrônico '
print('{:=^40}'.format(panel))

velocidade = float(input('Escreva a velocidade em que o carro se encontra: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("""
          Você foi multado! Excedeu o limite de Velocidade que é 80 km/h
          Multa por km = 7 kz
          A sua multa é de: {} Kz
    """.format(multa))

print('Tenha um bom dia e dirija com segurança!')
print('Fim...')