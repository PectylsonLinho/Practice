# Manipulando Textos
# Analizando posição inicial e final de uma String

name = str(input('Digite uma frase: ')).lower().strip()

print("""
      A letra " A "  aparece {} vezes na frase!
      A primeira letra " A " apareceu na {}ª posição!
      A ultima letra " A " apareceu na {}ª posição!
""".format(name.count('a'), name.find('a') + 1, name.rfind('a') + 1 )
)