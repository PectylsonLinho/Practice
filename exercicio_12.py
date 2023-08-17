# Operadores Aritméticos
# Calculo de Desconto!

head = ('Produto')
print('{:*^40}'.format(head))

valor = float(input('Digite o valor do produto: '))

print(""" O valor antigo do produto é {} kz, 
      e com desconto de 5% vai custar {:.2f} kz
      """.format(valor, valor-(valor*5/100))
)
