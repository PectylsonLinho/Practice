# Estou aprendendo a manipular textos!
# O primeiro exercício após a Aula - Analisador de Textos

show = 'Analisando Texto'
print('{:=^20}'.format(show))

name = str(input('Type your full name: ')).strip()
name0 = name.split()
print('''
    O teu nome escrito em Maiúsculo é: {}
    O teu nome escrito em Minuscúlo é: {}
    O teu nome tem {} letras (without space).
    O teu primeiro nome tem {} letras.
'''.format(name.upper(), name.lower(), (len(name) - name.count(' ')), len(name0[0]))
)

