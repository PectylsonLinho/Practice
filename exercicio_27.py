# Manipulando Textos
# Primeiro e Ultimo nome de uma pessoa!

name = str(input('Digite o nome completo: ')).strip()
nameS = name.split()
last = len(nameS) - 1

print("""
        = ANALISANDO O TEU NOME =
      
      O teu primeiro nome é: {}
      O teu ultimo nome é: {}
""".format(nameS[0], nameS[last])
)