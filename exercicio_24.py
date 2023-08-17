# Manipulando textos
# Verificando as Primeiras letras de um texto!
# Exercício Simples de origem, mais com uma melhorada.

header = ' CASO DE EXISTENCIA '
print('{:=^40}'.format(header))

verify = False

while verify == False:
    name = str(input('Cidade onde eu nasci: ')).strip()

    if ( name[0:7].upper() == 'NAMIBE'):
        verify = True

        print(""" 
                Acertouuu!
                cidade onde eu nasci é: {}/Angola
        """.format(name[:7]))
    else:
        print("""
            Errouuu!
            Tente Novamente...
        """)
